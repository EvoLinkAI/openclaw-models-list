# OpenClaw Modelleri

[![OpenClaw Models](banner.jpg)](https://evolink.ai/signup?utm_source=github&utm_medium=banner&utm_campaign=openclaw-models-list)

> OpenClaw için kullanıma hazır konfigürasyonlara sahip, özenle seçilmiş üst düzey AI modelleri listesi.

<p align="center">
  <strong>🌐 Languages：</strong>
  <a href="README.md">English</a> |
  <a href="README-zh-CN.md">简体中文</a> |
  <a href="README-zh-TW.md">繁體中文</a> |
  <a href="README-es.md">Español</a> |
  <a href="README-ja.md">日本語</a> |
  <a href="README-ko.md">한국어</a> |
  <a href="README-tr.md">Türkçe</a> |
  <a href="README-fr.md">Français</a> |
  <a href="README-de.md">Deutsch</a> |
  <a href="README-ru.md">Русский</a>
</p>

---

## Giriş

Bu depo, OpenClaw ile entegrasyon için mevcut olan ana AI modellerini sağlayıcıya göre düzenlenmiş olarak listeler. Her model, kopyala-yapıştır kurulum talimatlarını içeren bir konfigürasyon dosyası ile birlikte gelir.

**Desteklenen sağlayıcılar:**
- 🟣 Anthropic (Claude)
- 🔵 Google (Gemini)
- 🟢 OpenAI (GPT)
- 🟡 ByteDance (Doubao)
- 🌙 Moonshot (Kimi)

---

## Model Listesi

### 🟣 Anthropic (Claude)

| Model | ID | Dosya |
|-------|----|------|
| Claude Opus 4.6 | `anthropic/claude-opus-4-6` | [claude-opus-4-6.md](models/anthropic/claude-opus-4-6.md) |
| Claude Sonnet 4.6 | `anthropic/claude-sonnet-4-6` | [claude-sonnet-4-6.md](models/anthropic/claude-sonnet-4-6.md) |
| Claude Opus 4.5 | `anthropic/claude-opus-4-5-20251101` | [claude-opus-4-5.md](models/anthropic/claude-opus-4-5.md) |
| Claude Opus 4.1 | `anthropic/claude-opus-4-1-20250805` | [claude-opus-4-1.md](models/anthropic/claude-opus-4-1.md) |
| Claude Sonnet 4.5 | `anthropic/claude-sonnet-4-5-20250929` | [claude-sonnet-4-5.md](models/anthropic/claude-sonnet-4-5.md) |
| Claude Sonnet 4 | `anthropic/claude-sonnet-4-20250514` | [claude-sonnet-4.md](models/anthropic/claude-sonnet-4.md) |
| Claude Haiku 4.5 | `anthropic/claude-haiku-4-5-20251001` | [claude-haiku-4-5.md](models/anthropic/claude-haiku-4-5.md) |

### 🔵 Google (Gemini)

| Model | ID | Dosya |
|-------|----|------|
| Gemini 3.1 Flash Lite | `google/gemini-3.1-flash-lite-preview` | [gemini-3-1-flash-lite.md](models/google/gemini-3-1-flash-lite.md) |
| Gemini 3.1 Pro | `google/gemini-3.1-pro-preview` | [gemini-3-1-pro.md](models/google/gemini-3-1-pro.md) |
| Gemini 2.5 Pro | `google/gemini-2.5-pro` | [gemini-2-5-pro.md](models/google/gemini-2-5-pro.md) |
| Gemini 2.5 Flash | `google/gemini-2.5-flash` | [gemini-2-5-flash.md](models/google/gemini-2-5-flash.md) |
| Gemini 3.0 Pro | `google/gemini-3-pro-preview` | [gemini-3-0-pro.md](models/gemini-3-0-pro.md) |
| Gemini 3.0 Flash | `google/gemini-3-flash-preview` | [gemini-3-0-flash.md](models/gemini-3-0-flash.md) |

### 🟢 OpenAI (GPT)

| Model | ID | Dosya |
|-------|----|------|
| GPT-5.4 | `openai/gpt-5.4` | [gpt-5-4.md](models/openai/gpt-5-4.md) |
| GPT-5.2 | `openai/gpt-5.2` | [gpt-5-2.md](models/openai/gpt-5-2.md) |
| GPT-5.1 | `openai/gpt-5.1` | [gpt-5-1.md](models/openai/gpt-5-1.md) |
| GPT-5.1 Chat | `openai/gpt-5.1-chat` | [gpt-5-1-chat.md](models/openai/gpt-5-1-chat.md) |
| GPT-5.1 Thinking | `openai/gpt-5.1-thinking` | [gpt-5-1-thinking.md](models/openai/gpt-5-1-thinking.md) |

### 🟡 ByteDance (Doubao)

| Model | ID | Dosya |
|-------|----|------|
| Doubao Seed 2.0 Pro | `bytedance/doubao-seed-2.0-pro` | [doubao-seed-2-0-pro.md](models/bytedance/doubao-seed-2-0-pro.md) |
| Doubao Seed 2.0 Lite | `bytedance/doubao-seed-2.0-lite` | [doubao-seed-2-0-lite.md](models/bytedance/doubao-seed-2-0-lite.md) |
| Doubao Seed 2.0 Mini | `bytedance/doubao-seed-2.0-mini` | [doubao-seed-2-0-mini.md](models/bytedance/doubao-seed-2-0-mini.md) |
| Doubao Seed 2.0 Code | `bytedance/doubao-seed-2.0-code` | [doubao-seed-2-0-code.md](models/bytedance/doubao-seed-2-0-code.md) |

### 🌙 Moonshot (Kimi)

| Model | ID | Dosya |
|-------|----|------|
| Kimi K2 Thinking | `moonshot/kimi-k2-thinking` | [kimi-k2-thinking.md](models/moonshot/kimi-k2-thinking.md) |
| Kimi K2 Thinking Turbo | `moonshot/kimi-k2-thinking-turbo` | [kimi-k2-thinking-turbo.md](models/moonshot/kimi-k2-thinking-turbo.md) |

---

## Nasıl Kullanılır

### Önkoşullar
1. **Node.js 22+** — [İndir](https://nodejs.org/en/download)
2. **EvoLink API Key** — [Ücretsiz kaydol](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)

### Adım 1: OpenClaw'u Yükleyin

```bash
npm install -g openclaw@latest
```

### Adım 2: Modelleri Yapılandırın

`~/.openclaw/openclaw.json` dosyasını düzenleyin ve model yapılandırmasını ekleyin. Her model dosyası kopyalayıp yapıştırmaya hazır tam yapılandırma içerir.

> ⚠️ Gemini için, `403 Forbidden` hatalarını önlemek amacıyla `baseUrl`, `/v1beta` içermelidir.

### Adım 3: Varsayılan Modeli Ayarlayın

```bash
openclaw models set <provider>/<model-id>
```

### Adım 4: Yeniden Başlat & Doğrula

```bash
openclaw gateway restart
openclaw gateway status
openclaw agent --agent main -m "hi" --json
```

📖 Tam kurulum kılavuzu: [docs.openclaw.ai](https://docs.openclaw.ai)
