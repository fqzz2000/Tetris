from board import Board
from KBHit import KBHit
class Game:
    def __init__(self, delay = 100000):
        self.board = Board()
        self.kb = KBHit()
        self.delay = delay


    def run(self):
        while (not self.checkLose()):
            self.step()
            self.updateBoard()
        return
    
    def step(self):
        self.board.newBlock()
        while self.board.try_move_down():
            self.display()
            for _ in range(self.delay):
                if (self.kb.kbhit()):
                    c = self.kb.getch()
                    if (c == " "):
                        self.board.try_rotate_left()
                    elif (c == "a"):
                        self.board.try_move_left()
                    elif (c == "d"):
                        self.board.try_move_right()
                    self.display()

        self.board.dump()
        self.display()


    def updateBoard(self):
        for i in range(15):
            if (self.board.checkRowFull(i)):
                self.board.deleteRow(i)
        return

    def checkLose(self):
        return self.board.checkExist(2)
    
    def display(self):
        s = "#" * 22 + "\n"
        tmp = self.board.getBoard()[:]

        for i in range(len(tmp)):
            s += "#"
            for j in range(len(tmp[i])):
                if (tmp[i][j] == 1):
                    s += "*"
                else:
                    s += " "
            s += "#\n"
        s += "#" * 22 + "\n"
        print(s)
        