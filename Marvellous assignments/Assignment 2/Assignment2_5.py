def main():
    print("Enter number to check if prime or not:")
    number = int(input())

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print("Given Number is not Prime number")
                break
        else:
            print("Given number is prime number")


if __name__ == "__main__":
    main()