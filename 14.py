import numpy as np

##########
# Part 1 #
##########

code = np.loadtxt('14.txt', 'O,O', delimiter=' = ')

mem = {}
mask = [0, 0]
for op, v in code:
    if op == 'mask':
        mask[0] = int(v.replace('1', '0').replace('X', '1'), 2)
        mask[1] = int(v.replace('X', '0'), 2)
    else:
        v = int(v) & mask[0] | mask[1]
        exec('{} = {}'.format(op, v))
print(sum(mem.values()))

##########
# Part 2 #
##########

code = np.loadtxt('14.txt', 'O,O', delimiter=' = ')

mem = {}
mask = [0, 0]
for op, v in code:
    if op == 'mask':
        mask[0] = int(v.replace('1', '0').replace('X', '1'), 2)
        mask[1] = int(v.replace('X', '0'), 2)
    else:
        a = int(op.split('[')[1][:-1])
        addr = [a & ~mask[0] | mask[1] | m
                for m in bitmasks(mask[0])]
        mem.update({a: int(v) for a in addr})
print(sum(mem.values()))


def bitmasks(m):
    if not m:
        return [0]
    elif m & 1:
        A = [a << 1 for a in bitmasks(m >> 1)]
        B = [(a << 1) + 1 for a in bitmasks(m >> 1)]
        return A + B
    else:
        return [a << 1 for a in bitmasks(m >> 1)]
