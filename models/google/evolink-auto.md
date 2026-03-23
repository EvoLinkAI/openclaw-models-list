# EvoLink Auto — Google Provider

**Provider:** `evolink-google`
**Model ID:** `evolink-google/evolink/auto`
**API Type:** Google Generative AI
**Base URL:** `https://direct.evolink.ai/v1beta`

## What is EvoLink Auto?

Smart Model Routing — automatically selects the best Gemini model based on your request.

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
openclaw models set evolink-google/evolink/auto
```

## Get API Key

[Sign up at EvoLink.ai](https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=openclaw-models-list)
