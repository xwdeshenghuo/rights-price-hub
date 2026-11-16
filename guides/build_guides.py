#!/usr/bin/env python3
# Price guide pages under aggregator-site/guides/ - info pages.
# Prices: official pricing pages, checked via public search 2026-11-17.
# Store entrance (user approved 2026-11-17): links to the two shop homepages
# only, no product deep links, no promo language. No selling on these pages.
import os
BASE = os.path.expanduser("~/workspace/money-system/aggregator-site/guides")
os.makedirs(os.path.join(BASE, "ai-subscription"), exist_ok=True)
os.makedirs(os.path.join(BASE, "video-music"), exist_ok=True)

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

def page(title, desc, crumb_href, crumb_name, body, sisters=False):
    sis = ""
    if sisters:
        sis = """<h2>姊妹站</h2>
<ul>
<li><a href="https://xwdeshenghuo.github.io/rights-price-hub/">权益价榜首页</a></li>
<li><a href="https://xwdeshenghuo.github.io/creator-ai-tools/">创作者AI工具榜</a></li>
<li><a href="https://xwdeshenghuo.github.io/bottle-cap-guide/">瓶盖码指南</a></li>
</ul>
"""
    return ("<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            "<title>" + title + "</title>\n"
            "<meta name=\"description\" content=\"" + desc + "\">\n"
            "<style>" + CSS + "</style>\n</head>\n<body>\n"
            "<p class=\"note\"><a href=\"" + crumb_href + "\">" + crumb_name + "</a> &gt; " + title + "</p>\n"
            "<div class=\"warn\"><b>先说清楚：</b>" + DISCLAIMER + "</div>\n"
            + body + "\n" + STORE_BOX + sis +
            "<p class=\"note\">" + DISCLAIMER + "</p>\n</body>\n</html>\n")

pages = {}

# ================= A组 index =================
pages["ai-subscription/index.html"] = page(
    "AI订阅官方价对照：ChatGPT Plus、Claude Pro、Gemini Pro 等官网月价",
    "ChatGPT Plus、Claude Pro、Google AI Pro、Perplexity Pro、Grok、Cursor Pro 的官网公开月价与年付折算对照，逐条标注来源与核查日期。",
    "../../index.html", "权益价榜首页",
    """<h1>AI订阅官方价对照</h1>
<p>下表只列各家官网定价页公开的个人档价格（美元，按月付口径），不是供货价、不是代充价。年付折合月价的算法写在表下：年付总额 ÷ 12。各地税费、应用商店内购价、限时活动价可能不同，以下单页显示为准。</p>
<h2>总览（核查日期 2026-11-17）</h2>
<table>
<tr><th>产品</th><th>官网月价（按月付）</th><th>年付折合月价</th><th>官网入口</th></tr>
<tr><td><a href="chatgpt-plus.html">ChatGPT Plus</a></td><td>$20/月</td><td>无年付；按月付 12 个月共 $240</td><td><a href="https://chatgpt.com/pricing">chatgpt.com/pricing</a></td></tr>
<tr><td><a href="claude-pro.html">Claude Pro</a></td><td>$20/月</td><td>$16.67/月（$200/年，官网标 $17/月）</td><td><a href="https://claude.com/pricing">claude.com/pricing</a></td></tr>
<tr><td><a href="gemini-pro.html">Google AI Pro（Gemini Pro）</a></td><td>$19.99/月</td><td>$16.67/月（$199.99/年）</td><td><a href="https://gemini.google/subscriptions">gemini.google/subscriptions</a></td></tr>
<tr><td><a href="perplexity-pro.html">Perplexity Pro</a></td><td>$20/月</td><td>$16.67/月（$200/年，官网 Pro 页标 $17/月）</td><td><a href="https://www.perplexity.ai/hub/pricing">perplexity.ai/hub/pricing</a></td></tr>
<tr><td><a href="grok.html">Grok（SuperGrok）</a></td><td>$30/月（改版前官网价，见详情页说明）</td><td>$25/月（$300/年）</td><td><a href="https://x.ai/pricing">x.ai/pricing</a></td></tr>
<tr><td><a href="cursor.html">Cursor Pro</a></td><td>$20/月（老用户续用价；新用户见详情页）</td><td>$16/月（$192/年）</td><td><a href="https://cursor.com/pricing">cursor.com/pricing</a></td></tr>
</table>
<p class="note">算法说明：年付折合月价 = 年付总额 ÷ 12。Claude Pro 年付 $200 ÷ 12 = $16.67，官网页面四舍五入标为 $17/月；Google AI Pro 年付 $199.99 ÷ 12 = $16.67；Perplexity Pro 年付 $200 ÷ 12 = $16.67，官网 Pro 页标 $17/月；Cursor Pro 年付 $192 ÷ 12 = $16。ChatGPT Plus 官网帮助中心写明不支持年付。</p>
<h2>分产品详情</h2>
<ul>
<li><a href="chatgpt-plus.html">ChatGPT Plus：$20/月，无年付</a></li>
<li><a href="claude-pro.html">Claude Pro：$20/月，年付 $200</a></li>
<li><a href="gemini-pro.html">Google AI Pro（Gemini Pro）：$19.99/月，年付 $199.99</a></li>
<li><a href="perplexity-pro.html">Perplexity Pro：$20/月，年付 $200</a></li>
<li><a href="grok.html">Grok（SuperGrok）：$30/月，2026-10 月改版后新用户档位口径有变</a></li>
<li><a href="cursor.html">Cursor Pro：$20/月为老用户续用价，新用户走 The X Subscription</a></li>
</ul>
<h2>口径说明</h2>
<ul>
<li>以上均为美国区官网标价（美元，不含税）。其他地区按当地货币结算，金额以结算页为准。</li>
<li>应用商店（App Store / Google Play）内购价可能与官网网页价不同，以下单页为准。</li>
<li>Grok 与 Cursor 在 2026-10 月调整过订阅结构，详情页已按查到的口径分别标注，冲突处写明未核实，不猜测。</li>
<li>来源：各产品官网定价页，核查日期 2026-11-17（通过公开检索核对官网口径）。</li>
</ul>
""", sisters=True)

