#Blood Bank Management System
import pymongo
from os import system
from bson.objectid import ObjectId
import otp_service
Client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
blood_bank = Client['blood_bank']
donor = blood_bank.donors
is_Administrator = False


def print_data(dnr):
    print('ID: -',dnr['_id'])
    print('Name:- ',dnr['name'])
    print('Age:- ',dnr['age'])
    print('Blood group:- ', dnr['bgroup'])
    print('City:- ', dnr['city'])
    print('District:- ', dnr['district'])
    print('State:- ', dnr['state'])
    print('----------------------------')

def menu(ad):
    global is_Administrator
    is_Administrator = ad
    system('cls')
    while(True):
        print('------Blood Bank Management System------')
        print('1. New Donor\n2. List Donor\n3. Search Donor\n4. Update Donor\n5. Delete Donor\n6. Exit')
        choice = int(input('Enter your choice:- '))
        if(choice == 1):
            if(is_Administrator):
                new_donor()
            else:
                input("You are not an admin! Press enter to continue")
                system('cls')
                menu(is_Administrator)
        elif(choice == 2):
            list_donor()
        elif(choice == 3):
            search_donor()
        elif(choice == 4):
            if(is_Administrator):
                update_donor()
            else:
                input("You are not an admin! Press enter to continue")
                system('cls')
                menu(is_Administrator)
        elif(choice == 5):
            if(is_Administrator):
                delete_donor()
            else:
                input("You are not an admin! Press enter to continue")
                system('cls')
                menu(is_Administrator)
        elif(choice == 6):
                print('Exiting...')
                break
        else:
            ret = input("invalid choice!!! Wanna try again? (Y/N)").upper()
            if(ret == 'Y'):
                system('cls')
                menu()
            else:
                break
    return



def new_donor():
    name = input("Enter the name of the donor:- ")
    age = input("Enter the age of the donor:- ")
    bgroup = input("Enter the blood group of the donor:- ")
    city = input("Enter the city of the donor:- ")
    district = input("Enter the district of the donor:- ")
    state = input("Enter the state of the donor:- ")

    record = {
        'name': name.capitalize(),
        'age': age,
        'bgroup': bgroup.capitalize(),
        'city': city.capitalize(),
        'district': district.capitalize(),
        'state': state.capitalize(),
    }
    if(otp_service.verify_phone()): # pass mobile number to send otp to user mobile
        donor.insert_one(record)
        print('Data inserted successfully')
        input("PRESS ENTER TO CONTINUE")
        system('cls')
    else:
        print('Data not inserted ! Try again...')
        input("PRESS ENTER TO CONTINUE")
        system('cls')

def list_donor():
    cursor = donor.find({})
    print('------List of Donors-------\n')
    for dnr in cursor:
        print_data(dnr)
    else:
        print('\n------End of the list------')
    if(True):
        input("press enter to return to menu")
        system('cls')

def search_donor():
    choice = int(input("How do you want to search for the donor?"
                    "\n1. By Blood Group \n2. By City \n3. ByDistrict"
                    "\n4. By State \nEnter your choice:-"))
    if(choice==1):
        inp_bg = input("Enter the required blood group of the donor:- ").capitalize()
        print('\n------List of '+inp_bg+' donors------\n')
        for dnr in donor.find({'bgroup': inp_bg}):
            print_data(dnr)
        else:
            print('\n------End of the list------')
            input('press enter to return to menu')
            system('cls')
    elif(choice==2):
        inp_city = input("Enter the required city of the donor:- ").capitalize()
        print('\n------List of donors in '+inp_city+'------\n')
        for dnr in donor.find({'city': inp_city}):
            print_data(dnr)
        else:
            print('\n------End of the list------')
            input('press enter to return to menu')
            system('cls')
    elif(choice == 3):
        inp_dis = input("Enter the required district of the donor:- ").capitalize()
        print('\n------List of donors in '+inp_dis+'------\n')
        for dnr in donor.find({'bgroup': inp_dis}):
            print_data(dnr)
        else:
            print('\n------End of the list------')
            input('press enter to return to menu')
            system('cls')
    elif(choice == 4):
        inp_st = input("Enter the required state of the donor:- ").capitalize()
        print('\n------List of donors in '+inp_st+'------\n')
        for dnr in donor.find({'bgroup': inp_st}):
            print_data(dnr)
        else:
            print('\n------End of the list------')
            input('press enter to return to menu')
            system('cls')
    else:
        ret = input("invalid choice!!! Wanna try again? (Y/N)").upper()
        if(ret == "Y"):
            system('cls')
            search_donor()
        else:
            system('cls')


def update_donor():
    dnr_id = input('Enter the donor ID to update:- ')
    for dnr in donor.find({'_id':ObjectId(dnr_id)}):
        if(dnr['_id'] == ObjectId(dnr_id)):
            print('What you want to update?')
            choice = int(input('1.Name\n2.Age\n3.Blood Group'
                                '\n4.City\n5.District\n6.State'
                                '\nEnter your choice:- '))
            if(otp_service.verify_phone()): # pass mobile number to send otp to user mobile
                if(choice == 1):
                    new_name = input('Enter the new name:- ')
                    donor.update_one({'_id':ObjectId(dnr_id)},{'$set':{'name':new_name}})
                    input('Name updated. Press enter to continue')
                    system('cls')
                elif(choice == 2):
                    new_age = input('Enter the new age:- ')
                    donor.update_one({'_id':ObjectId(dnr_id)},{'$set':{'age':new_age}})
                    input('Age updated. Press enter to continue')
                    system('cls')
                elif(choice == 3):
                    new_bgroup = input('Enter the new blood group:- ')
                    donor.update_one({'_id':ObjectId(dnr_id)},{'$set':{'bgroup':new_bgroup}})
                    input('Blood group updated. Press enter to continue')
                    system('cls')
                elif(choice == 4):
                    new_city = input('Enter the new city:- ')
                    donor.update_one({'_id':ObjectId(dnr_id)},{'$set':{'city':new_city}})
                    input('Name updated. Press enter to continue')
                    system('cls')
                elif(choice == 5):
                    new_dist = input('Enter the new district:- ')
                    donor.update_one({'_id':ObjectId(dnr_id)},{'$set':{'name':new_dist}})
                    input('District updated. Press enter to continue')
                    system('cls')
                elif(choice == 6):
                    new_state = input('Enter the new state:- ')
                    donor.update_one({'_id':ObjectId(dnr_id)},{'$set':{'name':new_state}})
                    input('State updated. Press enter to continue')
                    system('cls')
                else:
                    ret = input("invalid choice!!! Wanna try again? (Y/N)").upper()
                    if(ret == "Y"):
                        system('cls')
                        update_donor()
                    else:
                        system('cls')
            else:
                print('Data not updated ! Try again...')
                input("PRESS ENTER TO CONTINUE")
                system('cls')
        else:
            print('donor not found')
            input('press enter to return to menu')
            system('cls')

def delete_donor():
    dnr_id = input('Enter the donor ID to delete:- ')
    for dnr in donor.find({'_id':ObjectId(dnr_id)}):
        if(dnr['_id'] == ObjectId(dnr_id)):
            if(otp_service.verify_phone()): # pass mobile number to send otp to user mobile
                donor.delete_one({'_id':ObjectId(dnr_id)})
                input('Donor deleted. Press enter to continue')
                system('cls')
            else:
                print('Data not updated ! Try again...')
                input("PRESS ENTER TO CONTINUE")
                system('cls')
        else:
            print('donor not found')
            input('press enter to return to menu')
            system('cls')
