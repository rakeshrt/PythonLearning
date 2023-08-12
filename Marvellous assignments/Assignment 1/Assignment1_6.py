# Write program to find out input number is positive or Negative or Zero

def main():
    print("Enter Number :")
    num1 = int(input())
    if num1 > 0:
        print("Given Number is Positive")
    elif num1 == 0:
        print("Given Number is Zero")
    else:
        print("Given number is negative Number")


if __name__ == "__main__":
    main()
