# 🚀 STEDI-Human-Balance-Analytics
## Project Overview
This project involves processing and analyzing data from the STEDI Step Trainer, which includes Customer Records, Step Trainer Records, and Accelerometer Records. The goal is to create a data pipeline using AWS Glue, AWS S3, and Athena to transform and sanitize the data for further analysis.

## Project Environment
- Python and Spark
- AWS Glue
- AWS Athena
- AWS S3

## Project Data
STEDI has three JSON data sources

[customer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/customer/landing)

[accelerometer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/accelerometer/landing)

[step_trainer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/step_trainer/landing)

## Project Steps -

Here are the brief steps to follow on the AWS website to complete this project :

### Step 1: Set Up S3 Buckets

1. Log in to the [AWS Management Console](https://aws.amazon.com/).

2. Go to **S3** and create three buckets or folders within a bucket named `customer_landing_zone`, `step_trainer_landing_zone`, and `accelerometer_landing_zone`.

3. Upload your JSON data files to the respective folders.

### Step 2: Create Glue Tables for Landing Zones

1. Go to the **AWS Glue Console**.

2. Create a new **Database** (e.g., `project_database`).

3. Create a **Crawler** to catalog the data in the S3 folders and run the crawlers to create tables in your database.

### Step 3: Query Tables Using Athena

1. Go to the **AWS Athena Console**.

2. Select the database you created and run SQL queries to verify the data in the `customer_landing_zone`, `step_trainer_landing_zone`, and `accelerometer_landing_zone` tables.

3. Take screenshots of your query results.

### Step 4: Create AWS Glue Jobs
#### Glue Job 1: Customer Trusted Table

This job sanitizes the customer data and only includes records for customers who agreed to share their data for research.

1. Go to the **AWS Glue Console**.

2. Create a new **Job** with a Python script that filters customer records (see the provided script for `customer_trusted_zone`).

3. Run the job and verify it creates the `customer_trusted_zone` table.

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Visual%20ETL%20Image/customer_landing_to_trusted.png
)

#### Glue Job 2: Accelerometer Trusted Table

This job sanitizes the customer data and only includes records for accelerometer who agreed to share their data for research.

1. Create another **Job** for sanitizing accelerometer data (see the provided script for `accelerometer_trusted_zone`).

2. Run the job and verify it creates the `accelerometer_trusted_zone` table.

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Visual%20ETL%20Image/accelerometer_Landing_to_trustrd.png)

#### Glue Job 3: step-trainer Trusted Table

This job sanitizes the Step-Trainer Records data for customers who have accelerometer data and have agreed to share their data for research.

1. Create another **Job** for sanitizing step-trainer data (see the provided script for `step_trainer_trusted_zone`).

2. Run the job and verify it creates the `step_trainer_trusted_zone` table.

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Visual%20ETL%20Image/step_trainer_trusted.png
)
   
### Step 5: Create Curated Glue Table

This Glue job sanitize the customer data and includes only those with accelerometer data.

1. Create a new **Job** to curate customer data (see the provided script for `customers_curated`).

2. Run the job and verify it creates the `customers_curated` table.

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Visual%20ETL%20Image/customer%20curated.png)

### Step 6: Create Aggregated Glue Table

Create a Glue job to aggregate step trainer readings with accelerometer data for the same timestamp.

1. Create a final **Job** to aggregate Step Trainer readings with accelerometer data (see the provided script for `machine_learning_curated`).

2. Run the job and verify it creates the `machine_learning_curated` table.

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Visual%20ETL%20Image/machine_learning_curated.png)

### Step 7: Query the Resulting Tables

1. Go back to **Athena**.

2. Run SQL queries to verify the data in the `customer_trusted_zone` , `accelerometer_trusted_zone`,`step_trainer_trusted_zone` , `customers_curated`, and `machine_learning_curated` tables.

3. Take screenshots of your query results.**[*Here is my* [Athena output](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/screenshort/Athena%20Output)]**

Remember to monitor your AWS costs to stay within your budget.

## Check your work!
After each stage of your project, check if the row count in the produced table is correct. You should have the following number of rows in each table:

### Landing

- `Customer: 956`
  
- `Accelerometer: 81273`
  
- `Step Trainer: 28680`
  
### Trusted

- `Customer: 482`

- `Accelerometer: 40981`

- `Step Trainer: 14460`

### Curated

- `Customer: 482`

- `Machine Learning: 43681`

<hr>

## Project Files 📂

- ### 1. Project Data
- **Description**: Contains all three JSON data sources.
   - [customer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/customer/landing)

   - [accelerometer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/accelerometer/landing)

   - [step_trainer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/step_trainer/landing)

### 2. SQL Code
- **Description**: Contains all the SQL DDL scripts for landing, trusted, and curated zones.
  - [customer_landing.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/customer_landing.sql)
  - [accelerometer_landing.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/accelerometer_landing.sql)
  - [step_trainer_landing.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/step_trainer_landing.sql)
  - [customer_trusted.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/customer_trusted.sql)
  - [accelerometer_trusted.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/accelerometer_trusted.sql)
  - [step_trainer_trusted.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/step_trainer_trusted.sql)
  - [customers_curated.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/customers_curated.sql)
  - [machine_learning_curated.sql](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/SQL%20code/machine_learning_curated.sql)

### 3. Python Code
- **Description**: Contains all the Glue job Python scripts.
  - [customer_trusted.py](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/python%20code/customer_landing_to_trusted.py)
  - [accelerometer_trusted.py](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/python%20code/accelerometer_landing_to_trusted.py)
  - [step_trainer_trusted.py](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/python%20code/step_trainer_landing_to_trusted.py)
  - [customers_curated.py](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/python%20code/customers_curated.py)
  - [machine_learning_curated.py](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/python%20code/machine_learning_curated.py)

### 4. Screenshots : *Contains all the visual ETL and Athena outputs.*
  
