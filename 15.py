# import numpy as np

##########
# Part 1 #
##########

turns = [14, 3, 1, 0, 9, 5]
mem = {a: (0, i) for i, a in enumerate(turns)}
a = turns[-1]
for i in range(len(turns), 2020):
    a = mem[a][0]
    if a not in mem:
        mem[a] = (0, i)
    else:
        mem[a] = (i-mem[a][1], i)
print(a)

##########
# Part 2 #
##########
# Sama

turns = [14, 3, 1, 0, 9, 5]
mem = {a: (0, i) for i, a in enumerate(turns)}
a = turns[-1]
for i in range(len(turns), 30000000):
    if not i % 3000000:  # paranoia
        print('{}0%'.format(i//3000000))
    a = mem[a][0]
    if a not in mem:
        mem[a] = (0, i)
    else:
        mem[a] = (i-mem[a][1], i)
print(a)
