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