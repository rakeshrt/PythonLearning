import os
import sys
from sys import *


with open(sys.argv[1], 'r') as file1, open(sys.argv[2], 'r') as file2:
    for line1 in file2:
        for line2 in file1:
            if line1 == line2.strip():
                print("success")
                exit()
            else:
                print("Failre")
                exit()