# ================= A组详情 =================
pages["ai-subscription/chatgpt-plus.html"] = page(
    "ChatGPT Plus 官方价：$20/月，无年付",
    "ChatGPT Plus 官网公开价 $20/月，按月计费，不支持年付。包含高级推理模型、Codex、深度研究等。",
    "index.html", "AI订阅官方价对照",
    """<h1>ChatGPT Plus 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>月价：<b>$20/月</b>（美元，不含税，按月计费）。</li>
<li>年付：官网帮助中心写明不支持年付，也不支持一次付多个月。按月付 12 个月共 $240，无年付折扣。</li>
<li>来源：OpenAI 官网定价页 chatgpt.com/pricing；OpenAI 帮助中心《What is ChatGPT Plus?》https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus（其中写明 Price: $20/month, billed monthly）。</li>
</ul>
<h2>包含什么（官网定价页口径）</h2>
<ul>
<li>高级推理模型、扩展的消息与上传额度、更准确的图片生成、扩展的深度研究。</li>
<li>扩展的记忆与上下文、Projects、定时任务、自定义 GPT。</li>
<li>Codex 使用额度扩展，ChatGPT Work（桌面 / 网页 / 移动端）。</li>
<li>API 用量不包含在 Plus 内，单独按量计费。</li>
</ul>
<h2>适合谁</h2>
<p>每天使用 ChatGPT 处理写作、查资料、写代码等个人任务，且免费版额度不够用的人。只偶尔问几个问题的人，免费版一般够用。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://chatgpt.com/pricing">https://chatgpt.com/pricing</a></li>
<li>帮助中心：<a href="https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus">https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus</a></li>
</ul>
<p class="note">价格以官网为准。不同地区结算货币与税费以结算页显示为准。</p>
""")

pages["ai-subscription/claude-pro.html"] = page(
    "Claude Pro 官方价：$20/月，年付 $200",
    "Claude Pro 官网公开价 $20/月，年付 $200（折合 $16.67/月，官网标 $17/月）。包含 Opus、Sonnet、Haiku 与 Claude Code。",
    "index.html", "AI订阅官方价对照",
    """<h1>Claude Pro 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>月价：<b>$20/月</b>（美元，不含税，按月付）。</li>
<li>年付：<b>$200/年</b>，一次付清；$200 ÷ 12 = $16.67/月，官网页面标为 $17/月。比按月付 12 个月（$240）少 $40。</li>
<li>来源：Anthropic 官网定价页 claude.com/pricing（多家第三方于 2026-10 月至 11 月初核对官网后的公开记录一致）。</li>
</ul>
<h2>包含什么（官网定价页口径）</h2>
<ul>
<li>Opus、Sonnet、Haiku 模型，至少 5 倍于免费版的用量（每 5 小时窗口计），另有每周用量上限。</li>
<li>Claude Code 包含在同一用量池内。</li>
<li>优先访问、扩展的上下文与项目功能（以官网定价页当期列表为准）。</li>
<li>官网注明：显示价格不含适用税费；移动端应用内价格可能不同。</li>
</ul>
<h2>适合谁</h2>
<p>每天用 Claude 写代码、写长文、做研究，且免费版额度不够用的人。Pro 是目前唯一提供年付折扣的个人档。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://claude.com/pricing">https://claude.com/pricing</a></li>
</ul>
<p class="note">价格以官网为准。不同地区按当地货币结算，金额以结算页显示为准。</p>
""")

