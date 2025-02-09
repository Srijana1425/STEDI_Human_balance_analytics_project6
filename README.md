# 🚀 STEDI-Human-Balance-Analytics
## Project Overview
This project involves processing and analyzing data from the STEDI Step Trainer, which includes Customer Records, Step Trainer Records, and Accelerometer Records. The goal is to create a data pipeline using AWS Glue, AWS S3, and Athena to transform and sanitize the data for further analysis.

## Project Data
STEDI has three JSON data sources

[customer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/customer/landing)

[accelerometer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/accelerometer/landing)

[step_trainer](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/step_trainer/landing)







# Data Sources
### 📂 Customer Records
Data from the fulfillment and the STEDI website.[customer data](https://github.com/Srijana1425/STEDI_Human_balance_analytics_project6/tree/main/myproject-files/customer/landing)

Fields: 

- `serialnumber`

- `sharewithpublicasofdate`

- `birthday`

- `registrationdate`

- `sharewithresearchasofdate`

- `customername`

- `email`

- `lastupdatedate`

- `phone`

- `sharewithfriendsasofdate`

### 📉 Step Trainer Records
Data from the motion sensor.

Fields: 

- `sensorReadingTime` 

- `serialNumber` 

- `distanceFromObject`

### 📱 Accelerometer Records
Data from the mobile app.

Fields: 

- `timeStamp`

- `user`

- `x` 

- `y`


