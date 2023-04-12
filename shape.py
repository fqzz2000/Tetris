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
        self.x = 0
        self.y = 0

    def moveUp(self):
        self.x -= 1
        
    def moveDown(self):
        self.x += 1

    def moveLeft(self):
        self.y -= 1

    def moveRight(self):
        self.y += 1

    def rotateLeft(self):
        self.cur = (self.cur + 1) % len(self.coordinates)

    def rotateRight(self):
        self.cur = (self.cur + len(self.coordinates) - 1) % len(self.coordinates)

    def getShape(self):
        return self.coordinates[self.cur][:]