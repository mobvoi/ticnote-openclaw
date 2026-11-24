# 浏览与搜索

TicNote 内容模型：知识库 = 目录树，节点是录音、上传文件、提取的视频等，每个节点有
`recordId`（树节点 ID）和 `fileId`（业务文件 ID）。后续所有操作都从这两个 ID 出发。

## 列出与过滤

```bash
tnote list -o json                          # 全部（默认前 50 条）
tnote list --name "会议" -o json            # 按名称过滤
tnote list --type file -o json              # 只要文件
tnote list --type directory -o json         # 只要目录
tnote list --file-type recording_file -o json  # 按业务类型（如 recording_file、pdf）
```

`--name` 是子串匹配，不是内容搜索；TicNote 当前没有内容级搜索工具，
按内容找材料时先用名称关键词尝试，找不到就如实说明并建议换关键词。

## 按名称搜索

```bash
tnote search "关键词" -o json               # 等价于 list --name，返回排序结果
tnote search "关键词" --type file -o json
```

## 语义要点

- 展示条目时优先给 `name`、`recordId`、状态；用户后续说"那个录音"时用刚返回的 ID，不重新猜。
- 列表结果是分页/截断的（默认 50 条）；没有更多标记时如实说明"默认前 50 条"，
  不声称已经列全。
- 空结果 ≠ 用户没有内容；换关键词、换 `--file-type` 再试，仍为空才如实回复。
- ID 按字符串原样传递；`recordId` 与 `fileId` 不互换：树操作（目录、分享位置）用
  recordId，转写/总结/翻译用 fileId。

---
