import numpy as np


def run(code, p, acc, visited):
    if p in visited:
        return False, acc
    elif p == len(code):
        return True, acc
    visited.add(p)
    op, v = code[p]
    if op == 'nop':
        return run(code, p+1, acc, visited)
    elif op == 'acc':
        return run(code, p+1, acc+v, visited)
    elif op == 'jmp':
        # assert(0 <= p+v <= len(code))
        return run(code, p+v, acc, visited)


##########
# Part 1 #
##########

code = np.loadtxt('08.txt', 'O,i')
run(code, 0, 0, set())[1]

##########
# Part 2 #
##########

for n, (op, v) in enumerate(code):
    if op == 'jmp':
        new_code = code.copy()
        new_code[n] = ('nop', v)
    elif op == 'nop':
        new_code = code.copy()
        new_code[n] = ('jmp', v)
    else:
        continue

    result, acc = run(new_code, 0, 0, set())
    if result:
        print(acc)
        break
