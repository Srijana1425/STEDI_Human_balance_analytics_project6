# 🚀 STEDI-Human-Balance-Analytics
## Project Overview
This project involves processing and analyzing data from the STEDI Step Trainer, which includes Customer Records, Step Trainer Records, and Accelerometer Records. The goal is to create a data pipeline using AWS Glue, AWS S3, and Athena to transform and sanitize the data for further analysis.

## Project Data
STEDI has three JSON data sources

[customer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/customer/landing)

[accelerometer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/accelerometer/landing)

[step_trainer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/step_trainer/landing)










## Check your work!
After each stage of your project, check if the row count in the produced table is correct. You should have the following number of rows in each table:

# Landing

- `Customer: 956`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/Customer_landing_zone.png)

Accelerometer: 81273

![]()

Step Trainer: 28680

![]()

# Trusted

Customer: 482

![]()

Accelerometer: 40981

![]()

Step Trainer: 14460

![]()

# Curated

Customer: 482

![]()

Machine Learning: 43681

![]()
