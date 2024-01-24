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
    def __init__(self):
        super().__init__()

    def parse_csv_file(self, filename, delimiter):
        self.message = self.spark.read.option("delimiter", delimiter).option("header", True).csv(filename)
        self.message = self.message.first().asDict()

    def get_message(self):
        return self.message