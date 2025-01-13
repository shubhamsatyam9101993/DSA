from property_reader import PropertyReader
from consume import Consume
from pyspark.sql import SparkSession, DataFrame
from schema_agreement import *


class MainModule:

    def __init__(self):
        self.spark = SparkSession.builder.getOrCreate()
        self._consume_obj = Consume(self.spark)

    def do(self):
        property_file = '/Users/shubhamsatyam/Downloads/projects/DSA/src/test.conf'
        prop = PropertyReader(property_file)
        section_name = 'COMMON_SECTION'
        path_name = prop.get_property(section_name, 'path')
        df = self._consume_table(path_name)
        df.show(truncate=False)

    def _consume_table(self, path_name) -> DataFrame:
        return self._consume_obj.do(path_name, schema_agreement, "1 == 1")


if __name__ == "__main__":
    MainModule().do()
