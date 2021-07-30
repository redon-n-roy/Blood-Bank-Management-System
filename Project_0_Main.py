import pymongo
from os import system
import otp_service
import stdiomask as s
from time import sleep
import Project_0
Client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
blood_bank = Client['blood_bank']
user = blood_bank.users
login_user = {}

def verify_password():
    pwd1 = s.getpass(prompt='Enter your password :-', mask = '*')
    pwd2 = s.getpass(prompt='Enter your password again:-', mask = '*')
    if(pwd1 != pwd2):
        input('Password mismatch. Press enter to try again')
        verify_password()
    elif(len(pwd1) <5 or len(pwd1)>16):
        input("Password length is not appropriate. Press enter to try again")
        verify_password()
    elif(pwd1.isalnum() == False):
        input("Password should contain only alphanumeric characters. Press enter to try again")
        verify_password()
    else:
        return pwd1

def check_mob():
    numb = input('Enter your 10-digit mobile number: -')
    global login_user
    for usr in user.find({'mobNo': '+91'+numb}):
        login_user = usr
    if(len(numb) != 10 or numb.isdecimal() == False):
        input("Invalid mobile number. Press enter to try again")
        check_mob()
    elif(bool(login_user) and login_user['mobNo'] == '+91'+numb):
        
        return [True,'+91'+numb]
    else:
        input("User does not exist!! Press enter to continue")
        return [False,'+91'+numb]

def check_pwd():
    pwd = s.getpass(prompt='Enter your password :-', mask = '*')
    global login_user
    if(len(pwd) <5 or len(pwd)>16):
        input("Password length is not appropriate. Press enter to try again")
        check_pwd()
    elif(pwd.isalnum() == False):
        input("Password should contain only alphanumeric characters. Press enter to try again")
        check_pwd()
    else:
        if(login_user['password'] == pwd):
            print("\n\nWelcome " + login_user['name'])
            print('Please wait.....')
            return True
        else:
            print('wrong password!!!')
            return False
            



def login_menu():
    global login_user
    login_user = {}
    system('cls')
    print("\n\n\n WELCOME TO BLOOD BANK MANAGEMENT SYSTEM\n\n\n")
    print("Please wait.....")
    sleep(2)
    system('cls')
    print('------Blood Bank Management System------')
    choice = int(input('1.Login\n2.Register\n3.Exit\nEnter your choice:- '))
    if(choice == 1):
        mob = check_mob()
        if(mob[0] == True):
            val = check_pwd()
            if(val == True):
                if(otp_service.verify_phone()): # mob[1] to send otp to user mobile
                    Project_0.menu(login_user['isAdmin'])
                    login_menu()
                else:
                    system('cls')
                    login_menu()
            else:
                system('cls')
                login_menu()
        else:
            system('cls')
            login_menu()

    elif(choice == 2):
        mob = check_mob()
        if(mob[0] == False ):
            name = input('Enter name of user:- ')
            password = verify_password()
            record = {
                'name' : name,
                'password' : password,
                'mobNo' : mob[1],
                'isAdmin': False
            }
            if(otp_service.verify_phone()): # mob[1] to send otp to user mobile
                user.insert_one(record)
                input('User created! Press enter to continue')
                system('cls')
                login_menu()
            else:
                system('cls')
                login_menu()
        else:
            input('User already exists! Press enter to continue')
            system('cls')
            login_menu()
    else:
        try:
            assert False
        except:
            print('Exiting.....')
            sleep(1)
            system('cls')



login_menu()