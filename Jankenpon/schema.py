from jankenpon import *

def welcome():
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("°            JANKENPON            °")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")


def scoreboard(name: str, user_points: int, computer_points: int):
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("°           SCOREBOARD            °") 
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print(f" {name} - {user_points}         ") 
    print(f" Computer - {computer_points}   ")


def make_your_choice(choices):
    print("___________________________________")
    print("Make your choice:")
    for i, choice in enumerate(choices):
        print(f'{i} - {choice}')
    print("___________________________________")








