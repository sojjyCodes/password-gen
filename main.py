import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+?'

number = input("Numbers of password ")
number = int(number)

length = input("The length ")
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)