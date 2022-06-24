import os
import sys
import pyperclip
import random


def password_generator():
    os.system("cls")
print("Password DUDGenerator")
print("Developed by: Vyznite")
print("Options:")
print("1. Maak een password met letters en cijfers")
print("2. Maak een password met letters en cijfers en speciale tekens")
choice = input("Enter your choice: ")

def To_Long():
    print("Het wachtwoord is te lang!")
    sys.exit()

password_generator()

if choice == "1":
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    length = int(input("length [MAX:50]: "))
    if length > 50:
        To_Long()
    else:
        for i in range(length):
            password += random.choice(letters + numbers)
            os.system("cls")
        print("het password is: " + password)
        print("dit password is gekopieerd naar het klembord")
        pyperclip.copy(password)
        input("druk op enter om terug te gaan")

if choice == '2':
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    special = "!@#$%^&*()_+"
    password = ""
    length = int(input("length: "))
    if length > 50:
        To_Long()
    else:
        for i in range(length):
            password += random.choice(letters + numbers + special)
            os.system("cls")
        print("het password is: " + password)
        print("dit password is gekopieerd naar het klembord")
        pyperclip.copy(password)
        input("druk op enter om terug te gaan")
