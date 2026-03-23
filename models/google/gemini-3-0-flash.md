# Gemini 3.0 Flash

**Provider:** `google`
**Model ID:** `google/gemini-3-flash-preview`
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
          { "id": "gemini-3-flash-preview", "name": "Gemini 3.0 Flash" }
        ]
      }
    }
  }
}
```

> ⚠️ `baseUrl` must include `/v1beta` — without it you will get `403 Forbidden`.

## Set as Default

```bash
openclaw models set google/gemini-3-flash-preview
```
