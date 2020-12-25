# import numpy as np
# import re
# from math import sqrt, prod
# from time import time

##########
# Part 1 #
##########


def transform(sub, pri):
    n = 1
    for _ in range(pri):
        n = (n*sub) % 20201227
    return n


def crack(sub, pub1, pub2, N=100000000):
    n = 1
    for pri in range(1, N):
        n = (n*sub) % 20201227
        if n == pub1:
            return transform(pub2, pri)
        elif n == pub2:
            return transform(pub1, pri)


sub = 7
pub_card, pub_door = 5764801, 17807724
pub_card, pub_door = 5099500, 7648211
print(crack(7, pub_card, pub_door))
