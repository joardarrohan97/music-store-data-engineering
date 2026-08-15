# Music Store Data Engineering Project

An end-to-end data engineering project built using the Music Store
database.

## Current Architecture

PostgreSQL
    ↓
Python
    ↓
Extract
    ↓
Transform
    ↓
Load
    ↓
Data Validation
    ↓
PostgreSQL

## Technologies

- PostgreSQL
- pgAdmin 4
- Python
- Pandas
- Psycopg
- SQLAlchemy
- python-dotenv
- Git

## Current ETL Pipeline

The pipeline extracts customer data from the PostgreSQL Music Store
database, transforms the data using Pandas, loads the transformed
data into a new PostgreSQL table, and validates the loaded records.

### Extract

Source table:

`customer`

### Transformations

- Remove leading and trailing whitespace
- Convert email addresses to lowercase
- Remove duplicate records

### Load

Target table:

`customer_clean`

### Validation

The pipeline validates that the number of records loaded into the
target table matches the number of transformed records.

## Project Structure

```text
Music Store Project/
│
├── Python/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── test_connection.py
│
├── SQL/
├── Airflow/
├── dbt/
├── Docker/
├── Data/
├── Notebooks/
│
├── Documentation/
│   └── logs/
│
├── .gitignore
├── requirements.txt
└── README.md