pages["ai-subscription/gemini-pro.html"] = page(
    "Google AI Pro（Gemini Pro）官方价：$19.99/月",
    "Google AI Pro 官网公开价 $19.99/月，年付 $199.99。谷歌不单卖名为 Gemini Pro 的计划，Pro 模型包含在 Google AI Pro 内。",
    "index.html", "AI订阅官方价对照",
    """<h1>Google AI Pro（Gemini Pro）官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>月价：<b>$19.99/月</b>（美元，不含税，按月付）。</li>
<li>年付：<b>$199.99/年</b>，$199.99 ÷ 12 = $16.67/月。</li>
<li>来源：Google 官网订阅页 gemini.google/subscriptions（页面同时列出免费档 $0、Google AI Plus $4.99/月、Google AI Pro $19.99/月、Google AI Ultra $99.99/月起）。</li>
<li>名称说明：谷歌不单卖一个叫“Gemini Pro”的计划；Gemini Pro 模型的使用权限包含在 Google AI Pro 计划内。此前名称为 Gemini Advanced / Google One AI Premium，2025 年 5 月改名为 Google AI Pro。</li>
</ul>
<h2>包含什么（官网订阅页口径）</h2>
<ul>
<li>Gemini 4 Argon 与 Pro 模型使用权限，4 倍于免费版的用量。</li>
<li>5 TB 云存储，Gemini 进 Gmail、Docs 等 Google 应用。</li>
<li>Flow 视频生成积分每月 1,000，YouTube Premium Lite（按地区提供）。</li>
</ul>
<h2>适合谁</h2>
<p>已在用 Google 全家桶（Gmail、Docs、Drive），且需要更高模型用量与 5 TB 存储的人。只用 Gemini 问答、不需要存储与视频功能的人，免费档或 Plus 档可能已够用。</p>
<h2>官网入口</h2>
<ul>
<li>订阅页：<a href="https://gemini.google/subscriptions">https://gemini.google/subscriptions</a></li>
</ul>
<p class="note">价格以官网为准。美国大学生等特定人群的免费期为限时活动，不在上表内，以下单页为准。</p>
""")

pages["ai-subscription/perplexity-pro.html"] = page(
    "Perplexity Pro 官方价：$20/月，年付 $200",
    "Perplexity Pro 官网公开价 $20/月，年付 $200。官网定价页与 Pro 单页对年付的标法不同，预算按月价算。",
    "index.html", "AI订阅官方价对照",
    """<h1>Perplexity Pro 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>月价：<b>$20/月</b>（美元，按月付）。</li>
<li>年付：<b>$200/年</b>，$200 ÷ 12 = $16.67/月；官网 Pro 单页把年付标为 $17/月。两个数字是同一笔年付的不同标法，预算按 $20/月算，年付一次性付 $200。</li>
<li>来源：Perplexity 官网定价页 https://www.perplexity.ai/hub/pricing（多家第三方于 2026-07 月至 10 月核对官网后的公开记录一致）。</li>
</ul>
<h2>包含什么（官网定价页口径）</h2>
<ul>
<li>模型选择、深度研究（Deep Research）、Perplexity Computer。</li>
<li>4,000 奖励积分（一次性），文件上传与素材生成额度为免费版的 10 倍。</li>
<li>API 按量单独计费，不包含在 Pro 内。</li>
</ul>
<h2>适合谁</h2>
<p>每天靠搜索做研究、查资料、做文件整理的人。只偶尔查一两个问题的人，免费版一般够用。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://www.perplexity.ai/hub/pricing">https://www.perplexity.ai/hub/pricing</a></li>
</ul>
<p class="note">价格以官网为准。不同地区与应用商店内购价可能不同，以下单页为准。</p>
""")

