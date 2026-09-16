# Sell It AI

Sell It on the Web with AI

## Setup

A local running OpenAI API compatibile LLM engine is needed on `localhost:8000` to run the main or the tests (see `src/sellitai/categorizer/openai.py`).

Install uv (if not installed)

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install project dependencies
```
$ uv sync
```

Starts the Flask server on http://localhost:8001
```
$ uv run main
```

