from locadora import *
from carro import *
from usuario import *
from schemas import *
import os


def main():
    os.system("clear")
    while True:
        answer = welcome()
        if answer not in '12':
            main()
        if answer == '1':
            os.system("clear")
            login_allowed = login()
        elif answer == '2':
            os.system("clear")
            pass

if __name__ == "__main__":
    main()
