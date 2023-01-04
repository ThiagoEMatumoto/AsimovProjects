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

    def computer_choice(self):
        return random.randint(0,2)
