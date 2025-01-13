from pyspark.sql.functions import DataFrame


class Consume:

    def __init__(self, spark):
        self._spark = spark

    def do(self, path, agreement, filter_cond) -> DataFrame:
        df = (self._spark.read.option("header", True).csv(path)
              .filter(filter_cond)
              .select(*agreement.names))
        return df
