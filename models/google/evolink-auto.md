# EvoLink Auto

**Provider:** `google`
**Model ID:** `google/evolink/auto`
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
          { "id": "evolink/auto", "name": "EvoLink Auto" }
        ]
      }
    }
  }
}
```

> ⚠️ `baseUrl` must include `/v1beta` — without it you will get `403 Forbidden`.

## Set as Default

```bash
openclaw models set google/evolink/auto
```
