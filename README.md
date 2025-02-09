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

- `Accelerometer: 81273`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/accelerometer_landing_zone.png)

- `Step Trainer: 28680`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/step_trainer_landing_zone.png)

# Trusted

- `Customer: 482`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/customer_trusted_zone.png)

- `Accelerometer: 40981`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/accelerometer_trusted_zone.png)

- `Step Trainer: 14460`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/step_trainer_trusted_zone.png)

# Curated

- `Customer: 482`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/customer_curated.png)

- `Machine Learning: 43681`

![](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/blob/main/screenshort/Athena%20Output/machine_learning_curated.png)