pages["ai-subscription/grok.html"] = page(
    "Grok（SuperGrok）官方价：$30/月，2026-10 月改版后新用户档位未核实",
    "SuperGrok 官网曾列价 $30/月。2026-10 月 xAI 调整订阅结构后，新用户可买档位口径有变，本页如实标注，未核实的不写。",
    "index.html", "AI订阅官方价对照",
    """<h1>Grok（SuperGrok）官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>SuperGrok：<b>$30/月</b>，年付 $300/年（$300 ÷ 12 = $25/月）。这是 xAI 官网定价页 x.ai/pricing 在 2026-08 月下旬的读数。</li>
<li>SuperGrok Plus：$100/月，年付 $1,000/年（同期官网读数）。</li>
<li>来源：xAI 官网定价页 https://x.ai/pricing（2026-08 月下旬第三方核对官网后的公开记录）。</li>
</ul>
<h2>重要说明：2026-10 月改版，新用户档位未核实</h2>
<ul>
<li>2026-10 月的第三方核查记录称，xAI 已调整订阅结构，新档位为 Premium $30/月、Super $100/月、Ultra $200/月，SuperGrok 与 SuperGrok Plus 不再向新用户出售。</li>
<li>本次核查未能直接打开官网结算页确认新用户当前可买的档位与价格，因此<b>新用户当前可买档位与价格写为“未核实”</b>，不把改版前的 $30 当作新用户现价，也不把第三方转述的改版后价格当作已核实的官网价。</li>
<li>已持有 SuperGrok 的老用户续费价以账号内显示为准。</li>
</ul>
<h2>包含什么（改版前官网定价页口径，仅供参考）</h2>
<ul>
<li>SuperGrok：旗舰 Grok 模型（当时为 Grok 4.6）、更高用量、图片与视频生成、Expert 深度搜索模式、Grok Bot。</li>
<li>SuperGrok Plus：用量更大、1080p 视频、最快响应、高峰期优先、功能抢先体验。</li>
<li>官网定价页不公布各档具体的每日 / 每月生成数量，订阅前以官网当期页面为准。</li>
</ul>
<h2>适合谁</h2>
<p>重度使用 Grok 做 X 平台实时搜索、图片与视频生成的人。只用 Grok 做文字问答的人，免费档一般够用；是否订阅以官网结算页当期价格为准。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://x.ai/pricing">https://x.ai/pricing</a></li>
</ul>
<p class="note">价格以官网为准。本页改版说明如与官网当期页面不一致，以官网当期页面为准。</p>
""")

pages["ai-subscription/cursor.html"] = page(
    "Cursor Pro 官方价：$20/月为老用户续用价，新用户走 The X Subscription",
    "Cursor Pro 官网曾列价 $20/月。2026-10 月起新用户走 The X Subscription，Pro 对应档为 Premium $30/月，本页分别标注。",
    "index.html", "AI订阅官方价对照",
    """<h1>Cursor Pro 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>Cursor Pro（老用户续用价）：<b>$20/月</b>，年付 $192/年（$192 ÷ 12 = $16/月，年付为月价的 8 折）。</li>
<li>新用户：2026-10 月起，Cursor 改为 The X Subscription 销售，新用户可选 Free $0、Plus $8/月、Premium $30/月、Super $100/月、Ultra $200/月；Cursor 官方把老 Pro 档对应为 Premium（$30/月）。Pro、Pro+、Ultra 已为老用户保留档，新用户不能再买。</li>
<li>来源：Cursor 官网定价页 cursor.com/pricing（2026-08 月至 10 月第三方核对官网后的公开记录；改版口径来自 Cursor 官方文档的第三方核查记录，核查于 2026-10-22 至 10-24）。</li>
</ul>
<h2>包含什么（Pro 档官网口径）</h2>
<ul>
<li>扩展的 Agent 额度、前沿模型、MCP、云端 Agent、Tab 自动补全。</li>
<li>每月包含 $20 第三方模型用量额度，超出部分按量另计。</li>
<li>价格不含税，团队档按座位另计。</li>
</ul>
<h2>适合谁</h2>
<p>每天用 Cursor 的 Agent 写代码的人。轻度使用（只用 Tab 补全、偶尔问 Agent）的人，免费档一般够用；新用户按 Premium $30/月做预算，老用户按账号内续费价为准。</p>
<h2>官网入口</h2>
<ul>
<li>定价页：<a href="https://cursor.com/pricing">https://cursor.com/pricing</a></li>
</ul>
<p class="note">价格以官网为准。新老用户档位不同，下单前以结算页显示的档位与价格为准。</p>
""")

for name, html in pages.items():
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(html)
print("wrote A group:", len(pages))
for n in sorted(pages):
    print(n)

