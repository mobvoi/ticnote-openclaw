# 注册公网 URL 与目录管理

## 注册公网文件 URL

```bash
tnote register <url> -o json                     # 单个公网文件
tnote register <url> --parent-id <parentId> -o json    # 注册到指定目录
tnote register <url> --file-name "会议录音.mp3" -o json # 指定名称
tnote register <url> --file-type mp3 -o json     # 指定类型（默认从文件名推断）
tnote register --files-json '<JSON 数组>' -o json  # 批量
```

- **只支持公网 URL**：URL 必须可被 TicNote 服务端直接访问。
  用户要求上传本地文件时如实说明当前不支持本地二进制上传，
  可建议先把文件放到可公开访问的位置再注册 URL，不冒充上传成功。
- 批量 `--files-json` 的文件项字段：`fileName`、`fileType`、`fileUrl`，可选
  `recordTime`、`sn`。
- 注册是登记，不代表内容已解析；注册后注册条目会走后续转写/解析流程，
  处理状态用 `tnote detail` 查询。

## 新建目录

```bash
tnote mkdir <目录名> -o json
tnote mkdir <目录名> --parent <parentId> -o json   # 默认根目录
```

- `parentId` 是父目录的 recordId（来自 `tnote list --type directory`）。
- 重名目录不自动覆盖也不自动改名；目标目录已存在时如实告知用户。

## 语义要点

- 建目录、注册文件属于写操作，执行前先说明动作与目标位置，取得用户确认。
- 写操作完成后重新 `tnote list` 复读，确认条目真实出现在预期位置，
  再向用户报告成功。
- ID 全部按字符串原样传递。

---
