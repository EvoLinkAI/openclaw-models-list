# OpenClaw 모델

[![OpenClaw Models](banner.jpg)](https://evolink.ai/signup?utm_source=github&utm_medium=banner&utm_campaign=openclaw-models-list)

> OpenClaw를 위한 바로 사용 가능한 설정이 포함된 최상위 AI 모델 목록입니다.

---

## 소개

이 저장소는 OpenClaw와 통합할 수 있는 주요 AI 모델들을 제공자별로 나열합니다. 각 모델에는 복사 및 붙여넣기가 가능한 설정 파일이 포함되어 있습니다.

**지원 제공자:**
- 🟣 Anthropic (Claude)
- 🔵 Google (Gemini)
- 🟢 OpenAI (GPT)
- 🟡 ByteDance (Doubao)
- 🌙 Moonshot (Kimi)

---

## 모델 목록

### 🟣 Anthropic (Claude)

| 모델 | ID | 파일 |
|-------|----|------|
| Claude Opus 4.6 | `anthropic/claude-opus-4-6` | [claude-opus-4-6.md](models/anthropic/claude-opus-4-6.md) |
| Claude Sonnet 4.6 | `anthropic/claude-sonnet-4-6` | [claude-sonnet-4-6.md](models/anthropic/claude-sonnet-4-6.md) |
| Claude Opus 4.5 | `anthropic/claude-opus-4-5-20251101` | [claude-opus-4-5.md](models/anthropic/claude-opus-4-5.md) |
| Claude Opus 4.1 | `anthropic/claude-opus-4-1-20250805` | [claude-opus-4-1.md](models/anthropic/claude-opus-4-1.md) |
| Claude Sonnet 4.5 | `anthropic/claude-sonnet-4-5-20250929` | [claude-sonnet-4-5.md](models/anthropic/claude-sonnet-4-5.md) |
| Claude Sonnet 4 | `anthropic/claude-sonnet-4-20250514` | [claude-sonnet-4.md](models/anthropic/claude-sonnet-4.md) |
| Claude Haiku 4.5 | `anthropic/claude-haiku-4-5-20251001` | [claude-haiku-4-5.md](models/anthropic/claude-haiku-4-5.md) |

### 🔵 Google (Gemini)

| 모델 | ID | 파일 |
|-------|----|------|
| Gemini 3.1 Flash Lite | `google/gemini-3.1-flash-lite-preview` | [gemini-3-1-flash-lite.md](models/google/gemini-3-1-flash-lite.md) |
| Gemini 3.1 Pro | `google/gemini-3.1-pro-preview` | [gemini-3-1-pro.md](models/google/gemini-3-1-pro.md) |
| Gemini 2.5 Pro | `google/gemini-2.5-pro` | [gemini-2-5-pro.md](models/google/gemini-2-5-pro.md) |
| Gemini 2.5 Flash | `google/gemini-2.5-flash` | [gemini-2-5-flash.md](models/google/gemini-2-5-flash.md) |
| Gemini 3.0 Pro | `google/gemini-3-pro-preview` | [gemini-3-0-pro.md](models/google/gemini-3-0-pro.md) |
| Gemini 3.0 Flash | `google/gemini-3-flash-preview` | [gemini-3-0-flash.md](models/gemini-3-0-flash.md) |

### 🟢 OpenAI (GPT)

| 모델 | ID | 파일 |
|-------|----|------|
| GPT-5.4 | `openai/gpt-5.4` | [gpt-5-4.md](models/openai/gpt-5-4.md) |
| GPT-5.2 | `openai/gpt-5.2` | [gpt-5-2.md](models/openai/gpt-5-2.md) |
| GPT-5.1 | `openai/gpt-5.1` | [gpt-5-1.md](models/openai/gpt-5-1.md) |
| GPT-5.1 Chat | `openai/gpt-5.1-chat` | [gpt-5-1-chat.md](models/openai/gpt-5-1-chat.md) |
| GPT-5.1 Thinking | `openai/gpt-5.1-thinking` | [gpt-5-1-thinking.md](models/openai/gpt-5-1-thinking.md) |

### 🟡 ByteDance (Doubao)

| 모델 | ID | 파일 |
|-------|----|------|
| Doubao Seed 2.0 Pro | `bytedance/doubao-seed-2.0-pro` | [doubao-seed-2-0-pro.md](models/bytedance/doubao-seed-2-0-pro.md) |
| Doubao Seed 2.0 Lite | `bytedance/doubao-seed-2.0-lite` | [doubao-seed-2-0-lite.md](models/bytedance/doubao-seed-2-0-lite.md) |
| Doubao Seed 2.0 Mini | `bytedance/doubao-seed-2.0-mini` | [doubao-seed-2-0-mini.md](models/bytedance/doubao-seed-2-0-mini.md) |
| Doubao Seed 2.0 Code | `bytedance/doubao-seed-2.0-code` | [doubao-seed-2-0-code.md](models/bytedance/doubao-seed-2-0-code.md) |

### 🌙 Moonshot (Kimi)

| 모델 | ID | 파일 |
|-------|----|------|
| Kimi K2 Thinking | `moonshot/kimi-k2-thinking` | [kimi-k2-thinking.md](models/moonshot/kimi-k2-thinking.md) |
| Kimi K2 Thinking Turbo | `moonshot/kimi-k2-thinking-turbo` | [kimi-k2-thinking-turbo.md](models/moonshot/kimi-k2-thinking-turbo.md) |

---

## 사용 방법

### 전제 조건
1. **Node.js 22+** — [다운로드](https://nodejs.org/en/download)
2. 선호하는 제공자의 **API 키**.

### 단계 1: OpenClaw 설치

```bash
npm install -g openclaw@latest
```

### 단계 2: 모델 설정

`~/.openclaw/openclaw.json` 파일을 편집하여 선택한 제공자를 설정합니다. 스키마 세부 사항은 [문서](https://docs.openclaw.ai)를 참조하십시오.

> ⚠️ Gemini 모델의 경우, `403 Forbidden` 오류를 방지하기 위해 `baseUrl`에 `/v1beta`가 포함되어야 합니다.

### 단계 3: 기본 모델 설정

```bash
openclaw models set <provider>/<model-id>
```

### 단계 4: 재시작 및 검증

```bash
openclaw gateway restart
openclaw gateway status
openclaw agent --agent main -m "hi" --json
```

📖 전체 설정 가이드: [docs.openclaw.ai](https://docs.openclaw.ai)
