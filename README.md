# Intelligent Data Quality Engine

## Overview
The Intelligent Data Quality Engine is a system designed to automatically detect data quality issues in CSV and JSON datasets.  
It identifies schema inconsistencies, missing values, and anomalies using statistical and machine learning techniques.

The system is designed with a modular architecture and will evolve into a REST API for real-time data quality analysis.

---

## Problem Statement
In real-world data pipelines, datasets often contain:
- Missing or null values
- Incorrect data types
- Schema mismatches
- Outliers and anomalies

These issues can lead to incorrect analysis and poor model performance.

This project aims to build a system that can **automatically analyze datasets and generate a structured data quality report**.

---

## Input / Output

### Input
- CSV files
- JSON files

### Output
- Structured data quality report (JSON format)
- Summary of:
  - Missing values
  - Data types
  - Schema issues
  - Statistical insights
  - Data quality score (future)

---

## System Flow
File → Ingestion → Validation → Analysis → Scoring → Reporting


### Flow Description
1. **Ingestion**
   - Load CSV/JSON data safely

2. **Validation**
   - Check schema consistency
   - Validate column presence and data types

3. **Analysis**
   - Compute statistics
   - Detect null values and anomalies

4. **Scoring**
   - Assign data quality scores (planned)

5. **Reporting**
   - Generate structured output (CLI / JSON / HTML)

---

## Project Structure
data_quality_engine/
│
├── src/
│ ├── ingestion/
│ │ └── loader.py
│ │
│ ├── validation/
│ │ └── validator.py
│ │
│ ├── analysis/
│ │ ├── analyzer.py
│ │ └── scorer.py
│ │
│ ├── reporting/
│ │ └── reporter.py
│ │
│ └── init.py
│
├── tests/ # Unit tests
├── data/ # Sample datasets
├── reports/ # Generated reports
├── notebooks/ # Exploration / experiments
│
├── main.py # CLI entry point
├── requirements.txt
├── README.md
└── .gitignore


---

## Technology Stack

- Python
- Pandas
- NumPy
- SQLite (for persistence)
- PyOD (for anomaly detection)
- FastAPI (for API layer - future)

---

## Future Enhancements

- ML-based anomaly detection (Isolation Forest, LOF)
- REST API for dataset upload and analysis
- HTML report generation
- Data quality dashboard (Streamlit)
- Historical tracking of dataset quality

---