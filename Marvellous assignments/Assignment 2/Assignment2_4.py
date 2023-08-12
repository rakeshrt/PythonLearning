def main():
    print("Enter number:")
    num = int(input())
    i = []
    #factorial = 1
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


if __name__ == "__main__":
    main()
