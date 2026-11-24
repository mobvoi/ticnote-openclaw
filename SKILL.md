---
name: ticnote
version: 0.3.0-beta.4
description: |
  通过官方 tnote CLI 连接 TicNote，完成浏览器授权、连接诊断，以及浏览、搜索、
  转写、总结、翻译、分享知识库内容。用户要找录音或会议、读取转写或总结原文、
  生成摘要或翻译、创建分享链接、注册公网文件或新建目录，或明确要求登录、诊断
  TicNote 时使用；不会自行安装或更新 Skill。
  Connect to TicNote for browser authorization, diagnostics, browsing, search, transcription,
  summaries, translation, sharing, and knowledge-base organization. Use when users ask about
  recordings, meetings, transcripts, summaries, public URL registration, directories, login,
  or diagnostics; do not install or update the Skill without an explicit request.
metadata:
  openclaw:
    emoji: "🎙"
    requires:
      bins: ["tnote"]
    install:
      - id: "node-ticnote"
        kind: "node"
        package: "ticnote-cli"
        bins: ["tnote"]
        label: "Install official TicNote CLI (npm)"
---

# TicNote

让用户在当前 AI 中直接连接、诊断 TicNote，并浏览、查找和处理自己的知识库内容。
本 Skill 理解用户意图、加载对应领域参考，并交给官方 `tnote` CLI 执行真实操作。

## 能力与外部影响

- 本 Skill 按用户请求执行 `tnote` 命令，通过 TicNote API 读取或修改当前已授权账号的数据。
- 登录会打开浏览器授权页，授权信息由 CLI 保存在其本机配置目录；Skill 不读取、展示或转发完整凭证。
- 翻译会更新已有结果、分享会让内容可能公开、注册与建目录会修改知识库结构——均遵守下方确认规则。
- 只有用户明确要求时才执行升级（`npm install -g ticnote-cli`）；不运行其他安装脚本、不修改其他 Skill 文件。
- `tnote` 缺失时使用平台根据 frontmatter `install` 声明提供的官方安装流程；平台要求确认时只请求这一次确认。

## 能力概览

| 用户想做什么 | 典型说法 | 完成后应返回什么 |
| --- | --- | --- |
| 找内容 | "我有哪些录音" "最近开了什么会" | 真实标题、recordId/fileId、状态 |
| 读内容 | "看下这个录音的转写" "上次总结说了什么" | 转写或总结原文，不用摘要冒充 |
| 处理内容 | "转写这个文件" "总结一下" "翻译成英文" | 异步任务等待到终态后的最终结果 |
| 分享 | "把这条转写分享出去" | 真实分享链接（先确认公开风险） |
| 收集材料 | "把这个网址存进知识库" | 注册后的文件条目（仅限公网 URL） |
| 整理 | "新建一个会议目录" | 真实目录与位置 |
| 连接与排障 | "登录 TicNote" "为什么连不上" | CLI、授权与 API 的实际检查结果 |

不要要求用户记命令。用户用自然语言表达目标即可。

## 首次连接

1. 执行 `command -v tnote`。如果 CLI 不存在，调用平台根据 frontmatter `install`
   声明提供的 `ticnote-cli` 安装流程；不要让用户选择安装方式。
2. 执行 `tnote setup`，完成授权引导与自检。
3. 尚未授权时运行 `tnote auth login` 并让用户只在浏览器确认；
   不得索要密码、Cookie 或 Authorization。
4. 执行 `tnote doctor -o json`。命令退出码为 0 且 `ready=true` 才能说已经连接；
   `status=degraded` 时继续说明并处理非阻断警告。
5. 先运行 `tnote list -o json` 做无写入验收，向用户展示真实条目。

## 每次任务的执行闭环

1. **理解目标**：识别用户要处理的对象、动作和目标位置；"这个录音"等指代不明确时先澄清。
2. **加载领域参考**：只读取本次任务涉及的 `references/*.md`，不要凭印象猜命令、参数或返回字段。
3. **确认真实对象**：先读取文件或目录的真实 ID（recordId / fileId）。名称重名时让用户选择。
4. **执行官方 CLI**：机器调用统一加 `-o json`；参数不确定时读取对应命令 `--help`。
5. **判断结果**：同时检查退出码、`ok` 与领域结果字段；异步任务必须轮询到终态，
   不能把"已提交"说成"已完成"。
6. **必要时复读**：翻译、分享等操作完成后按领域参考重新读取结果，确认最终状态。
7. **回复用户**：先给结论，再给标题、ID 或必要摘要；失败时说明原因与下一步。

## 路由

匹配用户意图后，必须读取并遵循对应领域参考：

- 登录、连接、诊断：读 [`references/auth.md`](references/auth.md)
- 浏览知识库、按名称找文件：读 [`references/list.md`](references/list.md)
- 读取详情、转写、总结、翻译：读 [`references/note.md`](references/note.md)
- 创建分享链接：读 [`references/share.md`](references/share.md)
- 注册公网 URL、新建目录：读 [`references/kb.md`](references/kb.md)

一个任务涉及多个领域时，按实际步骤依次读取对应参考。
例如"找到上周的会议录音并翻译成英文"先读 list 再读 note。

## 统一规则

- 所有真实操作由官方 `tnote` CLI 完成；机器调用统一加 `-o json`。
- ID 始终按字符串原样传递，不做数值转换。
- 退出码非 0 表示命令未完成；成功读取 `ok=true` 与领域参考指定的 `data` 字段，
  失败读取 `error` 字段，不能根据自然语言猜成功。
- 转写、总结、翻译是异步任务：提交后用 `tnote detail <recordId> --poll` 等待终态；
  翻译可能覆盖已有结果，执行前告知用户。
- 分享会让内容可能公开；删除类、公开类操作必须先确认。
- 失败时说明真实原因、是否可重试和下一步；不能伪造成功。
- 凭证不写入命令参数、聊天或日志。

## 用户要求更新

用户说"更新 TicNote"即构成完整更新授权：

1. 执行 `npm install -g ticnote-cli` 升级 CLI。
2. 执行 `tnote doctor -o json` 验证连接与工具集。
3. Skill 本体由平台管理，本 Skill 不覆盖自身文件。

---
