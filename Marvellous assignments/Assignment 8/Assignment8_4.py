

def summation(num):
    if num == 0:
        return 0
    else:
        return (num % 10 + summation(int( num / 10 )))

def main():
    print("Please enter number")
    num = int(input())

    addition = summation(num)
    print(addition)


if __name__ == "__main__":
    main()