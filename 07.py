import numpy as np
import re

rules = np.fromregex('07.txt', r'(.+) bags contain (.+)', 'O, O')
rules = {rule[0]:
         {bag: int(nr) for nr, bag in re.findall(r'(\d+) (\S+ \S+) bag', rule[1])}
         for rule in rules}

##########
# Part 1 #
##########


def fits_in(bag, bags):
    fit = {a for a in bags if bag in rules[a]}
    return fit and set.union(fit, *[fits_in(b, bags-fit) for b in fit])


print(len(fits_in('shiny gold', rules.keys())))

##########
# Part 2 #
##########


def fits_nr(bag):
    return sum([n*(1+fits_nr(b)) for b, n in rules[bag].items()])


print(fits_nr('shiny gold'))
