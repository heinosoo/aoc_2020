import numpy as np
from math import prod

##########
# Part 1 #
##########

jolts = np.sort(np.loadtxt('10.txt', 'i'))
jolts = np.append(jolts, jolts[-1]+3)
jolts = np.insert(jolts, 0, 0)
count = dict(np.transpose(np.unique(jolts[1:]-jolts[:-1], return_counts=True)))
count
print(count[1]*count[3])

##########
# Part 2 #
##########

jolts = np.sort(np.loadtxt('10.txt', 'i'))
jolts = np.append(jolts, jolts[-1]+3)
jolts = np.insert(jolts, 0, 0)
diffs = jolts[1:]-jolts[:-1]
ones = [len(b[b != 3]) for b in np.split(diffs, np.where(diffs == 3)[0])]
f = lambda a: f(a-1) + a-1 if a > 0 else 1
product = prod(map(f, ones))
print(product)
