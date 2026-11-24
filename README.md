# TicNote OpenClaw Skill

[![Version](https://img.shields.io/badge/version-0.3.0--beta.4-blue.svg)](VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[English](README.en.md)

让 AI 通过官方 `tnote` CLI 连接 TicNote，帮助你浏览、查找和处理自己的知识库内容。
你只需要用自然语言表达目标，Skill 负责理解意图、加载对应参考文档，并交给官方 CLI 执行真实操作。

---

## ✨ 核心能力

| 能力 | 说明 |
| --- | --- |
| **🔐 浏览器授权** | 引导完成 TicNote 登录、连接诊断和首次无写入验收 |
| **📚 浏览知识库** | 查看目录、文件和最近内容，返回真实标题、ID 与处理状态 |
| **🔍 按名称搜索** | 根据文件名查找知识库中的录音、会议和其他内容 |
| **🎤 转写录音** | 提交转写任务并等待异步任务完成，返回最终结果 |
| **📝 生成总结** | 对支持的内容生成总结，并确认任务最终状态 |
| **🌐 翻译内容** | 翻译最新转写结果；覆盖已有翻译前会先提示风险 |
| **🔗 创建分享链接** | 生成可访问链接；公开分享前会明确确认公开风险 |
| **🗂️ 知识库整理** | 注册公网 URL、新建目录，返回真实条目或目录信息 |

---

## 📦 安装

### 方式一：让 AI 直接安装（推荐）

将下面这句话发送给支持 Agent Skill 的 AI：

> 请从 https://github.com/mobvoi/ticnote-openclaw 安装 TicNote Skill，并引导我完成授权。

### 方式二：下载 Skill 安装包

打开 [TicNote Skill 发布页](https://github.com/mobvoi/ticnote-openclaw/releases/latest)，下载最新版 ZIP，
将 ZIP 拖进支持 Agent Skill 的 AI 聊天框，然后说明：

> 请安装这个 TicNote Skill，并引导我完成授权。

Skill 需要官方 TicNote 命令行工具，由 AI 平台按安装确认流程装好；Skill 本身不会执行下载脚本或自行覆盖文件。

---

## 🔑 首次授权

安装 Skill 后，AI 会自动检查 TicNote CLI、引导你在浏览器中完成授权，并验证当前账号是否可以正常读取内容。

授权时只需在浏览器中确认，不需要在聊天中粘贴密码、Cookie、API Key 或 Authorization。授权完成后，就可以直接用自然语言浏览、搜索和处理 TicNote 中的内容。

---

## 💡 使用示例

直接用自然语言描述目标即可：

```text
登录 TicNote 并检查连接状态

列出我最近的录音和会议

搜索名称里包含“产品评审”的文件

读取这条录音的完整转写

把这个录音转写，完成后告诉我结果

总结这条会议记录

把最新转写翻译成英文

为这条内容创建分享链接

把这个公网网址注册到知识库

新建一个“会议记录”目录
```

对于“这个录音”“上次会议”等无法唯一确定的指代，AI 会先读取真实列表并要求选择，不会猜测 ID。

---

## 🧭 支持的主要命令

Skill 通过官方 CLI 执行真实操作：

```text
tnote setup             初始化与授权引导
tnote auth login        浏览器 OAuth 登录
tnote doctor            连接与环境诊断
tnote list              浏览知识库
tnote search            按文件名搜索
tnote detail            查看详情与处理结果
tnote transcribe        提交转写任务
tnote summary           生成总结
tnote translate         翻译最新转写
tnote share             创建分享链接
tnote register          注册公网 URL
tnote mkdir             新建目录
```

机器调用统一使用 JSON 输出；转写、总结和翻译等异步任务必须等待到最终状态，不能把“已提交”说成“已完成”。

---

## 🗂️ 文件结构

```text
SKILL.md              # 意图路由、执行闭环与安全规则
references/
  auth.md             # 登录、诊断、区域与升级
  list.md             # 浏览与按名称搜索
  note.md             # 详情、转写、总结与翻译
  share.md            # 分享链接与公开风险确认
  kb.md               # 注册公网 URL 与新建目录
scripts/
  build_skill_package.py  # 构建 Skill 发布包
VERSION               # 当前版本
```

`SKILL.md` 和 `references/*.md` 面向 AI 读取，README 面向人类使用者。

---

## 🔐 安全边界

- 所有真实操作都由官方 `tnote` CLI 执行，Skill 不伪造结果；
- ID 始终按字符串传递，不做数值转换；
- 登录凭证不写入命令参数、聊天内容或日志；
- 分享可能使内容公开，创建分享链接前必须确认；
- 翻译可能覆盖已有结果，覆盖前必须告知用户；
- 新建目录、注册公网 URL 等写操作会明确返回实际结果；
- 失败时保留真实错误信息，并说明是否可重试及下一步；
- CLI 缺失时只使用官方 `ticnote-cli` 安装声明，不运行其他安装脚本。

---

## 🔄 更新

用户明确要求更新 TicNote 时，AI 才会执行更新流程并检查连接状态。CLI 依赖由支持 Agent Skill 的平台按照 Skill 安装声明管理，用户不需要手动执行 CLI 安装命令。

Skill 本体由 AI 平台管理，不会通过 CLI 更新流程覆盖自身文件。

---

## 📄 相关链接

- [TicNote CLI（npm）](https://www.npmjs.com/package/ticnote-cli)
- [TicNote OpenClaw Skill](https://github.com/mobvoi/ticnote-openclaw)
- [English README](README.en.md)

## License

MIT
