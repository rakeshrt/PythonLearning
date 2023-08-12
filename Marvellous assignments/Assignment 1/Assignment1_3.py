#Write program which contains one function names as Add() which accept two numbers from user and return addition of that two numbers and performm addition

def add():
    print("Enter frst number :")
    num1 = input()
    print("Enter second number :")
    num2 = input()
    addition = int(num1) + int(num2)
    print("Addition of num1 and num2 is ", addition)


add()