import time 
import os
from schema import *
from jankenpon import *

def main():
    welcome()
    name = input("User name: ")
    os.system('clear')
    
    game = jankenpon(name)
    scoreboard(game.name, game.player_points, game.computer_points)
    
    
    try:
        make_your_choice(game.choices)
        user_choice = int(input())
    except Exception as erro:
        print(erro)
        time.sleep(3)
        os.system('clear')
        
    game.compare_choices(user_choice)
    
if __name__ == "__main__":
    main()
