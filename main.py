import random
import clipboard
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+?'

while True:
    print("Welcome to the latest sojjyCodes program using python. ")
    number = int(input("Numbers of password: "))
    length = int(input("The length: "))

    for p in range(number):
        password = ''
    for c in range(length):
        password += random.choice(chars)
        print(password)
        text = clipboard.copy(password)

    print("The last password generated has been added to your clipboard!")

    operation = input("Do you want to continue (Y/N): ")
    if operation == "Y":
        print("Let get started")
    
    elif operation == "N":
        break 
    else:
        print("Invalid Command")