# ================= B组 index =================
pages["video-music/index.html"] = page(
    "影音会员官方价对照：爱奇艺、腾讯视频、优酷、芒果TV、B站、网易云",
    "爱奇艺黄金VIP、腾讯视频VIP、优酷VIP、芒果TV会员、哔哩哔哩大会员、网易云音乐黑胶VIP 的官网公开月价、年卡价与日均价换算对照。",
    "../../index.html", "权益价榜首页",
    """<h1>影音会员官方价对照</h1>
<p>下表只列各家官网公开的标准价（人民币），不是供货价、不是代充价。连续包月 / 包季 / 包年指开通自动续费的价格；月卡 / 季卡 / 年卡指一次买断、不自动续费的价格。日均价算法：年卡价 ÷ 365；连续包月价 ÷ 30。双 11 等大促活动价不在主表内，详情页另行注明。</p>
<h2>总览（核查日期 2026-11-17）</h2>
<table>
<tr><th>产品</th><th>连续包月</th><th>连续包季</th><th>连续包年</th><th>月卡（非连续）</th><th>年卡（非连续）</th></tr>
<tr><td><a href="iqiyi.html">爱奇艺黄金VIP</a></td><td>¥25/月</td><td>¥68/季</td><td>¥238/年</td><td>¥30</td><td>¥258</td></tr>
<tr><td><a href="tencent-video.html">腾讯视频VIP</a></td><td>¥25/月</td><td>¥68/季</td><td>¥238/年</td><td>¥30</td><td>¥258</td></tr>
<tr><td><a href="youku.html">优酷VIP</a></td><td>¥25/月</td><td>¥68/季</td><td>¥238/年</td><td>¥30</td><td>¥258</td></tr>
<tr><td><a href="mango.html">芒果TV会员</a></td><td>¥22/月</td><td>¥63/季</td><td>¥218/年</td><td>¥30</td><td>¥248</td></tr>
<tr><td><a href="bilibili.html">哔哩哔哩大会员</a></td><td>¥15/月</td><td>¥45/季</td><td>首年 ¥128，续费 ¥148/年（原价 ¥233）</td><td>¥25</td><td>¥233</td></tr>
<tr><td><a href="netease-cloud.html">网易云音乐黑胶VIP</a></td><td>¥15/月</td><td>¥45/季</td><td>¥158/年（续费价）</td><td>¥18</td><td>¥178</td></tr>
</table>
<p class="note">算法说明：日均价 = 年卡价 ÷ 365 天；连续包月日均价 = 月价 ÷ 30 天。芒果TV 季卡（非连续）本次核查未找到官网公开价，详情页写为“未核实”。各家首月 / 首年新人价为限时活动，不在上表内，详情页注明。</p>
<h2>分产品详情</h2>
<ul>
<li><a href="iqiyi.html">爱奇艺黄金VIP：连续包月 ¥25，连续包年 ¥238</a></li>
<li><a href="tencent-video.html">腾讯视频VIP：连续包月 ¥25，连续包年 ¥238</a></li>
<li><a href="youku.html">优酷VIP：连续包月 ¥25，连续包年 ¥238</a></li>
<li><a href="mango.html">芒果TV会员：连续包月 ¥22，连续包年 ¥218</a></li>
<li><a href="bilibili.html">哔哩哔哩大会员：连续包月 ¥15，连续包年首年 ¥128</a></li>
<li><a href="netease-cloud.html">网易云音乐黑胶VIP：连续包月 ¥15，连续包年 ¥158</a></li>
</ul>
<h2>口径说明</h2>
<ul>
<li>以上均为各家官网会员购买页与 App Store 官方订阅说明的公开价，核查日期 2026-11-17。活动价（如双 11 首年价）随窗口变化，以下单页实时价为准。</li>
<li>连续包年到期后一般按标注的续费价续扣，爱奇艺、腾讯视频、优酷的连续包年活动价到期后按 ¥238/年续，芒果TV 按 ¥218/年续；开通后如不需要续费，请自行关闭自动续费。</li>
<li>基础档一般不含电视端，电视端需另购高级档（白金 / SVIP / 全屏影视会员等），详情页已注明。</li>
<li>来源：各平台官网会员购买页与 App Store 官方订阅说明，核查日期 2026-11-17（通过公开检索核对官网口径）。</li>
</ul>
""", sisters=True)

