# GPT-5.1 Chat

**Provider:** `openai`
**Model ID:** `openai/gpt-5.1-chat`
**API Type:** openai-completions
**Base URL:** `https://direct.evolink.ai/v1`

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "openai": {
        "api": "openai-completions",
        "baseUrl": "https://direct.evolink.ai/v1",
        "apiKey": "YOUR_API_KEY",
        "models": [
          { "id": "gpt-5.1-chat", "name": "GPT-5.1 Chat" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set openai/gpt-5.1-chat
```
