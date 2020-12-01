import numpy as np


def find2(report, sum):
    a = report[0]
    report = report[1:]
    if not report:
        return 0
    else:
        for b in report:
            if a+b == sum:
                return a*b
    return find2(report, sum)


def find3(report, sum):
    a = report[0]
    report = report[1:]
    if not report:
        return 0
    else:
        return find2(report, sum-a)*a or find3(report, sum)


##########
# Part 1 #
##########

input_tests = [[1721, 979, 366, 299, 675, 1456]]
output_tests = [514579]
for it, ot in zip(input_tests, output_tests):
    o = find2(it, 2020)
    print(ot, o, ot == o)

a = np.loadtxt('01.txt', dtype=int)
print(find2(list(a), 2020))

##########
# Part 2 #
##########

input_tests = [[1721, 979, 366, 299, 675, 1456]]
output_tests = [241861950]
for it, ot in zip(input_tests, output_tests):
    o = find3(it, 2020)
    print(ot, o, ot == o)

a = np.loadtxt('01.txt', dtype=int)
print(find3(list(a), 2020))
