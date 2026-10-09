# Google Hosted LLM + Ollama

This folder contains examples and setup for working with both:

- Google-hosted LLMs (for example, Gemini models via Google AI APIs)
- Ollama local LLMs (run models on your machine without sending data to the cloud)

It is useful when you want to compare, prototype, or switch between cloud-hosted inference and local model inference.

## What is included

This folder is intended for:

- Google Generative AI / hosted LLM integrations
- Ollama model setup and local inference
- Example prompts, configuration, and scripts
- Development patterns for testing both approaches

## Google Hosted LLM

Google-hosted models are good when you want:

- quick setup
- managed infrastructure
- access to large hosted models
- no local GPU requirement

Typical setup includes:

- a Google API key
- environment variables for authentication
- calls to the Google Generative AI SDK or REST APIs

## Ollama

Ollama is useful when you want:

- local inference
- private or offline use
- faster iteration on your machine
- control over model files and runtime

Typical usage:

- install Ollama
- pull a model such as `llama3.1`, `mistral`, `qwen2.5`, or similar
- run models locally with a client or script

## Recommended workflow

1. Use Google-hosted LLMs for quick validation and cloud-based access.
2. Use Ollama for local development, testing, and privacy-sensitive workloads.
3. Keep prompts and code flexible so you can switch providers easily.

## Example commands

### Ollama

```bash
ollama pull llama3.1
ollama run llama3.1
```

### Google AI setup

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

Then use the Google SDK or API to call your selected model.

## Notes

- Keep API keys in environment variables or secret managers.
- Test both providers with the same prompt to compare quality, speed, and cost.
- Choose hosted vs local based on privacy, latency, model availability, and budget.

## Summary

This folder is set up to explore and experiment with both Google-hosted LLMs and Ollama-powered local models in a single environment.
