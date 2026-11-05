#!/usr/bin/env python3
"""
权益货源价榜 · 公开报价采集脚本（零第三方依赖，纯标准库）

数据来源：各货源站对游客公开的商品接口（同「diy 模板」站群）。
每站流程：抓首页 -> 定位 app.js -> 提取站点自带的公开 SIGN_KEY ->
按前端同款算法生成 Sign 头 -> POST /front/diy/goods/index 按关键词取价。
只采集已在人工验活中确认为「可采」的站点（见 grading.csv / ADAPTERS）。
礼貌限速：站间与关键词间均 sleep，单站失败即跳过该站，不重试轰炸。

用法：
  python3 scripts/collect.py            # 采集并更新 ../data.json
  python3 scripts/collect.py --dry-run  # 只打印将写入的报价，不改文件
"""
import hashlib
import json
import re
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TODAY = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")
ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}

# 已验证可采的同模板站（name 与 data.json 的 source 保持一致）
ADAPTERS = [
    ("万屿数卡", "vip.wanyuw.top"),
    ("优享票易", "vip.egzs.cn"),
    ("小乐权益", "123.xiaoleyingshi.com"),
    ("ABC数卡", "abc.101s.cc"),
    ("福气惠卡券", "www.fuqih.com"),
    ("91会员权益", "qy.91qy.cn"),
    ("九六城堡", "9696.zybk.net"),
    ("迅捷权益", "www.ssmvip6.top"),
    ("零点权益", "vip.lind0.cn"),
    ("北归权益", "mdl.9ip.top"),
    ("佰润权益", "shop.bairunqy.com"),
    ("聚合权益", "shop.jhmdl.cn"),
]

KEYWORDS = {
    "爱奇艺": "爱奇艺 会员",
    "腾讯视频": "腾讯视频 会员",
    "网易云": "网易云 音乐 会员",
    "瑞幸": "瑞幸 咖啡",
    "麦当劳": "麦当劳 餐饮",
    "肯德基": "肯德基 餐饮",
    "京东E卡": "京东E卡 礼品卡",
    "星巴克": "星巴克 咖啡",
}
PER_SITE_PER_KW = 3          # 每站每品类最多保留的报价条数（取最便宜的几条）
REQUEST_GAP = 0.6            # 礼貌限速（秒）


def http_get(url, timeout=35):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "ignore")


def make_sign(key):
    ts = str(int(time.time()))
    inner = hashlib.md5(("front" + key).encode()).hexdigest()
    mid = hashlib.md5((inner + ts).encode()).hexdigest()
    return hashlib.md5(mid.encode()).hexdigest() + ts


def fetch_sign_key(domain):
    html = http_get(f"https://{domain}/")
    m = re.findall(r"static/js/(app\.[a-z0-9]+\.js)", html)
    if not m:
        raise RuntimeError("首页未找到 app.js（模板不符）")
    js = http_get(f"https://{domain}/template/front/diy/static/js/{m[0]}", timeout=45)
    k = re.search(r'VUE_APP_SIGN_KEY:"([a-f0-9]+)"', js)
    if not k:
        raise RuntimeError("app.js 未找到 SIGN_KEY")
    return k.group(1)


