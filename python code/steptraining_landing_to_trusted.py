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

# Script generated for node customer curated
customercurated_node1739015084833 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="customer_curated", transformation_ctx="customercurated_node1739015084833")

# Script generated for node step trainer landing
steptrainerlanding_node1739015110171 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="step_trainer", transformation_ctx="steptrainerlanding_node1739015110171")

# Script generated for node SQL Query
SqlQuery796 = '''
select Step_Tainer.* from Step_Tainer
inner join Customer_Curated
on Step_Tainer.serialnumber = Customer_Curated.serialnumber;
'''
SQLQuery_node1739018314639 = sparkSqlQuery(glueContext, query = SqlQuery796, mapping = {"Customer_Curated":customercurated_node1739015084833, "Step_Tainer":steptrainerlanding_node1739015110171}, transformation_ctx = "SQLQuery_node1739018314639")

# Script generated for node Step trainer trusted
EvaluateDataQuality().process_rows(frame=SQLQuery_node1739018314639, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739017461289", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Steptrainertrusted_node1739018813783 = glueContext.getSink(path="s3://myproject-files/trusted_Zone/steptrainer_trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="Steptrainertrusted_node1739018813783")
Steptrainertrusted_node1739018813783.setCatalogInfo(catalogDatabase="project_database",catalogTableName="step_tariner_trusted")
Steptrainertrusted_node1739018813783.setFormat("json")
Steptrainertrusted_node1739018813783.writeFrame(SQLQuery_node1739018314639)
job.commit()