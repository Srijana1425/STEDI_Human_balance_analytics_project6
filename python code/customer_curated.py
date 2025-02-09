import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node customer trusted
customertrusted_node1739013899344 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="customer_trusted", transformation_ctx="customertrusted_node1739013899344")

# Script generated for node accelerometer landing
accelerometerlanding_node1739013871036 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="accelerometer", transformation_ctx="accelerometerlanding_node1739013871036")

# Script generated for node Drop field and Duplicates 
SqlQuery643 = '''
select distinct customer_trusted.*
from accelerometer_landing
inner join customer_trusted
on accelerometer_landing.user = customer_trusted.email

'''
DropfieldandDuplicates_node1739013932933 = sparkSqlQuery(glueContext, query = SqlQuery643, mapping = {"accelerometer_landing":accelerometerlanding_node1739013871036, "customer_trusted":customertrusted_node1739013899344}, transformation_ctx = "DropfieldandDuplicates_node1739013932933")

# Script generated for node customer curated
EvaluateDataQuality().process_rows(frame=DropfieldandDuplicates_node1739013932933, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739013858815", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
customercurated_node1739014069683 = glueContext.getSink(path="s3://myproject-files/Curated/customer_curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="customercurated_node1739014069683")
customercurated_node1739014069683.setCatalogInfo(catalogDatabase="project_database",catalogTableName="customer_curated")
customercurated_node1739014069683.setFormat("json")
customercurated_node1739014069683.writeFrame(DropfieldandDuplicates_node1739013932933)
job.commit()