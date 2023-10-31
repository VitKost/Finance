class Pipeline:
    count = 0
    def __init__(self):
        Pipeline.count += 1

    def __del__(self):
        Pipeline.count -= 1

