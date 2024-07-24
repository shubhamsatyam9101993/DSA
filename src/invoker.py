from pyspark.sql import SparkSession, DataFrame
import logging
import configparser as cp
from datetime import datetime


class Invoker:

    def __init__(self):
        self.config_parser = cp.ConfigParser()
        self.config_parser.optionxform = str
        self.config_parser.read(
            '/Users/shubhamsatyam/Downloads/projects/DSA/project.properties')
        self._input_path = self.config_parser.get(
            'COMMON_SECTION', 'input_path')
        self._output_path = self.config_parser.get(
            'COMMON_SECTION', 'output_path')
        self._timestamp_path = self.config_parser.get(
            'COMMON_SECTION', 'timestamp_path')
        self._spark = None

    def __enter__(self):
        self._spark = SparkSession.builder.getOrCreate()
        logging.info("Spark Session created")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._spark.sparkContext.stop()

    def read_csv(self) -> DataFrame:
        df = self._spark.read.option("header", "True").csv(self._input_path)
        return df

    def write_df(self, df: DataFrame) -> None:
        df.repartition(1).write.format("csv").mode(
            'overwrite').save(self._output_path)
        self.write_current_timestamp()

    def do(self) -> None:
        df = self.read_csv()
        self.write_df(df)

    def read_last_timestamp(self, path):
        return self._spark.read.option("header", "False").csv(path).collect()[0][0]

    def write_current_timestamp(self) -> None:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        df = self._spark.createDataFrame([(timestamp,)], ["timestamp"])
        df.repartition(1).write.format("csv").mode(
            'overwrite').save(self._timestamp_path)


if __name__ == '__main__':
    with Invoker() as inv:
        inv.do()
