import time 
import os
from schema import *
from jankenpon import *

def main():
    welcome()
    name = input("User name: ")
    os.system('clear')
    
    game = jankenpon(name)
    
    keep_playing =  True
    while keep_playing:
        scoreboard(game.name, game.player_points, game.computer_points)
        try:
            make_your_choice(game.choices)
            user_choice = int(input())
            
        except Exception as erro:
            print(erro)
            time.sleep(2)
            os.system('clear')
            continue
        try:    
            game.compare_choices(user_choice)
        except Exception as erro:
            print(erro)
            time.sleep(2)
            os.system('clear')
            continue
            
        keep_playing = int(input('''Do you want to continue playing?
        [1] Yes
        [0] No
        '''))
    
    
if __name__ == "__main__":
    main()
