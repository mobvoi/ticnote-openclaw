# TicNote OpenClaw Skill

[English](README.en.md)

TicNote OpenClaw Skill 让 AI 通过官方 `tnote` CLI 连接 TicNote，完成登录、诊断、浏览、搜索、转写、总结、翻译、分享和知识库整理。

### 安装

把本目录中的 `SKILL.md` 和 `references/` 一起安装到支持 Agent Skill 的 AI 平台。安装前请确保本机已安装官方 CLI：

```bash
npm install -g ticnote-cli
```

安装完成后，首次使用时运行：

```bash
tnote setup
tnote doctor -o json
```

AI 也可以通过自然语言引导完成授权。登录会打开浏览器，凭证保存在本机 `~/.config/ticnote/`，不会要求用户在聊天中粘贴密码、Cookie 或 Authorization。

### 文件结构

```text
SKILL.md              # 意图路由、执行闭环与安全规则
references/
  auth.md             # 登录、诊断、区域与升级
  list.md             # 浏览与按名称搜索
  note.md             # 详情、转写、总结与翻译
  share.md            # 分享链接与公开风险确认
  kb.md               # 注册公网 URL 与新建目录
```

> `SKILL.md` 与 `references/*.md` 面向 AI 读取，仅保留中文正文；`description` 字段包含中英文触发关键词。人类文档（README）保持中英双语。

### 设计原则

- Skill 只负责意图理解和命令路由，真实操作全部交给 `tnote` CLI。
- 领域参考文档按需读取，减少上下文并避免参数猜测。
- 转写、总结和翻译等异步任务必须轮询到最终状态。
- 所有 ID 按字符串传递，避免大整数精度丢失。
- 分享、翻译覆盖和其他写操作遵循确认规则。
- 失败时保留真实错误信息，不伪造成功。

### 支持的主要操作

```text
tnote auth login       浏览器 OAuth 登录
tnote doctor           连接与环境诊断
tnote list             浏览知识库
tnote search           按文件名搜索
tnote detail           查看详情与处理结果
tnote transcribe       提交转写任务
tnote summary          生成总结
tnote translate        翻译最新转写
tnote share            创建分享链接
tnote register         注册公网 URL
tnote mkdir            新建目录
```

[English](README.en.md)
