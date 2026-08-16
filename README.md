# 🎵 Music Store Data Engineering Project


An end-to-end data engineering project built around the Chinook/Music Store database.


The project demonstrates how to build, transform, validate, containerize, and orchestrate a data pipeline using PostgreSQL, Python, Docker, and Docker Compose.


---


## 🚀 Project Overview


This project starts with a PostgreSQL Music Store database and builds a complete ETL pipeline.


The current pipeline:


1. Extracts customer data from PostgreSQL
2. Transforms the data using Pandas
3. Loads the transformed data into a clean target table
4. Validates the loaded data
5. Logs pipeline execution
6. Runs inside Docker
7. Uses Docker Compose to manage PostgreSQL and the ETL service


---


## 🏗️ Current Architecture


```text
                 Docker Compose
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      PostgreSQL             Python ETL
       Container             Container
             │                   │
             │◄──────────────────┘
             │
             ▼
      music_store_analysis
             │
             ▼
       customer_clean
ETL Flow
PostgreSQL
    │
    ▼
Extract
    │
    ▼
Transform
    │
    ▼
Load
    │
    ▼
Validation
    │
    ▼
PostgreSQL
🛠️ Technologies Used
Technology	Purpose
PostgreSQL	Source and target database
Python	ETL development
Pandas	Data transformation
Psycopg	PostgreSQL connectivity
SQLAlchemy	Database connection and interaction
Docker	Containerization
Docker Compose	Multi-container environment
Git	Version control
GitHub	Source code management
📁 Project Structure
Music Store Project/
│
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── README.md
├── requirements.txt
│
├── Docker/
│   └── Dockerfile
│
├── Documentation/
│   ├── music_store_data_engineering_roadmap.txt
│   └── logs/
│       └── etl_pipeline.log
│
├── Python/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── test_connection.py
│   └── venv/
│
├── Data/
│   └── backups/
│
└── SQL/

.env, the Python virtual environment, database backups, cache files, and other local files are excluded from Git using .gitignore and .dockerignore.

🐍 Python ETL Pipeline

The ETL pipeline is divided into three major stages.

1. Extract

The extraction process connects to PostgreSQL and retrieves customer data.

PostgreSQL
     ↓
customer table
     ↓
Pandas DataFrame

Current extraction result:

Rows extracted: 59
Columns: 13
2. Transform

The transformation step cleans and prepares the extracted data using Pandas.

Raw Data
   ↓
Data Cleaning
   ↓
Data Transformation
   ↓
Clean Data
3. Load

The transformed data is loaded into:

customer_clean

Current result:

Rows loaded: 59
4. Validation

The pipeline validates the target table after loading.

Example:

Validation successful
Rows in customer_clean: 59
🐳 Docker

The ETL application is containerized using Docker.

The Docker image contains:

Python 3.14
Pandas
Psycopg
SQLAlchemy
ETL source code

Build the image:

docker build -f Docker/Dockerfile -t music-store-etl .

Run the ETL container:

docker run --rm \
  --env-file .env \
  -e DB_HOST=host.docker.internal \
  music-store-etl
🐳 Docker Compose

Docker Compose manages the PostgreSQL database and ETL service.

Start PostgreSQL:

docker compose up -d postgres

Check services:

docker compose ps

Run the complete ETL service:

docker compose run --rm etl

View ETL logs:

docker compose logs etl

Stop the services:

docker compose down
🗄️ PostgreSQL

The Docker PostgreSQL service exposes:

Host: localhost
Port: 5433
Database: music_store_analysis
Username: musicstore

Inside the Docker Compose network, the ETL connects to PostgreSQL using:

Host: postgres
Port: 5432

This is possible because Docker Compose provides service-to-service networking.

📊 Database

The Music Store database currently contains 12 tables:

album
artist
customer
customer_clean
employee
genre
invoice
invoice_line
media_type
playlist
playlist_track
track

Example data volumes:

Customers: 59
Tracks:    3503
Invoices:  614
🔐 Environment Variables

Database credentials are stored locally in:

.env

Example:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=music_store_analysis
DB_USER=rohanjoardar
DB_PASSWORD=your_password

The .env file is intentionally excluded from GitHub.

For Docker Compose, database configuration is provided through the Compose environment.

Never commit passwords, API keys, tokens, or other credentials to GitHub.

🧪 Running the Project Locally

Activate the Python virtual environment:

source Python/venv/bin/activate

Run the connection test:

python Python/test_connection.py

Run the ETL pipeline:

python Python/load.py

Expected output:

========== ETL PIPELINE STARTED ==========


✅ Data extracted
Rows extracted: 59


✅ Data transformed
Rows after transformation: 59


✅ Data loaded successfully!
Target table: customer_clean


✅ Validation successful!
Rows in customer_clean: 59


========== ETL PIPELINE COMPLETED ==========
📝 Logging

Pipeline execution is logged for monitoring and debugging.

The project maintains:

Documentation/logs/etl_pipeline.log

Example:

INFO - Starting extraction
INFO - Starting transformation
INFO - Starting load
INFO - Loaded 59 rows into customer_clean
INFO - Validation successful: 59 rows
INFO - ETL PIPELINE COMPLETED

When running inside Docker, logs are also available through Docker:

docker compose logs etl
🔄 Data Engineering Roadmap

The project will gradually evolve into a larger production-style data engineering platform.

Completed
 PostgreSQL
 SQL analysis
 Python
 Pandas
 ETL pipeline
 Data transformation
 Data validation
 Logging
 Environment configuration
 Git
 GitHub
 Docker
 Docker Compose
 PostgreSQL containerization
 Multi-container ETL pipeline
Planned
 Apache Airflow
 Airflow DAG
 Pipeline scheduling
 Pipeline monitoring
 dbt
 AWS S3
 Snowflake
 PySpark
 Apache Kafka
 Data warehouse architecture
 Data quality framework
 CI/CD
 Power BI dashboard
🎯 Project Goal

The goal of this project is to build practical data engineering skills by progressively transforming a simple PostgreSQL database into a production-style data platform.

The final architecture will evolve toward:

                Apache Airflow
                      │
                      ▼
                 ETL Pipeline
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      PostgreSQL                 AWS S3
          │                       │
          └───────────┬───────────┘
                      ▼
                  Snowflake
                      │
                      ▼
                    dbt
                      │
                      ▼
                Data Warehouse
                      │
                      ▼
                  Power BI
👨‍💻 Author

Rohan Joardar

This project is being developed as a practical data engineering portfolio project covering SQL, Python, ETL, Docker, orchestration, cloud platforms, data warehousing, and analytics.



Save it with:


**⌘ + S**


Then close TextEdit.


---


## Step 41 — Check the README


Back in Terminal run:


```bash
head -30 README.md

You should see:

# 🎵 Music Store Data Engineering Project

Then check Git:

git status

You should see README.md as modified.

Don't commit yet

Send me the output of:

git status

Then we'll review the changes and commit the updated README together.