# TyperAPI

A modern CLI and API interface for data processing, built with Typer and FastAPI.

## Features

- Modern CLI interface using Typer
- Fast API endpoints using FastAPI
- High-performance JSON processing with orjson
- Beautiful terminal output with Rich
- Type hints and Pydantic models throughout
- Async operations for better performance
- OpenAPI documentation
- CORS support for API endpoints

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

## CLI Usage

The CLI provides several commands for data processing:

```bash
# Show help
typerapi --help

# Process data
typerapi process input.json output.json

# Generate sample data
typerapi generate output.json --records 1000

# Validate data
typerapi validate input.json

# Start API server
typerapi serve --host 0.0.0.0 --port 8000
```

## API Usage

Start the API server:
```bash
typerapi serve
```

The API will be available at `http://localhost:8000` with the following endpoints:

- `POST /process` - Process data from input file
- `POST /generate` - Generate sample data
- `POST /validate` - Validate data in a file
- `GET /` - API information

View the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Example API Requests

```bash
# Process data
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{"input_file": "input.json", "output_file": "output.json"}'

# Generate data
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"output_file": "output.json", "records": 1000}'

# Validate data
curl -X POST http://localhost:8000/validate \
  -H "Content-Type: application/json" \
  -d '{"file_path": "input.json"}'
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

## Project Structure

```
typerapi/
├── api.py          # FastAPI application
├── cli.py          # Typer CLI application
├── models.py       # Pydantic models
└── operations.py   # Core operations
```

## License

MIT 