from pyspark.sql import SparkSession

class Parser:
    def __init__(self):
        self.spark = SparkSession \
            .builder \
            .appName("Python Spark SQL basic example") \
            .config("spark.some.config.option", "some-value") \
            .getOrCreate()
        pass

class CSVParser(Parser):
    def __init__(self, filename, delimeter):
        super().__init__()
        self.spark.read.option("delimeter", delimeter).option("header", True).csv(filename)