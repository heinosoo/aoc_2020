import numpy as np
# import re
# from math import sqrt, prod
# from time import time
from collections import defaultdict

# Oblique coordinates
dirmap = {'e': (1, 0),
          'w': (-1, 0),
          'a': (-1, 1),   # nw
          'b': (1, -1),   # se
          'c': (0, 1),    # ne
          'd': (0, -1)}  # sw

##########
# Part 1 #
##########

inst = np.loadtxt('24.txt', 'U')
inst = (a.replace('nw', 'a').replace('se', 'b').replace('ne', 'c').replace('sw', 'd')
        for a in inst)
inst = [tuple(map(sum, zip(*map(dirmap.get, a)))) for a in inst]
tiles = {tile: inst.count(tile) % 2 for tile in set(inst)}
print(sum(tiles.values()))

##########
# Part 2 #
##########

black = {tile for tile, n in tiles.items() if n}
for _ in range(100):
    mask = defaultdict(int)
    for tile in black:
        for tile_mark in [(tile[0]+x, tile[1]+y) for x, y in dirmap.values()]:
            mask[tile_mark] += 1
    black_add = set()
    black_rem = set()
    for tile, n in mask.items():
        if tile in black and n > 2:
            black_rem.add(tile)
        elif n == 2:
            black_add.add(tile)
    black_rem |= (black - set(mask.keys()))
    black = (black | black_add) - black_rem
print(len(black))
