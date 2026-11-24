# 登录、连接与诊断

## 检查与登录

```bash
command -v tnote          # CLI 是否存在
tnote auth login          # 浏览器 OAuth 登录（用户只需在浏览器确认）
tnote auth status         # 查看当前登录状态
tnote auth logout         # 清除本地凭证
```

- 登录打开浏览器授权页，凭证保存在 `~/.config/ticnote/`（600 权限）。
- 不得索要密码、Cookie 或 Authorization；代理问题可建议 `tnote auth login --manual`。

## 诊断

```bash
tnote doctor -o json
```

读取返回结构：

- `ready=true, status=ready` → 完整可用
- `ready=true, status=degraded` → 核心可用，把 `issues` 里的非阻断问题告知用户
- `ready=false` → 按 `issues[].code` 与 `next_actions` 修复：

| 问题码 | 处理 |
| --- | --- |
| `AUTH_NOT_LOGGED_IN` / `MCP_UNAUTHORIZED` | 运行 `tnote auth login` |
| `AUTH_TOKEN_EXPIRED_NO_REFRESH` | 运行 `tnote auth login` 重新授权 |
| `MCP_CONNECT_FAILED` | 检查网络；区域说明见下 |

## 区域

- `cn`（国内）/ `global`（海外）。CLI 默认 `global`；用户在国内时可建议
  `tnote --region cn ...` 或 `export TICNOTE_REGION=cn`。
- 优先级：`--region` 参数 > `TICNOTE_REGION` 环境变量 > 配置文件 > 默认 global。
- 连接失败时先确认区域是否匹配用户所在地，再怀疑网络。

## 升级

用户明确要求时：

```bash
npm install -g ticnote-cli
tnote doctor -o json      # 升级后验证
```

## 能力核对

```bash
tnote capabilities -o json
```

以返回的 tools/list 为准判断可用工具，不凭版本号假定能力存在。

---
