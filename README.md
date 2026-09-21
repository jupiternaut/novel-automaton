# 小说创作自动机 · 统一资料库

把这次小说创作需要的来源、两套设计与工作稿集中保存。当前是创作与架构资料包，尚未实现完整小说自动机。

## 从这里开始

| 内容 | 入口 |
| --- | --- |
| Gemini 大纲与原始附件 | [世界观整理](sources/gemini/世界观整理.md) · [PDF与来源说明](sources/gemini/README.md) |
| 《归乡疫期》原本 | [用户原始稿](sources/gui-xiang-yi-qi/原始稿.txt) |
| Claude 合作扩写 | [约3.47万汉字重建稿](sources/gui-xiang-yi-qi/Claude合作稿-重建.md) · [来源说明](sources/gui-xiang-yi-qi/README.md) |
| 架构一：人物属性历史 | [设计原文](architecture/01-character-history/设计原文.md) |
| 架构二：世界状态与事件因果 | [设计原文](architecture/02-world-events/设计原文.md) |
| 两套设计的连接 | [架构总览](architecture/README.md) |
| PLM、LightRAG、酒馆参考 | [参考说明与来源快照](references/README.md) |
| 本次新小说文风与开篇 | [文风分析](workbench/STYLE_AND_STATE.md) · [v0.2开篇](workbench/drafts/01-临时通知-v0.2.md) |
| 事件记录小样 | [九个事件](workbench/events/opening-v0.2.json) |
| 题辞 | [英文原文](EPIGRAPH.md) |
| 打包与校验 | [打包说明](PACKAGING.md) · [文件清单](MANIFEST.json) |

## 使用边界

用户明确设定、历史合作稿、新试写、设计提案、第三方参考分别存放。当前v0.2是待采纳试稿，旧v0.1保留为历史。两套架构来自用户提供的设计文本，未包装为已经实现的功能。

既有小说保存来源证据，不凭空补全未揭晓真相。新小说先由事件改变状态，再分别读取人物历史、世界状态、认知与读者披露；未采纳续写不覆盖原作。

本仓库默认私有。原始资料的版权与第三方许可证见[权利与来源](RIGHTS.md)。

## 下载

GitHub仓库页面选择 Code → Download ZIP，即可取得统一资料包。原始PDF、纯文本小说和Markdown设计均在仓库内，无需访问内网即可阅读主体材料。
