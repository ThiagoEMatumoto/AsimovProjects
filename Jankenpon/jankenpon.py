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
        self.computer_choice = self.choices[self.random_choice()]
        print(f'{self.name} used - {self.user_choice}')
        print(f'Computer used - {self.computer_choice}')
        
        if self.user_choice == "Stone":
            if self.computer_choice == "Stone":
                print('DRAW')
            if self.computer_choice == "Paper":
                print('YOU LOST')
                self.computer_points =+ 1
            if self.computer_choice == "Scissors":
                print('YOU WON')
                self.player_points =+ 1
                
        if self.user_choice == "Paper":
            if self.computer_choice == "Stone":
                print('YOU WON')
                self.player_points =+ 1
            if self.computer_choice == "Paper":
                print('DRAW')
            if self.computer_choice == "Scissors":
                print('YOU LOST')
                self.computer_points =+ 1
            
        if self.user_choice == "Scissors":
            if self.computer_choice == "Stone":
                print('YOU LOST')
                self.computer_points =+ 1
            if self.computer_choice == "Paper":
                print('YOU WON')
                self.player_points =+ 1
            if self.computer_choice == "Scissors":
                print('DRAW')
        
        
        