# CIS 103: Introduction to Programming
# Lab 01: "Calculator Function"
# Student: Elysee fleurant
# Date: 08/31/2024
#
import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero!."

def expo(x, y):
    return x**y

def modul(x, y):
    return x%y

def squar(x):
    return math.sqrt(x)
def main():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("6. Exponent")
        print("7. Rest")
        print("8. Square")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '5':
            print("exiting, thank you!")
            break
        #num1 = float(input("Enter your first number: "))
        #num2 = float(input("Enter your second number: "))
        if choice == '1':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"the addition between  {num1} and {num2} = {add(num1, num2)}")
        elif choice == '2':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"the subtract between{num1} and {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"the multiply between{num1} and {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"the divide between{num1} + {num2} = {divide(num1, num2)}")
        elif choice == '6':
            num1 = float(input("Enter your  number: "))
            num2 = float(input("Enter your exponent: "))
            print(f"the exponentiation {num1} between {num2} = {expo(num1, num2)}")
        elif choice == '7':
            num1 = float(input("Enter your number dividends: "))
            num2 = float(input("Enter your number divider: "))
            print(f"the rest of division between{num1} and {num2} = {modul(num1, num2)}")
        elif choice == '8':
            num1 = float(input("Enter your number: "))
            #num2 = float(input("Enter your second number: "))
            print(f" the Square is : {num1}  = {squar(num1)}")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()

