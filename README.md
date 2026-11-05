# ATELIER 露序 — Client Advisor Message Agent

A starter project for generating **three Chinese WeChat messages** for a Client Advisor (CA) to choose from. The fictional house sells premium home coffee machines. It covers all six scenarios.

## Brand assumptions

**ATELIER 露序** treats coffee as a considered daily ritual. Luxury is expressed through relevance and care, rather than exaggerated status language. All product details, client records and events here are fictional assignment assumptions.

| Model | Fictional price | Relevant fit | Important limit |
|---|---:|---|---|
| 晨序 | ¥12,800 | Simple black coffee; 24 cm width; two stored preferences | No automatic milk system |
| 暮白 | ¥22,800 | Latte/cappuccino; four stored preferences; 30 cm width | Milk components still need cleaning |
| 匠序 | ¥36,800 | Manual espresso; dual boiler; adjustable extraction temperature; 36 cm width | Separate grinder required; no one-touch milk coffee |

## Setup and run

Use Python 3.11+; Run commands from the `atelier-agent` directory.

```bash
python -m venv .venv

python -m pip install -e ".[dev]"
```

Copy `.env.example` to `.env`. Fill in your own `LLM_API_KEY` and a fixed `LLM_MODEL` ID supporting tool calling. `LLM_PROVIDER=openrouter` matches the reference project.
