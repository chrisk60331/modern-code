"""Command-line interface using Typer."""

import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel

from typerapi.operations import process_data, generate_data, validate_data

# Create Typer app
app = typer.Typer(
    name="typerapi",
    help="Modern CLI interface for data processing",
    add_completion=False,
)

# Create console for rich output
console = Console()


def print_success(message: str) -> None:
    """Print success message in green."""
    console.print(Panel(message, style="green"))


def print_error(message: str) -> None:
    """Print error message in red."""
    console.print(Panel(message, style="red"))


@app.command()
def process(
    input_file: Path = typer.Argument(..., help="Input file path"),
    output_file: Path = typer.Argument(..., help="Output file path"),
    pretty: bool = typer.Option(True, help="Pretty print output"),
) -> None:
    """Process data from input file and save to output file."""
    try:
        response = asyncio.run(process_data(input_file, output_file, pretty))
        if response.success:
            print_success(response.message)
        else:
            print_error(response.message)
            raise typer.Exit(1)
    except Exception as e:
        print_error(f"Error: {str(e)}")
        raise typer.Exit(1)


@app.command()
def generate(
    output_file: Path = typer.Argument(..., help="Output file path"),
    records: int = typer.Option(1000, help="Number of records to generate"),
    pretty: bool = typer.Option(True, help="Pretty print output"),
) -> None:
    """Generate sample data and save to file."""
    try:
        response = asyncio.run(generate_data(output_file, records, pretty))
        if response.success:
            print_success(response.message)
        else:
            print_error(response.message)
            raise typer.Exit(1)
    except Exception as e:
        print_error(f"Error: {str(e)}")
        raise typer.Exit(1)


@app.command()
def validate(
    file_path: Path = typer.Argument(..., help="File path to validate"),
) -> None:
    """Validate data in a file."""
    try:
        response = asyncio.run(validate_data(file_path))
        if response.is_valid:
            print_success(f"{file_path} contains valid data")
        else:
            print_error(f"{file_path} contains invalid data")
            raise typer.Exit(1)
    except Exception as e:
        print_error(f"Error: {str(e)}")
        raise typer.Exit(1)


@app.command()
def serve(
    host: str = typer.Option("127.0.0.1", help="Host to bind to"),
    port: int = typer.Option(8000, help="Port to bind to"),
) -> None:
    """Start the FastAPI server."""
    import uvicorn
    from typerapi.api import app as api_app
    
    console.print(f"Starting server at http://{host}:{port}")
    console.print("Press Ctrl+C to stop")
    uvicorn.run(api_app, host=host, port=port)


if __name__ == "__main__":
    app() 