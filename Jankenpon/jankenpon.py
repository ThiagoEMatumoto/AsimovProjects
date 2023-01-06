import random
import time 
import os
from schema import *

class jankenpon():
    
    choices = ["Stone", "Paper", "Scissors"]
    
    def __init__(self, name):
        self.name = name
        self.player_points = 0
        self.computer_points = 0

    def random_choice(self):
        return random.randint(0,2)
    
    def compare_choices(self, user_choice):
        self.user_choice = self.choices[user_choice]
        self.computer_choice = self.random_choice()
        if self.user_choice == 0:
            pass
        if self.user_choice == 1:
            pass
        if self.user_choice == 2:
            pass
        
        
        