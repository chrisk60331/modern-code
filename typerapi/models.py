"""Pydantic models for TyperAPI."""

from typing import List, Optional
from pydantic import BaseModel, Field


class Record(BaseModel):
    """A single record in our data structure."""
    id: int = Field(..., description="Unique identifier")
    name: str = Field(..., description="Name of the record")
    active: bool = Field(..., description="Active status")
    score: float = Field(..., description="Score value")
    tags: List[str] = Field(default_factory=list, description="List of tags")
    processed: bool = Field(default=False, description="Processing status")


class ProcessRequest(BaseModel):
    """Request model for processing data."""
    input_file: str = Field(..., description="Input file path")
    output_file: str = Field(..., description="Output file path")
    pretty: bool = Field(default=True, description="Pretty print output")


class GenerateRequest(BaseModel):
    """Request model for generating sample data."""
    output_file: str = Field(..., description="Output file path")
    records: int = Field(default=1000, description="Number of records to generate")
    pretty: bool = Field(default=True, description="Pretty print output")


class ValidateRequest(BaseModel):
    """Request model for validating data."""
    file_path: str = Field(..., description="File path to validate")


class ProcessResponse(BaseModel):
    """Response model for processing operation."""
    success: bool = Field(..., description="Operation success status")
    message: str = Field(..., description="Operation result message")
    input_file: str = Field(..., description="Input file path")
    output_file: str = Field(..., description="Output file path")


class GenerateResponse(BaseModel):
    """Response model for generate operation."""
    success: bool = Field(..., description="Operation success status")
    message: str = Field(..., description="Operation result message")
    output_file: str = Field(..., description="Output file path")
    records_generated: int = Field(..., description="Number of records generated")


class ValidateResponse(BaseModel):
    """Response model for validate operation."""
    success: bool = Field(..., description="Operation success status")
    message: str = Field(..., description="Operation result message")
    file_path: str = Field(..., description="File path validated")
    is_valid: bool = Field(..., description="Validation result") 