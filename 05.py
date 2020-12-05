import numpy as np

##########
# Part 1 #
##########

a = (bp.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
     for bp in np.loadtxt('05.txt', dtype=str))
a = [int(bp, 2) for bp in a]
print(max(a))

##########
# Part 2 #
##########

b = range(min(a), max(a))
print(set(b).difference(set(a)))
