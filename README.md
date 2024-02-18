# transaction_categorizer


## Pre-requisites
- poetry [Installation](https://python-poetry.org/docs/#installation)
- Ollama with llama2 model pulled **or** 
- Access to OpenAI API through API key exported to environment variable `OPENAI_API_KEY`

## Install dependencies
```sh
poetry install
```

## Run categorizer
```sh
poetry run python transaction_categorizer/main.py -d ClasOhlsonRingen -m llama2
```
