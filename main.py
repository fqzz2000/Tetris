from game import Game
def main():
    game = Game()
    game.board.newBlock()
    game.step()

if __name__ == "__main__":
    main()