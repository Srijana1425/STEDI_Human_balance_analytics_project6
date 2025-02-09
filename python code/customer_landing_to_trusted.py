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

# Script generated for node customer landing
customerlanding_node1739000726462 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="customer_landingzone", transformation_ctx="customerlanding_node1739000726462")

# Script generated for node share with researched
SqlQuery667 = '''
select * from myDataSource
where sharewithresearchasofdate is not null
'''
sharewithresearched_node1739000759086 = sparkSqlQuery(glueContext, query = SqlQuery667, mapping = {"myDataSource":customerlanding_node1739000726462}, transformation_ctx = "sharewithresearched_node1739000759086")

# Script generated for node customer trusted
EvaluateDataQuality().process_rows(frame=sharewithresearched_node1739000759086, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739000501606", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
customertrusted_node1739000818938 = glueContext.getSink(path="s3://myproject-files/trusted_Zone/customer_trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], compression="snappy", enableUpdateCatalog=True, transformation_ctx="customertrusted_node1739000818938")
customertrusted_node1739000818938.setCatalogInfo(catalogDatabase="project_database",catalogTableName="customer_trusted_zone")
customertrusted_node1739000818938.setFormat("json")
customertrusted_node1739000818938.writeFrame(sharewithresearched_node1739000759086)
job.commit()