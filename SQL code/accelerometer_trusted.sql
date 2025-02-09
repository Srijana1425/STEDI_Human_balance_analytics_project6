CREATE EXTERNAL TABLE `accelerometer_trusted`(
  `user` string, 
  `timestamp` bigint, 
  `x` double, 
  `y` double, 
  `z` double)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://myproject-files/trusted_Zone/accelerometer_trusted/'
TBLPROPERTIES (
  'CrawlerSchemaDeserializerVersion'='1.0', 
  'CrawlerSchemaSerializerVersion'='1.0', 
  'UPDATED_BY_CRAWLER'='accelerometer_trustedZone', 
  'averageRecordSize'='5', 
  'classification'='parquet', 
  'compressionType'='none', 
  'objectCount'='36', 
  'recordCount'='40981', 
  'sizeKey'='194245', 
  'typeOfData'='file')