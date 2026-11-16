#!/usr/bin/env python3
# Add 5 price guide pages (2026-11-17 batch 2) under aggregator-site/guides/ai-subscription/.
# Same template as build_guides.py (CSS / DISCLAIMER / STORE_BOX copied verbatim).
# Prices: official pricing pages, checked via public search 2026-11-17.
# Conflicts are written as "未核实", never guessed. Store entrance: shop homepages only.
import os
BASE = os.path.expanduser("~/workspace/money-system/aggregator-site/guides")
A = os.path.join(BASE, "ai-subscription")

CSS = ("body{font-family:system-ui,-apple-system,\"PingFang SC\",\"Microsoft YaHei\",sans-serif;"
       "max-width:720px;margin:0 auto;padding:24px 16px;line-height:1.8;color:#222}"
       "h1{font-size:22px}h2{font-size:18px;margin-top:28px}a{color:#1657c9}"
       ".note{color:#666;font-size:14px}"
       ".warn{background:#fff7e6;border:1px solid #f0c36d;padding:12px 14px;font-size:14px}"
       "ul{padding-left:20px}"
       "table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.6}"
       "th,td{border:1px solid #ddd;padding:8px 10px;text-align:left;vertical-align:top}"
       "th{background:#f6f6f6}")

DISCLAIMER = ("本站只做公开价格信息汇总，不卖卡、不代充。"
              "价格为 2026-11-17 核查的官网公开价，次日可能变动，以官网为准。"
              "文末的代充店入口只指向店铺首页，不挂具体商品直购链接，"
              "店内售价、库存与售后以店内页面为准。")

STORE_BOX = """<h2>代充店入口</h2>
<p>想找人代充可以去我们的店里看，只挂店铺首页，不挂具体商品链接，售价、库存、售后以店内页面为准：</p>
<ul>
<li><a href="https://www.16688.com.cn/shop/S833876">数卡星球 · 16688店</a></li>
<li><a href="https://wzyp.cn/shop/VJX8A2B1">数卡星球 · 链动小铺</a></li>
</ul>
"""

def page(title, desc, crumb_href, crumb_name, body):
    return ("<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            "<title>" + title + "</title>\n"
            "<meta name=\"description\" content=\"" + desc + "\">\n"
            "<style>" + CSS + "</style>\n</head>\n<body>\n"
            "<p class=\"note\"><a href=\"" + crumb_href + "\">" + crumb_name + "</a> &gt; " + title + "</p>\n"
            "<div class=\"warn\"><b>先说清楚：</b>" + DISCLAIMER + "</div>\n"
            + body + "\n" + STORE_BOX +
            "<p class=\"note\">" + DISCLAIMER + "</p>\n</body>\n</html>\n")

pages = {}

pages["midjourney.html"] = page(
    "Midjourney 官方价：Basic $10/月起，年付 8 折",
    "Midjourney 官网公开价 Basic $10/月、Standard $30/月、Pro $60/月、Mega $120/月，年付 8 折。无免费档。",
    "index.html", "AI订阅官方价对照",
    """<h1>Midjourney 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>月价：<b>Basic $10/月、Standard $30/月、Pro $60/月、Mega $120/月</b>（美元，不含税，按月付）。</li>
<li>年付：一次付清全年 8 折：Basic <b>$96/年</b>（折合 $8/月）、Standard <b>$288/年</b>（$24/月）、Pro <b>$576/年</b>（$48/月）、Mega <b>$1,152/年</b>（$96/月）。</li>
<li>Fast GPU 时间（每月）：Basic 3.3 小时（200 分钟）、Standard 15 小时、Pro 30 小时、Mega 60 小时；额外 Fast 时间 $4/小时，各档相同。</li>
<li>Relax 模式：Standard 起无限 Relax 图片；Pro 与 Mega 另有无限 Relax SD 视频。Stealth 模式（作品不公开）只在 Pro 与 Mega。</li>
<li>免费与试用：无免费档；网页端与 Discord 目前无免费试用（以官网帮助页当期口径为准）。</li>
<li>商用条款：年收入超 100 万美元的公司，商用须用 Pro 或 Mega。</li>
<li>来源：Midjourney 官方计划对照页 Comparing Midjourney Plans，https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans（页面更新于 2026-05-18；多家第三方于 2026-09 至 11 月核对官网后的公开记录一致）。</li>
</ul>
<h2>适合谁</h2>
<p>偶尔出图的人，Basic 够试水；经常出图、能等 Relax 排队的人，按 Standard 起步（年付折合 $24/月）；需要作品不公开、或公司年收入超 100 万美元商用的人，须按 Pro 或 Mega 做预算。</p>
<h2>官网入口</h2>
<ul>
<li>计划对照页：<a href="https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans">https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans</a></li>
<li>官网：<a href="https://midjourney.com">https://midjourney.com</a></li>
</ul>
<p class="note">价格以官网为准。应用商店内购价与网页价不同，以下单页显示为准。</p>
""")

