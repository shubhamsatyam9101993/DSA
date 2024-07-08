import unittest
from pyspark.sql import SparkSession


class FacadeFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.getOrCreate()
        cls.data_set = cls.data_set()

    @classmethod
    def data_set(cls):
        return cls.spark.createDataFrame(data=[("Shubham", "Satyam"),
                                         ("Urvashi", "Nayak")], schema=["name", "title"])

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()
