import numpy as np

##########
# Part 1 #
##########

data = np.loadtxt('09.txt', 'i')

for i, n in enumerate(data[25:]):
    sums = set.union(*[{a+b for a in data[i:i+25] if a != b} for b in data[i:i+25]])
    if n not in sums:
        invalid = n
        print(invalid)
        break

##########
# Part 2 #
##########

for L in range(1, len(data)):
    sums = [sum(data[i:i+L+1]) for i in range(len(data)-L-1)]
    if invalid in sums:
        i = sums.index(invalid)
        numbers = data[i:i+L+1]
        print(min(numbers)+max(numbers))
        break
