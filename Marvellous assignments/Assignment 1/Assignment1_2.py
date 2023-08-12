# create Function called chknum
# accept input as number and if number is even then display it as even number or display it as odd number


def chknum():
    print("Enter the number:")
    number = int(input())
    if number % 2 == 0:
        print("Even number")
    else:
        print("ODD Number")


chknum()
