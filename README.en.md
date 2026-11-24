# TicNote OpenClaw Skill

[中文](README.md)


TicNote OpenClaw Skill lets AI agents connect to TicNote through the official `tnote` CLI for login, diagnostics, browsing, search, transcription, summaries, translation, sharing, and knowledge-base organization.

### Installation

Install `SKILL.md` together with the `references/` directory into an AI platform that supports Agent Skills. Make sure the official CLI is installed first:

```bash
npm install -g ticnote-cli
```

After installation, run the initial setup and diagnostics:

```bash
tnote setup
tnote doctor -o json
```

The AI agent can guide the user through authorization in a browser. Credentials are stored locally under `~/.config/ticnote/`. The Skill never asks users to paste passwords, cookies, or Authorization headers into chat.

### File structure

```text
SKILL.md              # Intent routing, execution loop, and safety rules
references/
  auth.md             # Login, diagnostics, regions, and upgrades
  list.md             # Browsing and filename search
  note.md             # Details, transcription, summaries, and translation
  share.md            # Share links and public-sharing confirmation
  kb.md               # Public URL registration and directory creation
```

> `SKILL.md` and `references/*.md` are intended for AI consumption and are maintained in Chinese only; their `description` fields include Chinese and English trigger keywords. Human-facing README documentation is bilingual.

## Design principles

- The Skill handles intent understanding and command routing; all real operations are executed by the `tnote` CLI.
- Domain references are loaded on demand to reduce context and avoid guessing parameters.
- Asynchronous transcription, summary, and translation tasks must be polled until a final state.
- All IDs are passed as strings to prevent large-integer precision loss.
- Sharing, overwriting translations, and other write operations follow confirmation rules.
- Failures must preserve the real error information; the agent must never claim success without verification.

### Main operations

```text
tnote auth login       Browser-based OAuth login
tnote doctor           Connection and environment diagnostics
tnote list             Browse the knowledge base
tnote search           Search by filename
tnote detail           Read details and processing results
tnote transcribe       Submit a transcription task
tnote summary          Generate a summary
tnote translate        Translate the latest transcription
tnote share            Create a share link
tnote register         Register a public URL
tnote mkdir            Create a directory
```

## License

MIT
