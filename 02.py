import numpy as np


def test1(line):
    low, high, match, password = line
    if low <= password.count(match) <= high:
        return True
    else:
        return False


def test2(line):
    a, b, m, password = line
    if (password[a-1] == m) ^ (password[b-1] == m):
        return True
    else:
        return False


##########
# Part 1 #
##########

a = np.fromregex('02.txt', r'(\d+)-(\d+) (.+): (.+)', 'i, i, O, O')
print(np.count_nonzero(np.vectorize(test1)(a)))

##########
# Part 2 #
##########

a = np.fromregex('02.txt', r'(\d+)-(\d+) (.+): (.+)', 'i, i, O, O')
print(np.count_nonzero(np.vectorize(test2)(a)))
