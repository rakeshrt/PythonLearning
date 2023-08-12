def main():
    print("Enter Number to print * :")
    num = int(input())
    for i in range(num, 0, -1):
       for j in range(0,i):
           print("* ", end="")

       print("\n")


if __name__ == "__main__":
    main()