pages["canva-pro.html"] = page(
    "Canva Pro 官方价：年付 $144/年，月付口径未核实",
    "Canva Pro 官网公开价年付 $144/年（折合 $12/月），2026-10 月多家核对官网的记录一致；月付数字各家读数不一，本页写为未核实。",
    "index.html", "AI订阅官方价对照",
    """<h1>Canva Pro 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>年付：<b>$144/年</b>（折合 $12/月，一次付清，一人用）。2026-10 月多家核对官网定价页后的公开记录一致（coupo9 2026-10-04、mishalbrands 2026-10-24、aiproduct.reviews 2026-10-17、sagnikbhattacharya 2026-11）。</li>
<li>月付：<b>未核实</b>。第三方读数不一致：zapro.ai（2026-09-21）写月付 $15/月；moda.app（2026-09-08，脚本抓取 canva.com/pricing）与 aiproduct.reviews（2026-10-17，双档位核对）写月付 $18/月。本次核查未能直接打开官网结算页确认，因此月付数字不写，以下单页结算价为准。</li>
<li>旧口径作废：2026-06 月的 $120/年（折合 $10/月）已涨价，不再采用。</li>
<li>免费档：$0，一人用。</li>
<li>团队档：Business $250/年/人（2026-10 月读数）；原 Teams 已改名 Business。</li>
<li>来源：Canva 官网定价页 https://www.canva.com/pricing/（多家第三方 2026-09 至 11 月核对官网后的公开记录；月付数字各家读数不一致，见上）。</li>
</ul>
<h2>包含什么（官网定价页口径）</h2>
<ul>
<li>3.6M+ 模板、141M+ 高级素材、5 个品牌套件、背景移除、Magic Resize、100GB 存储。</li>
<li>Magic Studio AI 工具：Pro 的 AI 额度为免费档 10 倍（Premium / Ultra 工具），官网不再公布具体次数口径，以账号内显示为准；另有付费 AI Pass 可加购，价格以结算页为准。</li>
<li>Pro 账号仅限一人使用。</li>
</ul>
<h2>适合谁</h2>
<p>每周都要做图、做海报、做社媒封面的人。只偶尔做一张图的人，免费档一般够用；按年付 $144/年做预算，月付以结算页为准。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://www.canva.com/pricing/">https://www.canva.com/pricing/</a></li>
</ul>
<p class="note">价格以官网为准。月付数字本次未核实，下单前请在支付页再确认一次。</p>
""")

pages["elevenlabs-creator.html"] = page(
    "ElevenLabs Creator 官方价：$22/月，年付 $220/年",
    "ElevenLabs Creator 官网公开价 $22/月，年付 $220/年（折合 $18.33/月），每月 121,000 点数，约 121 分钟语音。",
    "index.html", "AI订阅官方价对照",
    """<h1>ElevenLabs Creator 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>月价：<b>$22/月</b>（美元，不含税，按月付）。</li>
<li>年付：<b>$220/年</b>，折合 $18.33/月；年付相当于 10 个月价、送 2 个月。</li>
<li>首月优惠：官网卡片曾显示首月 $11（半价），为 2026-10 月的限时口径，是否仍有效以结算页为准，不当作长期价。</li>
<li>额度：每月 <b>121,000 点数</b>，约 121 分钟语音（标准多语言模型约 1 点数兑 1 字符）；付费档未用点数可结转最多 2 个月（官网口径，以账号内为准）。</li>
<li>全档月价（同页口径）：Free $0（10,000 点数）、Starter $6/月（30,000 点数）、Creator $22/月、Pro $99/月（600,000 点数）、Scale $299/月、Business $990/月。</li>
<li>来源：ElevenLabs 官网定价页 https://elevenlabs.io/pricing（多家第三方于 2026-10-15 至 11-15 核对官网后的公开记录一致）。</li>
</ul>
<h2>包含什么（Creator 档官网口径）</h2>
<ul>
<li>商用许可、Dubbing Studio、Studio 长内容项目管理。</li>
<li>即时克隆 + 1 个专业克隆（Professional Voice Cloning），192 kbps 音频输出。</li>
<li>可加购额外点数，超额计费以账号内显示为准。</li>
</ul>
<h2>适合谁</h2>
<p>每月要出 1 小时以上配音、播客或有声内容，且需要专业克隆音色的人。每月只做几分钟配音的人，Starter（$6/月）一般够用；只试音色的人，免费档够用。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://elevenlabs.io/pricing">https://elevenlabs.io/pricing</a></li>
</ul>
<p class="note">价格以官网为准。点数按字符计费，实际分钟数随语速与模型而变，以下单页为准。</p>
""")

