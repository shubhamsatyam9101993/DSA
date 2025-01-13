

from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.getOrCreate()
columns = ['msc_id', 'cntry', 'mach_cd_id', 'uom_id', 'from_size', 'to_size']
data = [(57971, 36010001, 107, 30,	5.0000, 5.0000),
        (57972, 36010001, 107, 30,	6.0000, 6.0000),
        (57973, 36010001, 107, 30,	7.0000, 7.0000),
        (57974, 36010001, 107, 30,	8.0000, 8.0000),
        (57975, 36010001, 107, 30,	9.0000, 9.0000),
        (57976, 36010001,	107, 30, 10.0000, 10.0000),
        (57977,	36010001,	107, 30,	11.0000, 11.0000)]


df = spark.createDataFrame(data, columns)


sch = ['size_id', 'Month', 'Model', 'Units_sold', 'Manufacturer', 'JD - Product Category', 'Equipment',
       'Class', 'Equipment-class', 'Class group', 'Configuration', 'Customer_code', 'JD-C&F - Sales Zone	datas']
dt = [(107, '2024-05', 150, 'AWD', 1, 'CATERPILLAR', 'Motor Grader', 'MG', 10, 'MG10: 161-195kW', 'N/A', 'N/A',
       '100C&F Vic 214'),
      (107, '2024-05', 150, 'AWD', 1, 'CATERPILLAR', 'Motor Grader', 'MG', 4, 'MG10: 161-195kW', 'N/A', 'N/A',
       '100C&F Vic 214')]


file_df = spark.createDataFrame(dt, sch)


df.show(truncate=False)


file_df.show(truncate=False)
