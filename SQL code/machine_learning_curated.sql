CREATE EXTERNAL TABLE `machine_learning`(
  `sensorreadingtime` bigint COMMENT 'from deserializer', 
  `serialnumber` string COMMENT 'from deserializer', 
  `distancefromobject` int COMMENT 'from deserializer', 
  `user` string COMMENT 'from deserializer', 
  `x` double COMMENT 'from deserializer', 
  `y` double COMMENT 'from deserializer', 
  `z` double COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://myproject-files/Curated/machine_learning_curated/'
TBLPROPERTIES (
  'CreatedByJob'='machine learning curated.', 
  'CreatedByJobRun'='jr_da16979ec1553a858653b41ba1837d92af54f8f42fb794a9e532d23ad98090ff', 
  'classification'='json')