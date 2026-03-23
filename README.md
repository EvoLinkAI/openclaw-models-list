# openclaw-models-list

> Complete list of AI models available via EvoLink API, with ready-to-use OpenClaw configurations.

[![EvoLink](https://img.shields.io/badge/Powered%20by-EvoLink.ai-blue)](https://evolink.ai/signup?utm_source=github&utm_medium=banner&utm_campaign=openclaw-models-list)

---

## Introduction

[EvoLink.ai](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list) is an AI API gateway that gives you access to all major AI models — Claude, GPT, Gemini, Doubao, Kimi — with a single API key.

This repo lists every model available via EvoLink, organized by provider. Each model has its own configuration file with copy-paste setup for OpenClaw.

**Supported providers:**
- 🟣 Anthropic (Claude)
- 🔵 Google (Gemini)
- 🟢 OpenAI (GPT)
- 🟡 ByteDance (Doubao)
- 🌙 Moonshot (Kimi)

---

## Models List

### 🟣 Anthropic

| Model | ID | File |
|-------|----|------|
| EvoLink Auto | `evolink-anthropic/evolink/auto` | [evolink-auto.md](models/anthropic/evolink-auto.md) |
| Claude Opus 4.6 | `evolink-anthropic/claude-opus-4-6` | [claude-opus-4-6.md](models/anthropic/claude-opus-4-6.md) |
| Claude Sonnet 4.6 | `evolink-anthropic/claude-sonnet-4-6` | [claude-sonnet-4-6.md](models/anthropic/claude-sonnet-4-6.md) |
| Claude Opus 4.5 | `evolink-anthropic/claude-opus-4-5-20251101` | [claude-opus-4-5.md](models/anthropic/claude-opus-4-5.md) |
| Claude Opus 4.1 | `evolink-anthropic/claude-opus-4-1-20250805` | [claude-opus-4-1.md](models/anthropic/claude-opus-4-1.md) |
| Claude Sonnet 4.5 | `evolink-anthropic/claude-sonnet-4-5-20250929` | [claude-sonnet-4-5.md](models/anthropic/claude-sonnet-4-5.md) |
| Claude Sonnet 4 | `evolink-anthropic/claude-sonnet-4-20250514` | [claude-sonnet-4.md](models/anthropic/claude-sonnet-4.md) |
| Claude Haiku 4.5 | `evolink-anthropic/claude-haiku-4-5-20251001` | [claude-haiku-4-5.md](models/anthropic/claude-haiku-4-5.md) |

### 🔵 Google

| Model | ID | File |
|-------|----|------|
| EvoLink Auto | `evolink-google/evolink/auto` | [evolink-auto.md](models/google/evolink-auto.md) |
| Gemini 3.1 Flash Lite | `evolink-google/gemini-3.1-flash-lite-preview` | [gemini-3-1-flash-lite.md](models/google/gemini-3-1-flash-lite.md) |
| Gemini 3.1 Pro | `evolink-google/gemini-3.1-pro-preview` | [gemini-3-1-pro.md](models/google/gemini-3-1-pro.md) |
| Gemini 2.5 Pro | `evolink-google/gemini-2.5-pro` | [gemini-2-5-pro.md](models/google/gemini-2-5-pro.md) |
| Gemini 2.5 Flash | `evolink-google/gemini-2.5-flash` | [gemini-2-5-flash.md](models/google/gemini-2-5-flash.md) |
| Gemini 3.0 Pro | `evolink-google/gemini-3-pro-preview` | [gemini-3-0-pro.md](models/google/gemini-3-0-pro.md) |
| Gemini 3.0 Flash | `evolink-google/gemini-3-flash-preview` | [gemini-3-0-flash.md](models/google/gemini-3-0-flash.md) |

### 🟢 OpenAI

| Model | ID | File |
|-------|----|------|
| GPT-5.4 | `evolink-openai/gpt-5.4` | [gpt-5-4.md](models/openai/gpt-5-4.md) |
| GPT-5.2 | `evolink-openai/gpt-5.2` | [gpt-5-2.md](models/openai/gpt-5-2.md) |
| GPT-5.1 | `evolink-openai/gpt-5.1` | [gpt-5-1.md](models/openai/gpt-5-1.md) |
| GPT-5.1 Chat | `evolink-openai/gpt-5.1-chat` | [gpt-5-1-chat.md](models/openai/gpt-5-1-chat.md) |
| GPT-5.1 Thinking | `evolink-openai/gpt-5.1-thinking` | [gpt-5-1-thinking.md](models/openai/gpt-5-1-thinking.md) |

### 🟡 ByteDance (Doubao)

| Model | ID | File |
|-------|----|------|
| Doubao Seed 2.0 Pro | `evolink-openai/doubao-seed-2.0-pro` | [doubao-seed-2-0-pro.md](models/bytedance/doubao-seed-2-0-pro.md) |
| Doubao Seed 2.0 Lite | `evolink-openai/doubao-seed-2.0-lite` | [doubao-seed-2-0-lite.md](models/bytedance/doubao-seed-2-0-lite.md) |
| Doubao Seed 2.0 Mini | `evolink-openai/doubao-seed-2.0-mini` | [doubao-seed-2-0-mini.md](models/bytedance/doubao-seed-2-0-mini.md) |
| Doubao Seed 2.0 Code | `evolink-openai/doubao-seed-2.0-code` | [doubao-seed-2-0-code.md](models/bytedance/doubao-seed-2-0-code.md) |

### 🌙 Moonshot (Kimi)

| Model | ID | File |
|-------|----|------|
| Kimi K2 Thinking | `evolink-openai/kimi-k2-thinking` | [kimi-k2-thinking.md](models/moonshot/kimi-k2-thinking.md) |
| Kimi K2 Thinking Turbo | `evolink-openai/kimi-k2-thinking-turbo` | [kimi-k2-thinking-turbo.md](models/moonshot/kimi-k2-thinking-turbo.md) |

---

## How to Use

### Prerequisites
1. **Node.js 22+** — [Download](https://nodejs.org/en/download)
2. **EvoLink API Key** — [Get one free](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)

### Step 1: Install OpenClaw

```bash
npm install -g openclaw@latest
```

### Step 2: Configure EvoLink as Provider

Edit `~/.openclaw/openclaw.json` and add the providers. See the full config in [models.json](models.json).

> ⚠️ For Gemini, `baseUrl` must include `/v1beta` — without it you will get `403 Forbidden`.

### Step 3: Set Default Model

```bash
# Smart Routing (recommended)
openclaw models set evolink-anthropic/evolink/auto

# Or a specific model
openclaw models set evolink-anthropic/claude-sonnet-4-6
openclaw models set evolink-openai/gpt-5.4
openclaw models set evolink-google/gemini-2.5-pro
```

### Step 4: Restart & Verify

```bash
openclaw gateway restart
openclaw gateway status
openclaw agent --agent main -m "hi" --json
```

📖 Full setup guide: [docs.evolink.ai](https://docs.evolink.ai/en/integration-guide/openclaw?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)

---

## Get Your API Key

[Sign up at EvoLink.ai →](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)

- One key, all models
- Save 20–70% vs direct API pricing
- 99.9% uptime with auto-failover
