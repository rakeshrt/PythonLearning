import os
import sys
from sys import *


def FileCopy(Filename):
    with open(sys.argv[1], 'r') as file1, open(sys.argv[2], 'w') as file2:
        for line in file1:
            file2.write(line)
            print(line)


def main():
    if len(argv) != 3:
        print("Error : Invalid number of arguments")
        exit()

    FileCopy(argv[2])


if __name__ == "__main__":
    main()