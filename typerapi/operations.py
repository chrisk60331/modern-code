"""Core operations for TyperAPI."""

from pathlib import Path
from typing import Any, Dict, List, Union
import orjson
from rich.console import Console

from typerapi.models import Record, ProcessResponse, GenerateResponse, ValidateResponse

console = Console()


async def read_json(file_path: Union[str, Path]) -> Union[Dict[str, Any], List[Any]]:
    """Read JSON from a file using orjson.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Parsed JSON data as a dict or list
        
    Raises:
        orjson.JSONDecodeError: If JSON is invalid
        FileNotFoundError: If file doesn't exist
    """
    file_path = Path(file_path)
    with file_path.open('rb') as f:
        return orjson.loads(f.read())


async def write_json(
    data: Union[Dict[str, Any], List[Any]],
    file_path: Union[str, Path],
    pretty: bool = True
) -> None:
    """Write data to a JSON file using orjson.
    
    Args:
        data: Data to serialize
        file_path: Output file path
        pretty: Whether to pretty-print the JSON
        
    Raises:
        orjson.JSONEncodeError: If data cannot be serialized
    """
    file_path = Path(file_path)
    opts = orjson.OPT_INDENT_2 if pretty else 0
    with file_path.open('wb') as f:
        f.write(orjson.dumps(data, option=opts))


async def validate_json(file_path: Union[str, Path]) -> bool:
    """Validate that a file contains valid JSON.
    
    Args:
        file_path: Path to the JSON file to validate
        
    Returns:
        True if valid JSON, False otherwise
    """
    try:
        await read_json(file_path)
        return True
    except (orjson.JSONDecodeError, FileNotFoundError):
        return False


async def generate_sample_data(num_records: int = 1000) -> List[Record]:
    """Generate sample JSON data for testing.
    
    Args:
        num_records: Number of records to generate
        
    Returns:
        List of sample records
    """
    return [
        Record(
            id=i,
            name=f"Record {i}",
            active=i % 2 == 0,
            score=i / num_records,
            tags=[f"tag{j}" for j in range(3)]
        )
        for i in range(num_records)
    ]


async def process_data(
    input_file: Union[str, Path],
    output_file: Union[str, Path],
    pretty: bool = True
) -> ProcessResponse:
    """Process data from input file and save to output file.
    
    Args:
        input_file: Input file path
        output_file: Output file path
        pretty: Whether to pretty-print the output
        
    Returns:
        ProcessResponse with operation result
    """
    try:
        data = await read_json(input_file)
        
        # Process the data
        if isinstance(data, dict):
            data['processed'] = True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    item['processed'] = True
        
        await write_json(data, output_file, pretty)
        return ProcessResponse(
            success=True,
            message="Successfully processed data",
            input_file=str(input_file),
            output_file=str(output_file)
        )
    except Exception as e:
        return ProcessResponse(
            success=False,
            message=f"Error processing data: {str(e)}",
            input_file=str(input_file),
            output_file=str(output_file)
        )


async def generate_data(
    output_file: Union[str, Path],
    records: int = 1000,
    pretty: bool = True
) -> GenerateResponse:
    """Generate sample data and save to file.
    
    Args:
        output_file: Output file path
        records: Number of records to generate
        pretty: Whether to pretty-print the output
        
    Returns:
        GenerateResponse with operation result
    """
    try:
        data = await generate_sample_data(records)
        await write_json([record.model_dump() for record in data], output_file, pretty)
        return GenerateResponse(
            success=True,
            message="Successfully generated data",
            output_file=str(output_file),
            records_generated=records
        )
    except Exception as e:
        return GenerateResponse(
            success=False,
            message=f"Error generating data: {str(e)}",
            output_file=str(output_file),
            records_generated=0
        )


async def validate_data(file_path: Union[str, Path]) -> ValidateResponse:
    """Validate data in a file.
    
    Args:
        file_path: File path to validate
        
    Returns:
        ValidateResponse with validation result
    """
    is_valid = await validate_json(file_path)
    return ValidateResponse(
        success=True,
        message="Validation completed",
        file_path=str(file_path),
        is_valid=is_valid
    ) 