"""FastAPI application for TyperAPI."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from typerapi.models import (
    ProcessRequest, ProcessResponse,
    GenerateRequest, GenerateResponse,
    ValidateRequest, ValidateResponse
)
from typerapi.operations import process_data, generate_data, validate_data

app = FastAPI(
    title="TyperAPI",
    description="Modern API interface for data processing",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/process", response_model=ProcessResponse)
async def process(request: ProcessRequest) -> ProcessResponse:
    """Process data from input file and save to output file."""
    response = await process_data(
        request.input_file,
        request.output_file,
        request.pretty
    )
    if not response.success:
        raise HTTPException(status_code=400, detail=response.message)
    return response


@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest) -> GenerateResponse:
    """Generate sample data and save to file."""
    response = await generate_data(
        request.output_file,
        request.records,
        request.pretty
    )
    if not response.success:
        raise HTTPException(status_code=400, detail=response.message)
    return response


@app.post("/validate", response_model=ValidateResponse)
async def validate(request: ValidateRequest) -> ValidateResponse:
    """Validate data in a file."""
    return await validate_data(request.file_path)


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "TyperAPI",
        "version": "0.1.0",
        "description": "Modern API interface for data processing",
        "endpoints": [
            "/process",
            "/generate",
            "/validate"
        ]
    } 