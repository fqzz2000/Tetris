from game import Game
import pygame
from pygame.locals import *
def main():
    game = Game()
    game.board.newBlock()
    game.step()

if __name__ == "__main__":
    main()
    num = 0
    done = False
    while not done:
        print(num)
        num += 1

        if key := pygame.key.get_pressed():
            print("you pressed",key,"so now i will quit")
            done = True