# ================= B组详情 =================
pages["video-music/iqiyi.html"] = page(
    "爱奇艺黄金VIP官方价：连续包月 ¥25，连续包年 ¥238",
    "爱奇艺黄金VIP官网公开价：连续包月 ¥25/月，连续包季 ¥68，连续包年 ¥238/年，月卡 ¥30，年卡 ¥258。",
    "index.html", "影音会员官方价对照",
    """<h1>爱奇艺黄金VIP 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>连续包月：<b>¥25/月</b>；连续包季：<b>¥68/季</b>；连续包年：<b>¥238/年</b>。</li>
<li>一次买断：月卡 ¥30，季卡 ¥78，年卡 ¥258。</li>
<li>日均价换算：连续包年 ¥238 ÷ 365 ≈ ¥0.65/天；年卡 ¥258 ÷ 365 ≈ ¥0.71/天；连续包月 ¥25 ÷ 30 ≈ ¥0.83/天。</li>
<li>来源：爱奇艺官网会员购买页 https://www.iqiyi.com/vip/；App Store 爱奇艺 App 官方订阅说明（连续包月 ¥25、连续包季 ¥68、连续包年 ¥238）。</li>
<li>活动价说明：2026-10-29 官网实测，黄金VIP连续包年首年 ¥148（到期按 ¥238/年续）、首月 ¥12（次月起 ¥25/月续），均为双 11 窗口活动价，不在主表内，以下单页实时价为准。</li>
</ul>
<h2>包含权益（官网口径）</h2>
<ul>
<li>手机、平板、电脑三端使用，会员内容抢先看、帧绮映画 4K 画质、杜比音效、广告特权、下载特权。</li>
<li>黄金VIP 不支持电视端播放；电视端需白金VIP（连续包月 ¥35/月，连续包年 ¥348/年）或星钻VIP。</li>
</ul>
<h2>适合谁</h2>
<p>只在手机、平板、电脑上追剧的人。常在电视上看的人，应看白金VIP 或星钻VIP 的价格，而不是只看黄金VIP。</p>
<h2>官网入口</h2>
<ul>
<li>会员购买页：<a href="https://www.iqiyi.com/vip/">https://www.iqiyi.com/vip/</a></li>
</ul>
<p class="note">价格以官网为准。自动续费到期后按标注的续费价续扣，不需要续费请自行关闭自动续费。</p>
""")

pages["video-music/tencent-video.html"] = page(
    "腾讯视频VIP官方价：连续包月 ¥25，连续包年 ¥238",
    "腾讯视频VIP官网公开价：连续包月 ¥25/月，连续包季 ¥68，连续包年 ¥238/年，月卡 ¥30，年卡 ¥258。",
    "index.html", "影音会员官方价对照",
    """<h1>腾讯视频VIP 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>连续包月：<b>¥25/月</b>；连续包季：<b>¥68/季</b>；连续包年：<b>¥238/年</b>。</li>
<li>一次买断：月卡 ¥30，季卡 ¥78，年卡 ¥258。</li>
<li>日均价换算：连续包年 ¥238 ÷ 365 ≈ ¥0.65/天；年卡 ¥258 ÷ 365 ≈ ¥0.71/天；连续包月 ¥25 ÷ 30 ≈ ¥0.83/天。</li>
<li>来源：App Store 腾讯视频 App 官方订阅说明（连续包月 ¥25/月、连续包季 ¥68/季、连续包年 ¥238/年）；腾讯视频会员服务协议页 film.qq.com。单月卡、季卡、年卡价格为多家公开记录一致的官网口径。</li>
<li>活动价说明：2026-10 月双 11 窗口，腾讯视频VIP连续包年到手价曾低至 ¥138 左右（372 天），为限时活动价，不在主表内，以下单页实时价为准。</li>
</ul>
<h2>包含权益（官网口径）</h2>
<ul>
<li>会员内容、1080P 为主（部分 4K 需超级影视SVIP）、基础VIP仅支持 1 台设备同时在线。</li>
<li>VIP 不含电视端；电视端需超级影视SVIP（连续包月 ¥35/月，连续包年 ¥348/年），可在云视听极光 TV 使用。</li>
</ul>
<h2>适合谁</h2>
<p>只在手机、平板、电脑上看腾讯独播剧的人。需要在电视上看或多台设备同时看的人，应看超级影视SVIP 的价格。</p>
<h2>官网入口</h2>
<ul>
<li>官网：<a href="https://v.qq.com/">https://v.qq.com/</a></li>
<li>会员服务协议：<a href="https://film.qq.com/weixin/term.html">https://film.qq.com/weixin/term.html</a></li>
</ul>
<p class="note">价格以官网为准。自动续费到期后按标注的续费价续扣，不需要续费请自行关闭自动续费。</p>
""")

