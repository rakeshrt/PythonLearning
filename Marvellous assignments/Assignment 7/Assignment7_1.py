import threading


def even(num):
    for i in range(1,num,1):
        if(i % 2 ==0):
            print("Even Number :",i)


def odd(num):
    for i in range(1,num,1):
        if(i % 2 != 0):
            print("Odd Number :", i)


def main():
    print("Print Even and Odd using multithreading")
    number = 20

    process1 = threading.Thread(target=even, args = (number,))
    process2 = threading.Thread(target=odd, args = (number,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


if __name__ == "__main__":
    main()