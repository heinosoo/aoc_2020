import numpy as np
# import re
# from math import sqrt, prod

##########
# Part 1 #
##########

foods = [(set(things.split(' ')), set(allergens.split(', '))) for things, allergens
         in np.fromregex('21.txt', r'(.+) \(contains (.+)\)', 'O, O')]
ingredients = {b for i, _ in foods for b in i}  # All ingredients.
# Initialize the allergen possibilities.
a_dict = {b: ingredients.copy() for _, a in foods for b in a}
for things, allergens in foods:
    for allergen in allergens:
        # Leave only ingredients that were in the food and still possible.
        a_dict[allergen] &= things
i_clean = ingredients - {b for i in a_dict.values() for b in i}
print(sum([len(i & i_clean) for i, _ in foods]))

##########
# Part 2 #
##########

a_list = []
for _ in range(len(a_dict)):
    # Taavi method: take an item with only one possibility.
    next_a = min(a_dict, key=lambda x: len(a_dict[x]))
    next_i = a_dict.pop(next_a).pop()
    a_list.append((next_a, next_i))
    for a in a_dict:
        a_dict[a] -= {next_i}

print(','.join(i for _, i in sorted(a_list)))
