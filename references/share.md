# 分享

创建分享后内容将可能公开。执行前必须向用户说明并取得确认，不得静默执行。

## 创建分享

```bash
tnote share <fileId> -o json                    # 默认分享音频
tnote share <fileId> --type localFile -o json   # 分享文档/文件
tnote share <fileId> --type translation -o json # 分享翻译
```

- `fileId` 来自 `tnote list`，按字符串原样传递。
- 分享类型三选一：`audio | localFile | translation`；按用户实际要分享的内容选择，
  不确定时先确认。
- `-y` / `--yes` 会跳过确认；仅在用户已明确知晓公开风险并主动要求跳过确认时使用。

## 结果呈现

- 成功：回复真实分享链接；链接只用返回值，不自行拼接域名。
- 失败：读取 `error` 字段说明真实原因；取消、权限不足不能回复成功。
- 分享完成后如需核对，重新读取该文件状态确认分享生效。

## 群聊与共享会话

群聊或共享会话中用户要求分享时，先确认分享范围与公开风险再执行；
不在未确认的情况下批量分享多条内容。

---
