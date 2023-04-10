from shape import LShape
class Board:
    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.board = [[0] * 20 for _ in range(15)]
        
    
    def move_down(self):
        if (self.current_x < 14):
            self.current_x += 1
        return

    def move_left(self):
        if (self.current_y >= 1):
            self.current_y -= 1
        return
    
    def move_right(self):
        if (self.current_y < 19):
            self.current_y += 1
        return 
    
    # check if the shape is valid for 
    def checkValid(self, x : int, y : int, shape : LShape) -> bool:
        for i in range(4):
            for j in range(4):
                if shape.getShape()[i][j] and (x + i >= 15 or y + i >= 20 or y + i < 0):
                    return False
                if shape.getShape()[i][j] and self.board[x + i][y + j]:
                    return False
        return True
    # dump a shape in to the board
    def dump(self):
        for i in range(4):
            for j in range(4):
                if self.curBlock.getShape()[i][j] and self.board[self.current_x + i][self.current_y + j] == 0:
                    self.board[self.current_x + i][self.current_y + j] = 1
        return 
    # generate a new block
    def newBlock(self):
        self.curBlock = LShape(0)
        self.current_x = 0
        self.current_y = 0

    # return board
    def getBoard(self):
        tmp = []
        for i in self.board:
            tmp.append(i[:])
        for i in range(4):
            for j in range(4):
                tmp[self.current_x + i][self.current_y + j] = self.curBlock.getShape()[i][j]
        return tmp

    

