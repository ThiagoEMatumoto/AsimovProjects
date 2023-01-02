from locadora import *
from time import sleep


def welcome():
    print('=============================')
    print(' WELCOME TO SUPER CAR RENTAL ')
    print('=============================')
    print('          _______')
    print('         //  ||\ \ ')
    print('   _____//___||_\ \___')
    print('   )  _          _    \ ')
    print('   |_/ \________/ \___|')
    print('  ___\_/________\_/______ \n')
    print(' [1] - Login ')
    print(' [2] - Register \n')
    answer = input()
    return answer

def login():
    print('=============================')
    print('    LOGIN WITH YOUR COUNT    ')
    print('=============================')
    user =  input("Login: ")
    password =  input("Password: ")
    user_login = (user, password)
    if user_login in users:
        return True
    else: 
        return False

    
def register():
    print('=============================')
    print('     REGISTER A NEW COUNT    ')
    print('=============================')
    user =  input("Login: ")
    password =  input("Password: ")
    confirm_password =  input("Confirm your password: ")
    if password == confirm_password and (user) in users :
        users.append((user,password))
        login()
    elif password != confirm_password:
        print('Passwords are not the same')
        sleep(4)
        register()
    else:
        print('User already registered')
        sleep(4)
        register()

    
    
    