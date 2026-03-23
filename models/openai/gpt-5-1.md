# GPT-5.1

**Provider:** `openai`
**Model ID:** `openai/gpt-5.1`
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
          { "id": "gpt-5.1", "name": "GPT-5.1" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set openai/gpt-5.1
```
