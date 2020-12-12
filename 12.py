import numpy as np

##########
# Part 1 #
##########
def operate1(op, N, dir, loc):
    if op == 'F':
        return dir, loc + D[dir]*N
    elif op == 'R':
        return (dir+N//90) % 4, loc
    elif op == 'L':
        return (dir-N//90) % 4, loc
    else:
        assert(op in Dmap)
        return dir, loc + D[Dmap[op]]*N


Dmap = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
D = list(map(np.array, [(1, 0), (0, -1), (-1, 0), (0, 1)]))
OPs = [(inst[0], int(inst[1:])) for inst in np.loadtxt('12.txt', 'U')]
dir, loc = 0, (0, 0)
for op, N in OPs:
    dir, loc = operate1(op, N, dir, loc)
print(sum(map(abs, loc)))

##########
# Part 2 #
##########
def operate2(op, N, wp, loc):
    if op == 'F':
        return wp, loc + wp*N
    elif op == 'R':
        for _ in range(N//90): wp = R.dot(wp)
        return wp, loc
    elif op == 'L':
        for _ in range(N//90): wp = L.dot(wp)
        return wp, loc
    else:
        assert(op in Dmap)
        return wp + D[Dmap[op]]*N, loc


R = np.array([[0, 1], [-1, 0]])
L = -R
wp, loc = np.array((10, 1)), (0, 0)
for op, N in OPs:
    wp, loc = operate2(op, N, wp, loc)
print(sum(map(abs, loc)))
