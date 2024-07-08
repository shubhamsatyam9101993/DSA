from pyspark.sql import SparkSession, DataFrame
from pathlib import Path
import logging


class Invoker:

    def __init__(self):
        self._spark = None
        self.path = str(Path().absolute()).split("src")[0]+"/hello.csv"

    def __enter__(self):
        self._spark = SparkSession.builder.getOrCreate()
        logging.info("Spark Session created")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._spark.sparkContext.stop()

    def read_csv(self) -> DataFrame:
        df = self._spark.read.option("header", "True").csv(self.path)
        return df

    def write_df(self, df: DataFrame) -> None:
        df.repartition(1).write.format("csv").save(self.path.split("hello.csv")[0]+"op")

    def do(self) -> None:
        df = self.read_csv()
        self.write_df(df)


if __name__ == '__main__':
    with Invoker() as inv:
        inv.do()
