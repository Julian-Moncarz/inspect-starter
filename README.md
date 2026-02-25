## Quickest setup: GitHub Codespaces

Click the button below to open this repo in a browser-based VS Code with everything pre-installed:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Julian-Moncarz/inspect-starter?quickstart=1)

Once it loads, open the terminal and run:

```bash
export OPENROUTER_API_KEY="your-key-here"
inspect eval example_task.py --model openrouter/openai/gpt-4o-mini
```

## Mac/Linux local setup

```bash
pip install inspect-ai
export OPENROUTER_API_KEY="your-key-here"
inspect eval example_task.py --model openrouter/openai/gpt-4o-mini
```
