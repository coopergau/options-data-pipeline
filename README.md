# Options Chain Data Pipeline

## Table of Contents
- [Overview](#overview)
- [Architecture Summary](#architecture-summary)
- [Visuals](#visuals)

## Overview
Historical stock market data on normal assets is widely accessible for public use, while data on derivatives likes options is another story. For anything more than end of day or current options chain data, any member of the public usually has to pay. This purpose of this project is to create an automated data pipeline that periodically captures real-time options-chain data and stores it in a database, accumulating historical data that can be used for further analysis. This project is automated to save data at market close and once every hour that the market was open, though this can be adjusted in the airflow settings. One could easily set the pipeline to capture data at a much higher frequency; in this work, the script saves data on 16 different assets and takes about 20 seconds to run on average.

## Architecture Summary
### Data Collection
A Python script fetches real-time options-chain data from the yahoo finance API. The script transforms, cleans, and saves the data to a PostgreSQL database.
### Containerization
The Python script is packaged into a Docker image to ensure consistent execution across different environments.
### Orchestration
An AWS EC2 instance runs Apache Airflow in Docker to execute the data collection script according to the specified schedule.
### Storage
The data is stored in a PostgreSQL database hosted on AWS Relational Database Service (RDS).
### Analytics
Power BI connects directly to the RDS database to import and analyze the data.

## Visuals
### 1. 
<img src="images/threshold.PNG" width="600" />
### 2. 
<img src="images/threshold.PNG" width="600" />
### 3. 
<img src="images/threshold.PNG" width="600" />
### 4.
<img src="images/threshold.PNG" width="600" />


