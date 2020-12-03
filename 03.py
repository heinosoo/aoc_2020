import numpy as np


def count_trees(forest, r, d):
    forest = forest[::d]  # Select rows we actually visit.
    width = len(forest[0])
    line = [row[(r*i) % width] for i, row in enumerate(forest)]
    return line.count('#')


##########
# Part 1 #
##########

a = np.loadtxt('03.txt', dtype=str, comments=None)
print(count_trees(a, 3, 1))

##########
# Part 2 #
##########

print(count_trees(a, 1, 1) *
      count_trees(a, 3, 1) *
      count_trees(a, 5, 1) *
      count_trees(a, 7, 1) *
      count_trees(a, 1, 2))
