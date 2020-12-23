import numpy as np
# import re
# from math import sqrt, prod
from time import time

##########
# Part 1 #
##########


def move(cups):
    i = 1
    dest = (cups[0]-i-1) % L+1
    while dest in cups[1:4]:
        i += 1
        dest = (cups[0]-i-1) % L+1
    a = np.where(cups == dest)[0][0]
    return np.concatenate([cups[4:a+1], cups[1:4], cups[a+1:], cups[0:1]])


cups = np.asarray([int(a) for a in '157623984'])
L = len(cups)
for _ in range(100):
    cups = move(cups)
print(''.join(map(str, np.concatenate(np.split(cups, np.where(cups == 1)[0])[::-1])[1:])))

##########
# Part 2 #
##########

cups = np.asarray([int(a) for a in '157623984'])
cups = np.append(cups, list(range(max(cups)+1, 1000000+1)))
L = len(cups)

t = time()
i = 0
for _ in range(10000000):
    if not (i % 10000):
        print(r'{:.2f}% {:.1f}m'.format(i/100000, (time()-t)/60))
    i += 1
    cups = move(cups)

np.savetxt('23.txt', cups, fmt='%i')

# After a long long time (265 minutes)..
cups = np.loadtxt('23.txt', 'int')
print(cups[np.where(cups == 1)[0][0]+1]*cups[np.where(cups == 1)[0][0]+2])
