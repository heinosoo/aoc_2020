import numpy as np
# import re
from math import sqrt, prod


##########
# Part 1 #
##########

def variants(tile):
    tile_variants = [np.rot90(tile, n) for n in range(4)]
    tile_variants.extend([np.flipud(tile) for tile in tile_variants])
    return tile_variants


def test(image, tile, x, y):
    if x:  # Not first
        if not (image[x-1][y][:, -1] == tile[:, 0]).all():
            return False
    if y:
        if not (image[x][y-1][-1, :] == tile[0, :]).all():
            return False
    return True


def reconstruct(available):
    # print(available)
    if not available:
        return True
    for x in range(L):
        for y in range(L):
            if not isinstance(image[x][y], np.ndarray):  # Tile slot is empty
                for id in available:
                    for tile in tiles[id]:
                        if test(image, tile, x, y):
                            image[x][y] = tile
                            ids[x][y] = id
                            if reconstruct(available - {id}):
                                return True
                            else:
                                image[x][y] = False
                                ids[x][y] = False
                return False


with open('20.txt') as f:
    tiles = (tile.splitlines() for tile in f.read().split('\n\n'))
    tiles = {int(tile[0].split(' ')[1][:-1]):
             variants([[int(c == '#') for c in line] for line in tile[1:]])
             for tile in tiles}
    L = int(sqrt(len(tiles)))

image = [[0]*L for i in range(L)]
ids = [[0]*L for i in range(L)]
reconstruct(set(tiles.keys()))
print(prod((ids[0][0], ids[-1][0], ids[0][-1], ids[-1][-1])))

##########
# Part 2 #
##########

image = np.block([[image[y][x][1:-1, 1:-1]
                  for y in range(len(image[0]))] for x in range(len(image))])
seamonster = ['                  # ',
              '#    ##    ##    ###',
              ' #  #  #  #  #  #   ']
seamonster = np.asarray([[int(c == '#') for c in line] for line in seamonster])
sx, sy = seamonster.shape

found = False
for i_var in variants(image):
    for x in range(len(i_var)-sx+1):
        for y in range(len(i_var[0])-sy+1):
            window = i_var[x:sx+x, y:sy+y]
            if (np.logical_or(window, np.logical_not(seamonster))).all():
                print('Found one!')
                found = True
                i_var[x:sx+x, y:sy+y] = np.logical_xor(window, seamonster)
    if found: break
print(image.sum())
