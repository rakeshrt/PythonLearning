
def main():
    print("Enter number to print *")
    val = int(input())

    for i in range(val):
        for i in range(val):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    main()