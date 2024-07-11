from os import system, name
from server_requests import Server
import json

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

class Person:
    def __init__(self, name, dob, email, phone):
        self.name = name
        self.dob = dob
        self.email = email
        self.phone = phone

server = Server()

def house_menu(address):
    while True:
        clear()
        print(f"Address: {address}")
        print("1. Add person")
        print("2. Remove person")
        print("3. List people")
        print("4. Back")
        inp = input("Choose an option: ")
        if inp in ["1", "2", "3", "4"]:
            break
        input("Invalid option")
   
    clear()

    if inp == "1":
        name = input("Enter name: ")
        dob = input("Enter dob: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        person = Person(name, dob, email, phone)
        print(server.add_person(address, person))
    
    elif inp == "2":
        name = input("Enter name: ")
        dob = input("Enter dob: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        person = Person(name, dob, email, phone)
        print(server.remove_person(address, person))
   
    elif inp == "3":
        people = server.list_people(address)
        if people == "No people in this address" or people == "Address does not exist" or people == "Server is down. Cannot remove person. Run server.py first" or people == "Person already exists":
            print(people)
            input("Press enter to continue")
            return
        
        for person in json.loads(people):
            print("Name:", person["name"])
            print("DOB:", person["dob"])
            print("Email:", person["email"])
            print("Phone:", person["phone"])
            print()
        input("Press enter to continue")

def menu():
    inp = ""
    while True:
        clear()
        print("1. List houses")
        print("2. Manage houses")
        print("3. Exit")
        inp = input("Choose an option: ")
        if inp in ["1", "2", "3"]:
            break
        input("Invalid option")    
   
    clear()

    if inp == "1":
        houses = server.get_houses()
        if houses == "No addresses in storage" or houses == "Server is down. Cannot remove person. Run server.py first":
            print(houses)
            input("Press enter to continue")
            menu()
        
        for house in json.loads(houses):
            print(house)
        
        input("Press enter to continue")
        menu()

    elif inp == "2":
        inp = ""
        while True:
            clear()
            print("1. Add house")
            print("2. Manage house")
            print("3. Back")            
            inp = input("Choose an option: ")
            if inp in ["1", "2", "3"]:
                break
            input("Invalid option")

        clear()

        if inp == "1":
            address = input("Enter address: ")
            print(server.add_house(address))
            input("Press enter to continue")
            menu()
   
        elif inp == "2":
            address = input("Enter address: ")
            house_menu(address)
            menu()

if __name__ == "__main__":
    menu()
