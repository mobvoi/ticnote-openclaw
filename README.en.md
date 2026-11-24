# TicNote OpenClaw Skill

[中文](README.md)

[![Version](https://img.shields.io/badge/version-0.3.0--beta.4-blue.svg)](VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Let AI connect to TicNote through the official `tnote` CLI, so you can browse, find, and process your own knowledge-base content using natural language.

---

## ✨ Core capabilities

| Capability | Description |
| --- | --- |
| **🔐 Browser authorization** | Guides TicNote login, connection diagnostics, and initial read-only verification |
| **📚 Browse knowledge bases** | View directories, files, and recent content with real titles, IDs, and processing status |
| **🔍 Search by name** | Find recordings, meetings, and other content by filename |
| **🎤 Transcribe recordings** | Submit transcription jobs and wait for the final result |
| **📝 Generate summaries** | Generate summaries for supported content and verify the final state |
| **🌐 Translate content** | Translate the latest transcription and warn before overwriting an existing result |
| **🔗 Create share links** | Generate accessible links and confirm the public-sharing risk first |
| **🗂️ Organize knowledge bases** | Register public URLs and create directories, returning the actual result |

---

## 📦 Installation

### Option 1: Ask an AI to install it directly (recommended)

Send the following message to an AI platform that supports Agent Skills:

> Install the TicNote Skill from https://github.com/mobvoi/ticnote-openclaw and guide me through authorization.

### Option 2: Download the Skill package

Open the [TicNote Skill releases page](https://github.com/mobvoi/ticnote-openclaw/releases/latest), download the latest ZIP,
drag it into the chat window of an AI platform that supports Agent Skills, and say:

> Install this TicNote Skill and guide me through authorization.

The Skill requires the official TicNote command-line tool, which the AI platform installs through its installation confirmation flow. The Skill itself does not run download scripts or overwrite files on its own.

---

## 🔑 First-time authorization

After the Skill is installed, the AI checks the TicNote CLI, guides you through browser-based authorization, and verifies that the current account can be read successfully.

You only need to confirm in the browser. Do not paste passwords, cookies, API keys, or Authorization headers into chat. After authorization, you can browse, search, and process TicNote content using natural language.

---

## 💡 Usage examples

Describe your goal in natural language:

```text
Log in to TicNote and check the connection

List my recent recordings and meetings

Search for files whose names contain “product review”

Read the full transcript of this recording

Transcribe this recording and tell me the result when it is finished

Summarize this meeting

Translate the latest transcription into English

Create a share link for this content

Register this public URL in the knowledge base

Create a “Meeting Records” directory
```

If a reference such as “this recording” or “the last meeting” cannot be uniquely identified, the AI reads the real list and asks you to choose instead of guessing an ID.

---

## 🧭 Main commands

The Skill uses the official CLI for real operations:

```text
tnote setup             Initialize and guide authorization
tnote auth login        Browser-based OAuth login
tnote doctor            Connection and environment diagnostics
tnote list              Browse the knowledge base
tnote search            Search by filename
tnote detail            Read details and processing results
tnote transcribe       Submit a transcription task
tnote summary           Generate a summary
tnote translate         Translate the latest transcription
tnote share            Create a share link
tnote register         Register a public URL
tnote mkdir             Create a directory
```

Machine calls use JSON output consistently. Asynchronous transcription, summary, and translation jobs must be waited on until their final state; “submitted” must not be reported as “completed.”

---

## 🗂️ File structure

```text
SKILL.md                  # Intent routing, execution loop, and safety rules
references/
  auth.md                 # Login, diagnostics, regions, and upgrades
  list.md                 # Browsing and filename search
  note.md                 # Details, transcription, summaries, and translation
  share.md                # Share links and public-sharing confirmation
  kb.md                   # Public URL registration and directory creation
scripts/
  build_skill_package.py  # Build the Skill release package
VERSION                   # Current version
```

`SKILL.md` and `references/*.md` are intended for AI consumption; this README is intended for human users.

---

## 🔐 Security boundaries

- All real operations are executed by the official `tnote` CLI; the Skill never fabricates results.
- IDs are always passed as strings without numeric conversion.
- Login credentials are never placed in command arguments, chat messages, or logs.
- Sharing may make content public; creating a share link requires confirmation first.
- Translation may overwrite an existing result; the user must be informed beforehand.
- Directory creation and public URL registration return the actual operation result.
- Failures preserve the real error and explain whether retrying is possible and what to do next.
- If the CLI is missing, only the official `ticnote-cli` installation declaration is used; no other installation scripts are run.

---

## 🔄 Updates

When the user explicitly requests a TicNote update, the AI runs the update flow and checks the connection. CLI dependencies are managed by the AI platform according to the Skill's installation declaration; users do not need to run CLI installation commands manually.

The Skill itself is managed by the AI platform and is not overwritten by the CLI update flow.

---

## 📄 Related links

- [TicNote CLI on npm](https://www.npmjs.com/package/ticnote-cli)
- [TicNote OpenClaw Skill](https://github.com/mobvoi/ticnote-openclaw)
- [中文 README](README.md)

## License

MIT
