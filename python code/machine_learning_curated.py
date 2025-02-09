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

# Script generated for node Step trainer trusted
Steptrainertrusted_node1739022512083 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="steptrainer_trusted", transformation_ctx="Steptrainertrusted_node1739022512083")

# Script generated for node accelerometer trusted
accelerometertrusted_node1739022485296 = glueContext.create_dynamic_frame.from_catalog(database="project_database", table_name="accelerometer_trusted", transformation_ctx="accelerometertrusted_node1739022485296")

# Script generated for node SQL Query
SqlQuery561 = '''
select steptrainer_trusted.sensorreadingtime,steptrainer_trusted.serialnumber,
steptrainer_trusted.distancefromobject,accelerometer_trusted.user,accelerometer_trusted.x,
accelerometer_trusted.y,accelerometer_trusted.z
from steptrainer_trusted
inner join accelerometer_trusted
on accelerometer_trusted.timestamp=steptrainer_trusted.sensorreadingtime;
'''
SQLQuery_node1739022553513 = sparkSqlQuery(glueContext, query = SqlQuery561, mapping = {"steptrainer_trusted":Steptrainertrusted_node1739022512083, "accelerometer_trusted":accelerometertrusted_node1739022485296}, transformation_ctx = "SQLQuery_node1739022553513")

# Script generated for node machine learning curated.
EvaluateDataQuality().process_rows(frame=SQLQuery_node1739022553513, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1739022403658", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
machinelearningcurated_node1739022836232 = glueContext.getSink(path="s3://myproject-files/Curated/machine_learning_curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="machinelearningcurated_node1739022836232")
machinelearningcurated_node1739022836232.setCatalogInfo(catalogDatabase="project_database",catalogTableName="machine_learning")
machinelearningcurated_node1739022836232.setFormat("json")
machinelearningcurated_node1739022836232.writeFrame(SQLQuery_node1739022553513)
job.commit()