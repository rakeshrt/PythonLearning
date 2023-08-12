def main():
    print("calculate factorial of input number: ")
    num1 = int(input())
    factor = 1

    for i in range(1, num1+1):
        factor = factor * i
    print("factorial is:", factor)


if __name__ == "__main__":
    main()

