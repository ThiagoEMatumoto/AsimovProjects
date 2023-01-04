import time 
import random
import os
from schema import *
from jankenpon import *

def main():
    welcome()
    name = input("User name: ")
    os.system('clear')
    
    game = jankenpon(name)
    scoreboard(game.name, game.player_points, game.computer_points)
    
    
if __name__ == "__main__":
    main()
