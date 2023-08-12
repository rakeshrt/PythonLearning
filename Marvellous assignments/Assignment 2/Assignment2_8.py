def main():
    print("Enter number:")
    number = int(input())

    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")


if __name__ == "__main__":
    main()