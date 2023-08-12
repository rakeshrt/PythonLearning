import sys
from collections import Counter
lines = open(sys.argv[2], 'r').readlines()
c = Counter()
for line in lines:
    for work in line.strip().split():
        c.update(work)
for ind in c:
    print ind, c[ind]