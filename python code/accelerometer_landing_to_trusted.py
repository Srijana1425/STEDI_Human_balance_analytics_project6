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
customertrusted_node1739011785477 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="customer_trusted", transformation_ctx="customertrusted_node1739011785477")

# Script generated for node accelerometer landing
accelerometerlanding_node1739011806838 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="accelerometer", transformation_ctx="accelerometerlanding_node1739011806838")

# Script generated for node Join
Join_node1739011829188 = Join.apply(frame1=customertrusted_node1739011785477, frame2=accelerometerlanding_node1739011806838, keys1=["email"], keys2=["user"], transformation_ctx="Join_node1739011829188")

# Script generated for node Drop fields
SqlQuery669 = '''
select user, timestamp, x, y, z
from myDataSource;


'''
Dropfields_node1739011849049 = sparkSqlQuery(glueContext, query = SqlQuery669, mapping = {"myDataSource":Join_node1739011829188}, transformation_ctx = "Dropfields_node1739011849049")

# Script generated for node accelerometer trusted
EvaluateDataQuality().process_rows(frame=Dropfields_node1739011849049, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739011777713", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
accelerometertrusted_node1739012171546 = glueContext.getSink(path="s3://myproject-files/trusted_Zone/accelerometer_trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="accelerometertrusted_node1739012171546")
accelerometertrusted_node1739012171546.setCatalogInfo(catalogDatabase="project_database",catalogTableName="accelerometer_trusted_Zone")
accelerometertrusted_node1739012171546.setFormat("glueparquet", compression="snappy")
accelerometertrusted_node1739012171546.writeFrame(Dropfields_node1739011849049)
job.commit()