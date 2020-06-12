class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        if len(self.data) != self.capacity:
            self.data.append(item)

    def get(self):
        pass