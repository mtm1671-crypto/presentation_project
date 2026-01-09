# Agent Project

This is the tiniest of AI agents, used to show off the very basics of how modern LLMs can interact with a codebase

## Features

- **File Operations**: List directories, read file contents, and write/overwrite files
- **Code Execution**: Run Python files with optional arguments
- **Agentic Loop**: Iteratively calls tools until the task is complete

## Setup

1. Install dependencies:
   ```bash
   pip install anthropic python-dotenv
   ```

2. Set your Anthropic API key in a `.env` file:
   ```
   ANTHROPIC_API_KEY=your_api_key
   ```

## Usage

```bash
python main.py "your prompt here"
```

Add `--verbose` for detailed output including token usage and function call results.

## Example

```bash
python main.py "List all Python files and summarize what they do"
```
