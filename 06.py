import numpy as np

##########
# Part 1 #
##########

with open('06.txt') as f:
    a = np.array(f.readlines())
a = (''.join(group) for group in np.split(a, np.where(a == '\n')[0]))
s = sum((len(set(group))-1 for group in a))
print(s)

##########
# Part 2 #
##########

with open('06.txt') as f:
    a = np.array(f.readlines())
a = np.split(a, np.where(a == '\n')[0])
a = [len(set.intersection(*[set(q.strip()) for q in group if q != '\n']))
     for group in a]
print(sum(a))
