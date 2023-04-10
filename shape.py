class LShape:
    def __init__(self, cur):
        self.coordinates = \
        [[[0, 1, 0, 0], 
         [0, 1, 0, 0],
         [0, 1, 0, 0],
         [0, 1, 1, 0]],
         [[0, 0, 0, 0],
          [0, 0, 0, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]]
        self.cur = cur

    def rotateLeft(self):
        self.cur = (self.cur + 1) % len(self.coordinates)

    def rotateRight(self):
        self.cur = (self.cur + len(self.coordinates) - 1) % len(self.coordinates)

    def getShape(self):
        return self.coordinates[self.cur][:]