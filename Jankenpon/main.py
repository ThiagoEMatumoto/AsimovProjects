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
    
    make_your_choice()
    user_choice = input()
    jankenpon.compare_choices(user_choice)
    
if __name__ == "__main__":
    main()
