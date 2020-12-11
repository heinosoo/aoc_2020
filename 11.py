import numpy as np


def mask(seats):
    mask = np.zeros(seats.shape)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == '#':
                mask[i-1:i+2, j-1:j+2] += 1
                mask[i, j] -= 1
    return mask


def step(seats):
    to_fill = (seats == 'L') * (mask(seats) == 0)
    to_empty = (seats == '#') * (mask(seats) >= 4)
    seats[to_fill] = '#'
    seats[to_empty] = 'L'
    return seats


def mask2(seats):
    mask = np.zeros(seats.shape)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == '#':
                mask2_loc((i, j), mask, seats)
    return mask


def mask2_loc(loc, mask, seats):
    shape = seats.shape
    right = range(loc[0]+1, shape[0])
    down = range(loc[1]+1, shape[1])
    left = range(loc[0]-1, -1, -1)
    up = range(loc[1]-1, -1, -1)

    directions = (zip(right, down),
                  zip(right, up),
                  zip(left, up),
                  zip(left, down),
                  zip(right, shape[0]*[loc[1]]),
                  zip(left, shape[0]*[loc[1]]),
                  zip(shape[1]*[loc[0]], up),
                  zip(shape[1]*[loc[0]], down))
    for direction in directions:
        for p in direction:
            mask[p] += 1
            if seats[p] != '.':
                break


def step2(seats):
    to_fill = (seats == 'L') * (mask2(seats) == 0)
    to_empty = (seats == '#') * (mask2(seats) >= 5)
    seats[to_fill] = '#'
    seats[to_empty] = 'L'
    return seats


##########
# Part 1 #
##########
seats_input = np.array([list(row) for row in np.loadtxt('11.txt', 'U')])
seats = np.full(np.array(seats_input.shape)+2, ',')
seats[1:-1, 1:-1] = seats_input

while True:
    if np.array_equal(seats.copy(), step(seats)):
        break
np.count_nonzero(seats == '#')

##########
# Part 2 #
##########

seats_input = np.array([list(row) for row in np.loadtxt('11.txt', 'U')])
seats = np.full(np.array(seats_input.shape)+2, ',')
seats[1:-1, 1:-1] = seats_input

while True:
    if np.array_equal(seats.copy(), step2(seats)):
        break
np.count_nonzero(seats == '#')
