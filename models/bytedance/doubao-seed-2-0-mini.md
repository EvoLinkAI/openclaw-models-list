# Doubao Seed 2.0 Mini

**Provider:** `bytedance`
**Model ID:** `bytedance/doubao-seed-2.0-mini`
**API Type:** openai-completions
**Base URL:** `https://direct.evolink.ai/v1`

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "bytedance": {
        "api": "openai-completions",
        "baseUrl": "https://direct.evolink.ai/v1",
        "apiKey": "YOUR_API_KEY",
        "models": [
          { "id": "doubao-seed-2.0-mini", "name": "Doubao Seed 2.0 Mini" }
        ]
      }
    }
  }
}
```

## Set as Default

```bash
openclaw models set bytedance/doubao-seed-2.0-mini
```