pages["video-music/youku.html"] = page(
    "优酷VIP官方价：连续包月 ¥25，连续包年 ¥238",
    "优酷VIP官网公开价：连续包月 ¥25/月，连续包季 ¥68，连续包年 ¥238/年，月卡 ¥30，年卡标价 ¥258。",
    "index.html", "影音会员官方价对照",
    """<h1>优酷VIP 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>连续包月：<b>¥25/月</b>；连续包季：<b>¥68/季</b>；连续包年：<b>¥238/年</b>。</li>
<li>一次买断：月卡 ¥30，年卡标价 ¥258。</li>
<li>日均价换算：连续包年 ¥238 ÷ 365 ≈ ¥0.65/天；年卡 ¥258 ÷ 365 ≈ ¥0.71/天；连续包月 ¥25 ÷ 30 ≈ ¥0.83/天。</li>
<li>来源：App Store 优酷 App 官方订阅说明（连续包月每月 ¥25、连续包年每年 ¥238）；优酷官网会员中心 vip.youku.com（2026-11-10 公开实测记录：月卡 ¥30、年卡 ¥128 为活动价、划线价 ¥258，连续包年 ¥118 为活动价、划线价 ¥238）。</li>
<li>活动价说明：连续包月首 3 个月 ¥9.9/月、连续包年 ¥118、年卡 ¥128 均为双 11 窗口活动价，到期后按标准价续费，不在主表内，以下单页实时价为准。</li>
</ul>
<h2>包含权益（官网口径）</h2>
<ul>
<li>会员内容，覆盖手机、平板、电脑。</li>
<li>VIP 不含电视端；电视端需 SVIP（酷喵），SVIP 连续包月 ¥35/月，月卡 ¥50，年卡标价 ¥488。</li>
</ul>
<h2>适合谁</h2>
<p>只在手机、平板、电脑上看优酷独播内容的人。需要在电视上看的人，应看 SVIP（酷喵）的价格。</p>
<h2>官网入口</h2>
<ul>
<li>会员中心：<a href="https://vip.youku.com/">https://vip.youku.com/</a></li>
</ul>
<p class="note">价格以官网为准。活动价到期后按标准价续费，下单前请在支付页再确认一次。</p>
""")

pages["video-music/mango.html"] = page(
    "芒果TV会员官方价：连续包月 ¥22，连续包年 ¥218",
    "芒果TV会员官网公开价：连续包月 ¥22/月，连续包季 ¥63，连续包年 ¥218/年，月卡 ¥30，年卡标价 ¥248。",
    "index.html", "影音会员官方价对照",
    """<h1>芒果TV会员 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>连续包月：<b>¥22/月</b>；连续包季：<b>¥63/季</b>；连续包年：<b>¥218/年</b>（到期仍按 ¥218/年续）。</li>
<li>一次买断：月卡 ¥30，年卡标价 ¥248。</li>
<li>季卡（非连续）：<b>未核实</b>（本次核查未找到官网公开价，不写数字）。</li>
<li>日均价换算：连续包年 ¥218 ÷ 365 ≈ ¥0.60/天；年卡 ¥248 ÷ 365 ≈ ¥0.68/天；连续包月 ¥22 ÷ 30 ≈ ¥0.73/天。</li>
<li>来源：App Store 芒果TV App 官方订阅说明（连续包月每月 ¥22、连续包季每季度 ¥63、连续包年每年 ¥218）；芒果TV官网会员购买页 https://www.mgtv.com/vip/（2026-10-29 公开实测记录一致）。</li>
<li>活动价说明：新用户连续包月前 3 个月 ¥9/月（第 4 个月起 ¥22/月续）、连续包季 ¥43（到期按 ¥63/季续）、年卡券后 ¥82（标价 ¥248），均为双 11 窗口活动价，不在主表内，以下单页实时价为准。</li>
</ul>
<h2>包含权益（官网口径）</h2>
<ul>
<li>手机、平板、电脑档会员内容。</li>
<li>不含电视端；电视端需全屏影视会员（SVIP），月卡 ¥60。</li>
<li>2025-03-25 起，新订阅会员的同时使用设备数从 2 台降到 1 台。</li>
</ul>
<h2>适合谁</h2>
<p>只在手机、平板、电脑上追芒果综艺、剧集的人。需要在电视上看的人，应看全屏影视会员的价格。</p>
<h2>官网入口</h2>
<ul>
<li>会员购买页：<a href="https://www.mgtv.com/vip/">https://www.mgtv.com/vip/</a></li>
</ul>
<p class="note">价格以官网为准。芒果TV 的连续包年到期后仍按 ¥218/年续，是本组里唯一在页面上写明续费价不涨的。</p>
""")

