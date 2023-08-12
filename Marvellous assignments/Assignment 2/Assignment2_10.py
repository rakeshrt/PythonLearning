def main():
    print("Enter number:")
    num1 = input()

    sum = 0
    for i in range(0, len(num1)):
        fact1 = int(num1[i])
        #print("first number1", fact1)
        sum = sum + int(num1[i])

    print("sum is: ", sum)


if __name__ == "__main__":
    main()