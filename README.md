# Click Demo

A proof of concept demonstrating best practices using Python Click, uv, and orjson.

## Features

- Modern CLI application structure using Click
- Fast JSON processing with orjson
- Dependency management with uv
- Type hints and modern Python practices

## Installation

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
uv pip install -e .
```

## Usage

The CLI provides several commands for demonstration:

```bash
# Show help
clickdemo --help

# Process a JSON file
clickdemo process input.json

# Generate sample data
clickdemo generate output.json --records 1000

# Validate JSON
clickdemo validate input.json
```

## Development

To set up for development:

1. Clone the repository
2. Create a virtual environment with uv
3. Install dependencies
4. Run tests:
```bash
pytest
``` 