pages["video-music/bilibili.html"] = page(
    "哔哩哔哩大会员官方价：连续包月 ¥15，连续包年首年 ¥128",
    "哔哩哔哩大会员官网公开价：连续包月 ¥15/月，连续包季 ¥45，连续包年首年 ¥128、续费 ¥148/年，月卡 ¥25，年卡 ¥233。",
    "index.html", "影音会员官方价对照",
    """<h1>哔哩哔哩大会员 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>连续包月：<b>¥15/月</b>；连续包季：<b>¥45/季</b>；连续包年：首年 <b>¥128</b>，续费 <b>¥148/年</b>（原价 ¥233/年）。</li>
<li>一次买断：月卡 ¥25，季卡 ¥68，年卡 ¥233。</li>
<li>日均价换算：连续包年续费 ¥148 ÷ 365 ≈ ¥0.41/天；首年 ¥128 ÷ 365 ≈ ¥0.35/天；年卡 ¥233 ÷ 365 ≈ ¥0.64/天；连续包月 ¥15 ÷ 30 = ¥0.50/天。</li>
<li>来源：App Store 哔哩哔哩 App 官方订阅说明（连续包月大会员 ¥15/月、连续包季 ¥45）；多家公开记录一致的官网口径（连续包年首年 ¥128、续费 ¥148，原价 ¥233；月卡 ¥25、季卡 ¥68、年卡 ¥233）。</li>
<li>口径说明：个别渠道称“首月 ¥15、次月起 ¥25/月”，与当前 ¥15/月续费的口径有出入，以官网结算页显示为准。活动价说明：618 等大促期间年卡曾低至 ¥108 左右，为限时活动价，不在主表内。</li>
</ul>
<h2>包含权益（官网口径）</h2>
<ul>
<li>1080P 高码率画质、部分番剧影视内容、年度会员 B 币返利、红色昵称等权益。</li>
<li>不含 TV 端；TV 端需超级大会员（连续包月 ¥30/月，连续包年首年 ¥178/年，原价 ¥388/年）。</li>
</ul>
<h2>适合谁</h2>
<p>常看番剧、影视与 PUGV 中长视频，且需要高码率画质的人。只看免费区、不追番的人，不需要开大会员。</p>
<h2>官网入口</h2>
<ul>
<li>官网：<a href="https://www.bilibili.com/">https://www.bilibili.com/</a>（会员页需登录后查看）</li>
<li>会员服务协议：<a href="https://www.bilibili.com/blackboard/big-protocol.html#monthly">https://www.bilibili.com/blackboard/big-protocol.html#monthly</a></li>
</ul>
<p class="note">价格以官网为准。自动续费到期后按标注的续费价续扣，不需要续费请自行关闭自动续费。</p>
""")

pages["video-music/netease-cloud.html"] = page(
    "网易云音乐黑胶VIP官方价：连续包月 ¥15，连续包年 ¥158",
    "网易云音乐黑胶VIP官网公开价：连续包月 ¥15/月，连续包季 ¥45，连续包年 ¥158/年（续费价），月卡 ¥18，年卡 ¥178。",
    "index.html", "影音会员官方价对照",
    """<h1>网易云音乐黑胶VIP 官方价</h1>
<h2>官方价（核查日期 2026-11-17）</h2>
<ul>
<li>连续包月：<b>¥15/月</b>；连续包季：<b>¥45/季</b>；连续包年：<b>¥158/年</b>（续费价）。</li>
<li>一次买断：月卡 ¥18，年卡 ¥178。</li>
<li>季卡（非连续）：<b>未核实</b>（本次核查未找到官网公开价，不写数字）。</li>
<li>日均价换算：连续包年 ¥158 ÷ 365 ≈ ¥0.43/天；年卡 ¥178 ÷ 365 ≈ ¥0.49/天；连续包月 ¥15 ÷ 30 = ¥0.50/天。</li>
<li>来源：App Store 网易云音乐 App 官方订阅说明（2026-09-28 抓取：连续包月黑胶VIP ¥15/月、黑胶SVIP ¥28/月；黑胶VIP 包季 ¥45、包年 ¥158）；网易云音乐官网会员收银台 https://music.163.com/g/vip-h5-cashier。</li>
<li>活动价说明：连续包年首年新客价 ¥68、连续包月首月 ¥4.8 左右、双 11 官方店年卡 ¥98 加赠 88 天，均为限时活动价，不在主表内，以下单页实时价为准。</li>
</ul>
<h2>包含权益（官网口径）</h2>
<ul>
<li>免费畅听会员曲库、无损音质、免费下载、多端通用、会员音效等 30 多项基础权益。</li>
<li>黑胶SVIP（连续包月 ¥28/月）在黑胶VIP 之上另加超清母带、沉浸环绕声、有声书等权益；SVIP 月卡 ¥40、年卡 ¥348（原价 ¥480）。</li>
</ul>
<h2>适合谁</h2>
<p>每天在网易云音乐听歌、需要无损音质与下载的人。只听免费曲库的人，不需要开黑胶VIP。</p>
<h2>官网入口</h2>
<ul>
<li>会员收银台：<a href="https://music.163.com/g/vip-h5-cashier">https://music.163.com/g/vip-h5-cashier</a></li>
<li>官网：<a href="https://music.163.com/">https://music.163.com/</a></li>
</ul>
<p class="note">价格以官网为准。自动续费到期后按标注的续费价续扣，不需要续费请自行关闭自动续费。</p>
""")

for name, html in pages.items():
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(html)
print("wrote total:", len(pages))
for n in sorted(pages):
    print(n)
