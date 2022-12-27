from locadora import *


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

def login():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('    LOGIN WITH YOUR COUNT    ')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    user =  input("Login: ")
    password =  input("Password: ")
    user_login = (user, password)
    return user_login
    
def register():
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('     REGISTER A NEW COUNT    ')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    user =  input("Login: ")
    password =  input("Password: ")
    confirm_password =  input("Confirm your password: ")
    try:
        password == confirm_password
    except:
        pass
    user_login = (user, password)

    
    
    