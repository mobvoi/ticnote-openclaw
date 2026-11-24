# 详情、转写、总结与翻译

## 读取详情

```bash
tnote detail <recordId> -o json                # 状态、转写、总结
tnote detail <recordId> --field transcribeJson -o json   # 只取某字段
tnote detail <recordId> --poll -o json         # 轮询等待转写完成（5s 间隔，10 分钟超时）
```

- `recordId` 来自 `tnote list`，按字符串原样传递。
- 用户要"看原文/转写"时读取转写字段本身，不要用总结冒充原文；
  反之用户要"总结"时给总结，不要贴全文。

## 提交转写（异步）

```bash
tnote transcribe <fileId> -o json
tnote transcribe <fileId> --language zh -o json     # 指定语言（默认自动检测）
```

提交成功只代表任务已受理。之后必须：

```bash
tnote detail <recordId> --poll -o json
```

轮询到转写完成才算完成；超时则如实告知"仍在处理"，不伪造结果。

## 生成总结（异步）

```bash
tnote summary <fileId> -o json                       # 自动探测文件类型
tnote summary <fileId> --audio -o json               # 按音频处理（reSummary）
tnote summary <fileId> --doc -o json                 # 按文档处理（localFileSummary）
tnote summary <fileId> --record-id <recordId> -o json  # 探测失败时补充 recordId
tnote summary <fileId> --lang zh --template <模板> -o json
tnote summary <fileId> --customize "重点提取待办" -o json
```

自动探测失败时优先用 `--record-id` 提供 recordId；仍失败或用户明确知道类型时用
`--audio` / `--doc` 跳过探测。提交后同样用 `tnote detail --poll` 等待结果。

## 翻译（异步，可能覆盖已有结果）

```bash
tnote translate <fileId> --lang en -o json
```

- 目标语言：`zh / zh-Hant / en / ja / ko / fr / de / es / it / pt / ru / yue`。
- 翻译的是**最新转写**，且可能更新已有翻译结果——执行前告知用户这一点。
- 提交后轮询 detail 到终态，返回最终译文。

## 语义要点

- 三个任务全部异步：闭环是"提交 → 拿 ID → detail --poll → 终态"，
  任何一步没到终态都不能回复"已完成"。
- 失败时读取返回的 `error` 字段说明真实原因与下一步，不重试猜测。
- 修改类操作（总结覆盖、翻译覆盖）前先向用户说明并取得确认。

---
