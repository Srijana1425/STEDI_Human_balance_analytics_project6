# 🚀 STEDI-Human-Balance-Analytics
## Project Overview
This project involves processing and analyzing data from the STEDI Step Trainer, which includes Customer Records, Step Trainer Records, and Accelerometer Records. The goal is to create a data pipeline using AWS Glue, AWS S3, and Athena to transform and sanitize the data for further analysis.

## Data Sources
# 📂 Customer Records
Data from the fulfillment and the STEDI website.

Fields: 

- serialnumber

- sharewithpublicasofdate

- birthday

- registrationdate

- sharewithresearchasofdate

- customername

- email

- lastupdatedate

- phone

- sharewithfriendsasofdate

# 📉 Step Trainer Records
Data from the motion sensor.

Fields: 

- sensorReadingTime 

- serialNumber 

- distanceFromObject

# 📱 Accelerometer Records
Data from the mobile app.

Fields: 

- timeStamp

- user

- x 

- y

## Project Requirements
# 🚀 Landing Zones:

Create S3 directories: customer_landing, step_trainer_landing, accelerometer_landing.

Copy the data to these directories.

# 📊 Create Glue Tables:

customer_landing.sql

accelerometer_landing.sql

step_trainer_landing.sql

Query these tables using Athena and take screenshots.

# 🛠️ Glue Jobs:

- # Sanitize Customer Data:

Create a Glue Table customer_trusted for customers who agreed to share their data for research.

- # Sanitize Accelerometer Data:

Create a Glue Table accelerometer_trusted for readings from customers who agreed to share their data for research.

Verify and Query the Glue tables using Athena and take screenshots.

🚨 Data Quality Issue:

Create a Glue Job to sanitize the Customer data and create a Glue Table customers_curated for customers who have accelerometer data and agreed to share their data for research.

🎛️ Glue Studio Jobs:

Read the Step Trainer IoT data stream and populate a Trusted Zone Glue Table step_trainer_trusted.

Create an aggregated table machine_learning_curated with Step Trainer Readings and associated accelerometer data for the same timestamp for customers who agreed to share their data.

## Data Validation
Ensure the row count in each produced table is correct:

- # 📥 Landing:

Customer: 956

Accelerometer: 81273

Step Trainer: 28680

- # 📊 Trusted:

Customer: 482

Accelerometer: 40981

Step Trainer: 14460

- # 📑 Curated:

Customer: 482

Machine Learning: 43681


## Conclusion
This project demonstrates the creation of a data pipeline using AWS Glue and other AWS services to transform and sanitize data for further analysis. The final output is an aggregated table ready for machine learning analysis.
