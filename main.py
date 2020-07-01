import random
import clipboard

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+?'

print("Welcome to the latest sojjyCodes program using python. ")
number = input("Numbers of password: ")
number = int(number)

length = input("The length: ")
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
    text = clipboard.copy(password)