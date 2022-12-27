from locadora import *
from carro import *
from usuario import *
from schemas import *
import os

def main():
    answer = welcome()
    if answer == 1:
        os.system("clear")
        user_login = login()
        if user_login in users:
            return True
        else: 
            return False
    else:
        os.system("clear")
        pass

if __name__ == "__main__":
    main()
