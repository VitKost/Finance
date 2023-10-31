import pandas

class Parser:
    def __init__(self):
        pass

class CSVParser(Parser):
    def __init__(self, filename):
        super().__init__()
        self.data = pandas.read_csv(filename)