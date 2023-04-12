from shape import LShape
class Board:
    def __init__(self):

        self.curBlock = LShape(0)
        self.board = [[0] * 20 for _ in range(15)]
        
    # try to move the shape down
    def try_move_down(self):
        self.curBlock.moveDown()
        if (not self.checkValid(self.curBlock)):
            self.curBlock.moveUp()
            return False
        return True
    # try to move the shape to the left
    def try_move_left(self):
        self.curBlock.moveLeft()
        if (not self.checkValid(self.curBlock)):
            self.curBlock.moveRight()
            return False
        return
    # try to move the shape to the right
    def try_move_right(self):
        self.curBlock.moveRight()
        if (not self.checkValid(self.curBlock)):
            self.curBlock.moveLeft()
            return False
        return 
    # try to rotate the shape to left
    def try_rotate_left(self):
        self.curBlock.rotateLeft()
        if (not self.checkValid(self.curBlock)):
            self.curBlock.rotateRight()
            return False
        return True

    # try to rotate the shape to the right
    def try_rotate_right(self):
        self.curBlock.rotateRight()
        if (not self.checkValid(self.curBlock)):
            self.curBlock.rotateLeft()
            return False
        return True
    
    # check if the shape is valid for 
    def checkValid(self, shape : LShape) -> bool:
        for i in range(4):
            for j in range(4):

                if (shape.x + i >= 15 or shape.y + j >= 20 or shape.y + j < 0) and shape.getShape()[i][j]:
                    return False
                if (shape.x + i >= 15 or shape.y + j >= 20 or shape.y + j < 0):
                    continue
                if shape.getShape()[i][j] and self.board[shape.x + i][shape.y + j]:
                    return False
        return True
    
    # dump a shape in to the board
    def dump(self):
        for i in range(4):
            for j in range(4):
                if self.curBlock.getShape()[i][j] and self.board[self.curBlock.x + i][self.curBlock.y + j] == 0:
                    self.board[self.curBlock.x + i][self.curBlock.y + j] = 1
        return 

    
    # generate a new block
    def newBlock(self):
        self.curBlock = LShape(0)
    
    # check if a row is full
    def checkRowFull(self, rowNum):
        for i in self.board[rowNum]:
            if i == 0:
                return False
        return True
    # check if a row is empty
    def checkExist(self, rowNum):
        for i in self.board[rowNum]:
            if i == 1:
                return True
        return False

    # delete a row from the board
    def deleteRow(self, rowNum):
        for i in range(rowNum, 0, -1):
            self.board[i] = self.board[i - 1][:]
        self.board[0] = [0] * 20
        return

    # return board
    def getBoard(self):
        tmp = []
        for i in self.board:
            tmp.append(i[:])
        for i in range(4):
            for j in range(4):
                if (self.curBlock.x + i < 15 and self.curBlock.y + j < 20 and self.curBlock.y + j >= 0):
                    tmp[self.curBlock.x + i][self.curBlock.y + j] = self.curBlock.getShape()[i][j]
        return tmp

    

