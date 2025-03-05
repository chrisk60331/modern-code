"""Command-line interface using Click."""

from pathlib import Path
from typing import Optional
import sys

import click

from click_demo import json_ops


def print_error(message: str) -> None:
    """Print error message in red."""
    click.secho(f"Error: {message}", fg="red", err=True)


@click.group()
@click.version_option()
def main() -> None:
    """CLI tool demonstrating Click, uv, and orjson best practices."""
    pass


@main.command()
@click.argument('input_file', type=click.Path(exists=True, path_type=Path))
@click.argument('output_file', type=click.Path(path_type=Path))
@click.option('--pretty/--no-pretty', default=True, help='Pretty-print output JSON')
def process(input_file: Path, output_file: Path, pretty: bool) -> None:
    """Process a JSON file and save the result.
    
    This command demonstrates reading, processing, and writing JSON using orjson.
    """
    try:
        # Read input JSON
        data = json_ops.read_json(input_file)
        
        # Process the data (example: add metadata)
        if isinstance(data, dict):
            data['processed'] = True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    item['processed'] = True
        
        # Write processed data
        json_ops.write_json(data, output_file, pretty=pretty)
        click.secho(f"Successfully processed {input_file} → {output_file}", fg="green")
        
    except Exception as e:
        print_error(str(e))
        sys.exit(1)


@main.command()
@click.argument('output_file', type=click.Path(path_type=Path))
@click.option('--records', '-n', default=1000, help='Number of records to generate')
@click.option('--pretty/--no-pretty', default=True, help='Pretty-print output JSON')
def generate(output_file: Path, records: int, pretty: bool) -> None:
    """Generate sample JSON data for testing."""
    try:
        data = json_ops.generate_sample_data(records)
        json_ops.write_json(data, output_file, pretty=pretty)
        click.secho(
            f"Generated {records} records to {output_file}",
            fg="green"
        )
    except Exception as e:
        print_error(str(e))
        sys.exit(1)


@main.command()
@click.argument('file_path', type=click.Path(path_type=Path))
def validate(file_path: Path) -> None:
    """Validate that a file contains valid JSON."""
    if json_ops.validate_json(file_path):
        click.secho(f"{file_path} contains valid JSON", fg="green")
    else:
        print_error(f"{file_path} contains invalid JSON")
        sys.exit(1)


if __name__ == '__main__':
    main() 