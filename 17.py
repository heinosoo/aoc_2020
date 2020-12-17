import numpy as np


def step(grid):
    mask = np.zeros(grid.shape, dtype=int)
    for x, y, z in zip(*grid.nonzero()):
        mask[x-1:x+2, y-1:y+2, z-1:z+2] += 1
        mask[x, y, z] -= 1
    to_activate = np.logical_not(grid) * (mask == 3)
    to_deactivate = grid * (mask != 2) * (mask != 3)
    grid[np.where(to_activate)] = 1
    grid[np.where(to_deactivate)] = 0
    return grid.sum()


def step4d(grid):
    mask = np.zeros(grid.shape, dtype=int)
    for x, y, z, w in zip(*grid.nonzero()):
        mask[x-1:x+2, y-1:y+2, z-1:z+2, w-1:w+2] += 1
        mask[x, y, z, w] -= 1
    to_activate = np.logical_not(grid) * (mask == 3)
    to_deactivate = grid * (mask != 2) * (mask != 3)
    grid[np.where(to_activate)] = 1
    grid[np.where(to_deactivate)] = 0
    return grid.sum()


##########
# Part 1 #
##########

state = [[int(a) for a in line.replace('.', '0').replace('#', '1')]
         for line in np.loadtxt('17.txt', 'U', comments=None)]

L = len(state)*13  # Side length for grid
C = len(state)*12//2  # "Centre" of the grid
grid = np.zeros((L,)*3, dtype=int)  # Make a grid of zeroes
grid[C:C+len(state), C:C+len(state), C] = state  # Initialize
_ = [print(r'step: {}, active: {}'.format(i, step(grid))) for i in range(1,7)]

##########
# Part 2 #
##########

state = [[int(a) for a in line.replace('.', '0').replace('#', '1')]
         for line in np.loadtxt('17.txt', 'U', comments=None)]

L = len(state)*13  # Side length for grid
C = len(state)*12//2  # "Centre" of the grid
grid = np.zeros((L,)*4, dtype=int)  # Make a grid of zeroes
grid[C:C+len(state), C:C+len(state), C, C] = state  # Initialize
_ = [print(r'step: {}, active: {}'.format(i, step4d(grid))) for i in range(1,7)]
