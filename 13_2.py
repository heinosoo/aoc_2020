import numpy as np

##########
# Part 1 #
##########

with open('13_test.txt') as f:
    start = int(f.readline())
    ids = [int(id) for id in f.readline().strip().split(',') if id != 'x']

departs_in = [start % n and (n - start % n) for n in ids]
earliest = departs_in.index(min(departs_in))
print(ids[earliest]*departs_in[earliest])

##########
# Part 2 #
##########

with open('13.txt') as f:
    start = int(f.readline())
    ids = [int(id) for id in f.readline().strip().replace('x', '0').split(',')]
    ids_enum = [(i, id) for i, id in enumerate(ids) if id]

N = 0
a = 1
for i, id in ids_enum:
    # print(i,id)
    for k in range(id):
        if not ((N + k*a + i) % id):
            N += k*a
            # print('result', k, N % id, i, N)
            a *= id
            break
print(N)