def fetch_goods(domain, key, keyword):
    payload = json.dumps({"cid": [], "page": 1, "limit": 30,
                          "is_count": 1, "keyword": keyword}).encode()
    req = urllib.request.Request(
        f"https://{domain}/front/diy/goods/index", data=payload,
        headers={**UA, "Sign": make_sign(key), "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = json.loads(resp.read().decode("utf-8", "ignore"))
    if data.get("code") != 200:
        raise RuntimeError(f"接口拒绝 code={data.get('code')} msg={data.get('msg')}")
    return data.get("data", {}).get("list", [])


HIGH_RISK_MARKS = ("转赠", "共享", "兑换链接", "链接直冲", "仅手机号", "仅移动号", "极速版授权")


def normalize(item, source_name, kw_label):
    name = re.sub(r"\s+", " ", str(item.get("goods_name", ""))).strip()
    try:
        price = float(item.get("goods_price"))
    except (TypeError, ValueError):
        return None
    if not name or price < 1:             # 过滤占位/异常低价条目
        return None
    # 面值只认商品名里写的面额（接口 face_value 是参考价，不可信）
    face = None
    dm = re.search(r"(\d+(?:\.\d+)?)\s*元", name)
    if dm:
        denom = float(dm.group(1))
        if "E卡" in kw_label and denom < 10:   # 1 元面额 E 卡是引流噪音
            return None
        if denom > price:
            face = int(denom) if denom == int(denom) else denom
    if "链接" in name or "CDK" in name.upper():
        gtype = "链接直冲" if "链接" in name else "CDK"
    elif "卡密" in name:
        gtype = "卡密"
    elif "代下" in name:
        gtype = "代下单"
    elif "慢充" in name:
        gtype = "人工代充"
    elif "直充" in name:
        gtype = "直充"
    else:
        gtype = "自动充值"
    risk = "normal"
    if any(mk in name for mk in HIGH_RISK_MARKS):
        risk = "high"
    elif "质保" in name:
        risk = "warn"
    row = {"name": name, "kw": kw_label, "price": round(price, 3),
           "source": source_name, "type": gtype, "risk": risk,
           "checked": TODAY, "note": "公开商品接口采集"}
    if face:
        row["face"] = face
    if "年卡" in name or "年会员" in name:
        row["per"] = f"约¥{price / 12:.1f}/月"
    elif "季卡" in name:
        row["per"] = f"约¥{price / 3:.1f}/月"
    stock = item.get("stock_num")
    if isinstance(stock, (int, float)) and 0 < stock < 100:
        row["note"] += f"；库存 {int(stock)}"
    return row


def collect_site(source_name, domain):
    key = fetch_sign_key(domain)
    rows = []
    for kw, label in KEYWORDS.items():
        items = fetch_goods(domain, key, kw)
        cand = []
        for it in items:
            if it.get("status") != 1:
                continue
            r = normalize(it, source_name, label)
            if r:
                cand.append(r)
        cand.sort(key=lambda r: r["price"])
        rows.extend(cand[:PER_SITE_PER_KW])
        time.sleep(REQUEST_GAP)
    return rows


def main():
    dry = "--dry-run" in sys.argv
    existing = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    adapter_names = {n for n, _ in ADAPTERS}
    kept = [q for q in existing["quotes"] if q.get("source") not in adapter_names]
    fresh, failed = [], []
    for name, domain in ADAPTERS:
        try:
            rows = collect_site(name, domain)
            fresh.extend(rows)
            print(f"[OK] {name} ({domain}): {len(rows)} 条")
        except Exception as exc:  # 单站失败不中断整体
            failed.append((name, str(exc)[:100]))
            print(f"[FAIL] {name} ({domain}): {exc}")
        time.sleep(REQUEST_GAP)
    seen, merged = set(), []
    for q in kept + fresh:
        k = (q["name"], q["source"])
        if k not in seen:
            seen.add(k)
            merged.append(q)
    merged.sort(key=lambda q: (q.get("kw", ""), q["price"]))
    out = {"updated": TODAY,
           "note": f"{TODAY} 更新：种子人工实查 + 公开接口自动采集"
                   f"（适配站 {len(ADAPTERS) - len(failed)}/{len(ADAPTERS)} 成功）",
           "quotes": merged}
    print(f"合计报价 {len(merged)} 条，独立源 {len({q['source'] for q in merged})} 个；"
          f"失败站：{failed if failed else '无'}")
    if dry:
        print(json.dumps(out, ensure_ascii=False)[:800], "...")
        return
    DATA_FILE.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"已写入 {DATA_FILE}")


if __name__ == "__main__":
    main()
