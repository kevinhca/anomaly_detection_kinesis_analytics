# Anomaly Detection with Amazon Amazon Kinesis Analytics

#Code:
### 1. connected_turbine_ingest_into_firehose.py - simulation code that ingests randomly generated telemetry and anomalies into Kinesis Firehose.
### 2. kinesis_analytics_app_for_anomaly_detection.sql - contains the SQL code for kinesis analytics application


# Steps 

### 1. Create two S3 Buckets -  raw data and another one for data with anomalies score.

### 2. Create two Kinesis Firehose Streams – one for Raw Data Ingestion and second for the output from Kinesis Analytics App

### 3. Create Kinesis Analytics App – using in-built template for Anomaly detection.

### 4. Create Glue Crawler to crawl the schema from S3 Bucket. 

### 5. Use Athena to query Data from Table definition

### 6. Build visual charts in QuickSight with Athena as a source. 
