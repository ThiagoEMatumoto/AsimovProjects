from locadora import *
from carro import *
from usuario import *
import os

def welcome():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(' WELCOME TO SUPER CAR RENTAL ')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('          _______')
    print('         //  ||\ \ ')
    print('   _____//___||_\ \___')
    print('   )  _          _    \ ')
    print('   |_/ \________/ \___|')
    print('  ___\_/________\_/______ \n')
    print(' [1] - Login ')
    print(' [2] - Register \n')
    answer = int(input())
    return answer

def main():
    answer = welcome()
    if answer == 1:
        pass
    else:
        pass

if __name__ == "__main__":
    main()
