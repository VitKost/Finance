class Pipeline:
    count = 0
    def __init__(self):
        self.count += 1

    def __del__(self):
        self.count -= 1

    