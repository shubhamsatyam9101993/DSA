
from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.getOrCreate()

transaction_schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("transaction_type", StringType(), True),
    StructField("transaction_amount", FloatType(), True)
])

transactions_data = [
    (1, "credit", 30.0),
    (1, "debit", 90.0),
    (2, "credit", 50.0),
    (3, "debit", 57.0),
    (2, "debit", 90.0)
]

transactions_df = spark.createDataFrame(transactions_data, schema=transaction_schema)

transactions_df.show()

amount_schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("current_amount", FloatType(), True)
])

amounts_data = [
    (1, 1000.0),
    (2, 2000.0),
    (3, 3000.0),
    (4, 4000.0)
]

amounts_df = spark.createDataFrame(amounts_data, schema=amount_schema)
