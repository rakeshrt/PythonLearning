

def factorial(num):
    if num == 1:
        return num
    else:
        return (num * factorial(num-1))


def main():
    print("Please enter number")
    num = int(input())

    factor = factorial(num)
    print(factor)


if __name__ == "__main__":
    main()