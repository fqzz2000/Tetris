from board import Board
class Game:
    def __init__(self):
        self.board = Board()


    def run(self):
        return
    
    def step(self):
        while self.board.checkValid(self.board.current_x + 1, self.board.current_y, self.board.curBlock):
            self.board.move_down()
            self.display()
        self.board.dump()
        self.display()
        

    
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
        