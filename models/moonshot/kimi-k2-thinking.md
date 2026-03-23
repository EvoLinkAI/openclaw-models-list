# Kimi K2 Thinking

**Provider:** `moonshot`
**Model ID:** `moonshot/kimi-k2-thinking`
**API Type:** openai-completions
**Base URL:** `https://direct.evolink.ai/v1`

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "moonshot": {
        "api": "openai-completions",
        "baseUrl": "https://direct.evolink.ai/v1",
        "apiKey": "YOUR_API_KEY",
        "models": [
          { "id": "kimi-k2-thinking", "name": "Kimi K2 Thinking" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set moonshot/kimi-k2-thinking
```
