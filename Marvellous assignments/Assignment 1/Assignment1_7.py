#Write code to check input number is divisible by 5 or return false
def main():
    print("Enter Number ")
    num = int(input())
    if num % 5 == 0:
        print("Number is divisible by 5 ")
    else:
        print("Number is false")


if __name__ == "__main__":
    main()