from pyspark.sql.types import *

name = 'name'
title = 'title'

schema_agreement = StructType([StructField(name, StringType(), True),
                               StructField(title, StringType(), True)])

