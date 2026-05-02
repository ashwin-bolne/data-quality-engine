# Intelligent Data Quality Engine

## Project Overview 

This project is an end-to-end data quality validation and monitoring pipeline designed for structured datasets (CSV/JSON). It performs schema validation, statistical analysis, and data quality scoring, with optional preprocessing and persistent storage of results.

The system simulates a production-style data quality workflow used in data engineering and machine learning pipelines, where poor data quality can directly impact downstream analytics and model performance.

Key capabilities include:
- Automated schema validation and error handling
- Statistical profiling using NumPy
- Data quality scoring based on dataset characteristics
- Optional preprocessing pipeline using Pandas
- Persistent tracking of historical quality runs using SQLite
- CLI-based interaction for analysis, history tracking, and diagnostics

## Features

- **Robust Data Ingestion**
  - Loads structured datasets from CSV files with strict error handling for missing files, invalid formats, and parsing issues.

- **Schema Validation**
  - Ensures dataset consistency by validating column structure and detecting schema mismatches.

- **Statistical Analysis (NumPy-based)**
  - Computes column-wise statistics including mean, standard deviation, and percentiles using vectorized operations.

- **Data Quality Scoring**
  - Assigns a quality score based on dataset characteristics such as null values, data types, and row-level integrity.

- **Optional Data Preprocessing Pipeline (`--clean`)**
  - Modular Pandas pipeline for:
    - Dropping high-null columns
    - Filling missing numeric values
    - Encoding categorical variables

- **Persistent Storage with SQLite**
  - Stores metadata of each data quality run for tracking and auditing.

- **CLI-Based Querying**
  - `--history`: View recent dataset quality runs  
  - `--worst N`: Identify lowest-quality datasets  

- **Verbose Mode (`-v`)**
  - Displays detailed column-level statistics for deeper inspection.

- **Structured Exception Handling**
  - Custom exceptions for file handling, parsing errors, and schema mismatches ensure predictable system behavior.

## Architecture

The system follows a modular data processing pipeline, where each stage is responsible for a specific transformation or validation step.

```mermaid
flowchart TD

A[CLI Input: CSV] --> B[Loader]
B --> C[Schema Validator]
C --> D[Analyzer (NumPy Statistics)]
D --> E[Scorer (Data Quality Score)]

E --> F{--clean flag?}

F -->|Yes| G[Pandas Preprocessing Pipeline]
F -->|No| H[Skip Cleaning]

G --> I[(SQLite Storage)]
H --> I

I --> J[Reporter (CLI Output)]

---
Pipeline Explanation
Loader: Reads input dataset and handles file-related errors
Validator: Ensures schema consistency across columns
Analyzer: Computes statistical summaries using NumPy
Scorer: Generates an overall data quality score
Preprocessing Pipeline (--clean): Applies optional transformations for data cleaning
SQLite Storage: Persists run metadata for historical tracking
Reporter: Outputs validation results and quality metrics via CLI

The pipeline is designed to be modular, allowing each stage to be extended or replaced independently.
---

## Tech Stack

- **Python 3.11** — Core application logic and CLI orchestration  
- **Pandas** — Data preprocessing pipeline and transformations  
- **NumPy** — Efficient statistical computations for analysis  
- **SQLite** — Lightweight persistent storage for tracking data quality runs  
- **Pytest** — Unit testing framework for validating core components  

## Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd data-quality-engine

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt

## Usage

### Run Data Quality Analysis
```bash
python main.py data/sample.csv

python main.py data/sample.csv --clean

python main.py data/sample.csv -v

python main.py --history

python main.py --worst 5

## CLI Reference

### Arguments

- `<path_to_csv>`  
  Path to the input CSV dataset.

### Options

- `-v`  
  Enable verbose output with column-wise statistics.

- `--clean`  
  Run the Pandas preprocessing pipeline (drop high-null columns, fill missing values, encode categoricals).

- `--history`  
  Display recent data quality runs stored in SQLite.

- `--worst [N]`  
  Show top N datasets with the lowest quality scores (default: 5).


  ## What I Learned

- **Designing Modular Data Pipelines**  
  Learned how to structure a data processing system into independent components (ingestion, validation, analysis, scoring, storage) to improve maintainability and extensibility.

- **Building CLI-Driven Data Tools**  
  Implemented argument-based workflows (`--clean`, `--history`, `--worst`) to control execution paths, similar to real-world data engineering tools.

- **Vectorized Computation with NumPy**  
  Replaced Pandas-based statistics with NumPy operations for better control and performance in statistical analysis.

- **Data Quality as a Quantifiable Metric**  
  Developed a scoring mechanism to evaluate datasets based on null values, schema consistency, and structure.

- **Persistent Tracking with SQLite**  
  Learned how to store and query historical data quality runs, enabling trend analysis and auditing.

- **Error Handling in Data Pipelines**  
  Implemented structured exception handling to manage file errors, parsing issues, and schema mismatches predictably.

- **Testing Data Workflows with Pytest**  
  Wrote unit tests for ingestion and validation logic, covering edge cases like missing files and empty datasets.

- **Balancing Flexibility and Simplicity**  
  Designed optional preprocessing pipelines while keeping the core system simple and modular.