pages["gamma-pro.html"] = page(
    "Gamma Pro 官方价：$25/月，年付 $216/年",
    "Gamma Pro 官网公开价 $25/座位/月，年付 $216/年（折合 $18/月），每月 4,000 点数。",
    "index.html", "AI订阅官方价对照",
    """<h1>Gamma Pro 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>月价：<b>$25/座位/月</b>（美元，不含税，按月付）。</li>
<li>年付：<b>$216/年</b>，折合 $18/月，一次付清。</li>
<li>同系列：Free $0（400 点数一次性，不刷新）；Plus $12/月（年付 $108/年，折合 $9/月）；Ultra $100/月（年付 $90/月）。</li>
<li>额度：Pro 每月 <b>4,000 点数</b>，未用点数最多结转至 2 倍月额度。</li>
<li>来源：Gamma 官网定价页 https://gamma.app/pricing（多家第三方于 2026-10-01 至 11-08 核对官网后的公开记录一致）。</li>
</ul>
<h2>包含什么（Pro 档官网口径）</h2>
<ul>
<li>高级 AI 图片模型、自定义品牌、详细分析、高级分享。</li>
<li>API 接入、自定义字体、密码保护、页眉页脚、最多 10 个自定义域名。</li>
<li>每次提示最多 100 张卡片（Plus 与免费档上限更低）。</li>
</ul>
<h2>适合谁</h2>
<p>每周都要用 AI 做演示文稿、且要去掉 Gamma 品牌、挂自己域名、看详细阅读数据的人。只偶尔做一次演示的人，免费档或 Plus 一般够用；注意 Pro 是按座位计费，人多时先算总价。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://gamma.app/pricing">https://gamma.app/pricing</a></li>
</ul>
<p class="note">价格以官网为准。点数按生成消耗，实际用量以账号内显示为准。</p>
""")

pages["notion.html"] = page(
    "Notion 官方价：Plus $10/人/月起，完整 Notion AI 只在 Business 档",
    "Notion 官网公开价 Plus $10/人/月（年付）、Business $20/人/月（年付）；2025 年 5 月起独立 AI 附加包停售，完整 Notion AI 只含在 Business 及以上档。",
    "index.html", "AI订阅官方价对照",
    """<h1>Notion 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>Plus：<b>$10/人/月</b>（年付），月付 $12/人/月。</li>
<li>Business：<b>$20/人/月</b>（年付），月付 $24/人/月。</li>
<li>Free：$0；企业档：询价。</li>
<li>年付比月付便宜约 17%（Plus $10 对 $12，Business $20 对 $24）。</li>
<li>来源：Notion 官网定价页 https://notion.com/pricing（多家第三方于 2026-07-16 至 11-03 核对官网后的公开记录一致）。</li>
</ul>
<h2>重要说明：Notion AI 不是单独加购的</h2>
<ul>
<li>2025 年 5 月前，任何档都可加购独立 Notion AI 附加包（约 $8–$10/人/月）；2025 年 5 月起该附加包已停售新购。</li>
<li>现在完整 Notion AI（Notion Agent、AI 会议笔记、企业搜索）只包含在 <b>Business 及以上档</b>；Free 与 Plus 只有有限试用，不能单独加购。</li>
<li>新开工作区想用完整 AI，实际预算应按 Business $20/人/月（年付）算，而不是 Plus 价加附加包。</li>
<li>自定义 Agent 另按点数计费：$10/1,000 点数（2026-05-04 起收费，以官网为准）。</li>
</ul>
<h2>适合谁</h2>
<p>只用 Notion 做笔记、管项目、协作的人，按 Plus 做预算；每天要靠 AI 写、查、开会记笔记的人，按 Business 做预算；注意 Business 是按人头全员计费，不能只给几个人买 AI。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://notion.com/pricing">https://notion.com/pricing</a></li>
</ul>
<p class="note">价格以官网为准。不同地区按当地货币结算，金额以结算页显示为准。</p>
""")

for name, html in pages.items():
    with open(os.path.join(A, name), "w", encoding="utf-8") as f:
        f.write(html)
print("wrote new pages:", len(pages))
for n in sorted(pages):
    print(n)

