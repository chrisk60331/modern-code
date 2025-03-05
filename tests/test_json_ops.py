"""Tests for JSON operations."""

from pathlib import Path
import pytest

from click_demo import json_ops


@pytest.fixture
def sample_data():
    """Generate sample data for tests."""
    return json_ops.generate_sample_data(10)


@pytest.fixture
def temp_json_file(tmp_path):
    """Create a temporary JSON file."""
    return tmp_path / "test.json"


def test_write_and_read_json(sample_data, temp_json_file):
    """Test writing and reading JSON data."""
    # Write data
    json_ops.write_json(sample_data, temp_json_file)
    assert temp_json_file.exists()
    
    # Read data back
    loaded_data = json_ops.read_json(temp_json_file)
    assert loaded_data == sample_data


def test_validate_json(sample_data, temp_json_file):
    """Test JSON validation."""
    # Valid JSON
    json_ops.write_json(sample_data, temp_json_file)
    assert json_ops.validate_json(temp_json_file)
    
    # Invalid JSON
    temp_json_file.write_text("{invalid json")
    assert not json_ops.validate_json(temp_json_file)
    
    # Non-existent file
    assert not json_ops.validate_json(Path("nonexistent.json"))


def test_generate_sample_data():
    """Test sample data generation."""
    data = json_ops.generate_sample_data(5)
    assert len(data) == 5
    assert all(isinstance(item, dict) for item in data)
    assert all("id" in item for item in data)
    assert all("name" in item for item in data)
    assert all("active" in item for item in data)
    assert all("score" in item for item in data)
    assert all("tags" in item for item in data) 