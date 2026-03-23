# Gemini 2.5 Pro

**Provider:** `google`
**Model ID:** `google/gemini-2.5-pro`
**API Type:** google-generative-ai
**Base URL:** `https://direct.evolink.ai/v1beta`

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "google": {
        "api": "google-generative-ai",
        "baseUrl": "https://direct.evolink.ai/v1beta",
        "apiKey": "YOUR_API_KEY",
        "models": [
          { "id": "gemini-2.5-pro", "name": "Gemini 2.5 Pro" }
        ]
      }
    }
  }
}
```

> ⚠️ `baseUrl` must include `/v1beta` — without it you will get `403 Forbidden`.

## Set as Default

```bash
openclaw models set google/gemini-2.5-pro
```