# ---- patch ai-subscription/index.html: table rows + detail list + desc ----
idx_path = os.path.join(A, "index.html")
idx = open(idx_path, encoding="utf-8").read()
row_anchor = """<tr><td><a href="cursor.html">Cursor Pro</a></td><td>$20/月（老用户续用价；新用户见详情页）</td><td>$16/月（$192/年）</td><td><a href="https://cursor.com/pricing">cursor.com/pricing</a></td></tr>"""
new_rows = row_anchor + """
<tr><td><a href="midjourney.html">Midjourney</a></td><td>Basic $10/月起（Standard $30、Pro $60、Mega $120）</td><td>8 折：$96/$288/$576/$1,152/年</td><td><a href="https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans">Midjourney 计划对照页</a></td></tr>
<tr><td><a href="canva-pro.html">Canva Pro</a></td><td>月付未核实（见详情页）</td><td>$12/月（$144/年）</td><td><a href="https://www.canva.com/pricing/">canva.com/pricing</a></td></tr>
<tr><td><a href="elevenlabs-creator.html">ElevenLabs Creator</a></td><td>$22/月</td><td>$18.33/月（$220/年）</td><td><a href="https://elevenlabs.io/pricing">elevenlabs.io/pricing</a></td></tr>
<tr><td><a href="gamma-pro.html">Gamma Pro</a></td><td>$25/座位/月</td><td>$18/月（$216/年）</td><td><a href="https://gamma.app/pricing">gamma.app/pricing</a></td></tr>
<tr><td><a href="notion.html">Notion（Plus / Business）</a></td><td>Plus $12/人/月，Business $24/人/月（月付）</td><td>Plus $10、Business $20/人/月（年付）</td><td><a href="https://notion.com/pricing">notion.com/pricing</a></td></tr>"""
assert row_anchor in idx, "cursor row anchor missing"
idx = idx.replace(row_anchor, new_rows, 1)

list_anchor = """<li><a href="cursor.html">Cursor Pro：$20/月为老用户续用价，新用户走 The X Subscription</a></li>"""
new_list = list_anchor + """
<li><a href="midjourney.html">Midjourney：Basic $10/月起，年付 8 折</a></li>
<li><a href="canva-pro.html">Canva Pro：年付 $144/年，月付口径未核实</a></li>
<li><a href="elevenlabs-creator.html">ElevenLabs Creator：$22/月，年付 $220/年</a></li>
<li><a href="gamma-pro.html">Gamma Pro：$25/月，年付 $216/年</a></li>
<li><a href="notion.html">Notion：Plus $10/人/月起，完整 Notion AI 只在 Business 档</a></li>"""
assert list_anchor in idx, "cursor list anchor missing"
idx = idx.replace(list_anchor, new_list, 1)

idx = idx.replace(
    "ChatGPT Plus、Claude Pro、Google AI Pro、Perplexity Pro、Grok、Cursor Pro 的官网公开月价与年付折算对照，逐条标注来源与核查日期。",
    "ChatGPT Plus、Claude Pro、Google AI Pro、Perplexity Pro、Grok、Cursor Pro、Midjourney、Canva Pro、ElevenLabs Creator、Gamma Pro、Notion 的官网公开月价与年付折算对照，逐条标注来源与核查日期。",
    1)
note_anchor = "<li>来源：各产品官网定价页，核查日期 2026-11-17（通过公开检索核对官网口径）。</li>"
assert note_anchor in idx, "source note anchor missing"
idx = idx.replace(note_anchor, note_anchor + "\n<li>2026-11-17 新增 Midjourney、Canva Pro、ElevenLabs Creator、Gamma Pro、Notion 五页；Canva Pro 月付数字各家读数不一致，详情页写为未核实。</li>", 1)
open(idx_path, "w", encoding="utf-8").write(idx)
print("patched ai-subscription/index.html")

# ---- patch sitemap.xml ----
sm_path = os.path.expanduser("~/workspace/money-system/aggregator-site/sitemap.xml")
sm = open(sm_path, encoding="utf-8").read()
cursor_url = """  <url>
    <loc>https://xwdeshenghuo.github.io/rights-price-hub/guides/ai-subscription/cursor.html</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>"""
assert cursor_url in sm, "cursor sitemap anchor missing"
new_urls = cursor_url + """
  <url>
    <loc>https://xwdeshenghuo.github.io/rights-price-hub/guides/ai-subscription/midjourney.html</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://xwdeshenghuo.github.io/rights-price-hub/guides/ai-subscription/canva-pro.html</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://xwdeshenghuo.github.io/rights-price-hub/guides/ai-subscription/elevenlabs-creator.html</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://xwdeshenghuo.github.io/rights-price-hub/guides/ai-subscription/gamma-pro.html</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://xwdeshenghuo.github.io/rights-price-hub/guides/ai-subscription/notion.html</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>"""
sm = sm.replace(cursor_url, new_urls, 1)
open(sm_path, "w", encoding="utf-8").write(sm)
print("patched sitemap.xml (now 21 urls)")
