# Gemini 3.0 Flash — via EvoLink

**Provider:** `evolink-google`
**Model ID:** `evolink-google/gemini-3-flash-preview`
**API Type:** Google Generative AI
**Base URL:** `https://direct.evolink.ai/v1beta`

## OpenClaw Configuration

```json
{
  "models": {
    "providers": {
      "evolink-google": {
        "api": "google-generative-ai",
        "baseUrl": "https://direct.evolink.ai/v1beta",
        "apiKey": "Your EvoLink API Key",
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
openclaw models set evolink-google/gemini-3-flash-preview
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
