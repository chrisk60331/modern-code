"""JSON operations using orjson for high-performance processing."""

from pathlib import Path
from typing import Any, Dict, List, Union
import orjson


def read_json(file_path: Union[str, Path]) -> Union[Dict[str, Any], List[Any]]:
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


def write_json(
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


def validate_json(file_path: Union[str, Path]) -> bool:
    """Validate that a file contains valid JSON.
    
    Args:
        file_path: Path to the JSON file to validate
        
    Returns:
        True if valid JSON, False otherwise
    """
    try:
        read_json(file_path)
        return True
    except (orjson.JSONDecodeError, FileNotFoundError):
        return False


def generate_sample_data(num_records: int = 1000) -> List[Dict[str, Any]]:
    """Generate sample JSON data for testing.
    
    Args:
        num_records: Number of records to generate
        
    Returns:
        List of sample records
    """
    return [
        {
            "id": i,
            "name": f"Record {i}",
            "active": i % 2 == 0,
            "score": i / num_records,
            "tags": [f"tag{j}" for j in range(3)]
        }
        for i in range(num_records)
    ] 