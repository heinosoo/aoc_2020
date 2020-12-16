# import numpy as np
import re
from math import prod


def parse(file):
    re_rule = re.compile('^(.+): (\d+)-(\d+) or (\d+)-(\d+)')
    rules = {}
    with open(file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            rule, a, b, c, d = re_rule.findall(line)[0]
            k = [int(x) for x in (a, b, c, d)]
            rules[rule] = lambda x, k=k: (k[0] <= x <= k[1]) or (k[2] <= x <= k[3])
        f.readline()
        while True:
            line = f.readline().strip()
            if not line:
                break
            ticket_mine = [int(a) for a in line.split(',')]
        f.readline()
        tickets = [[int(a) for a in ticket.strip().split(',')]
                   for ticket in f.readlines()]
    return rules, ticket_mine, tickets


##########
# Part 1 #
##########

rules, _, tickets = parse('16.txt')
x = [[(not any([rule(a) for rule in rules.values()]))*a
     for a in ticket] for ticket in tickets]
sum(sum(x, []))

##########
# Part 2 #
##########

rules, ticket_mine, tickets = parse('16.txt')
tickets = [ticket for ticket in tickets if
           all([any([rule(a) for rule in rules.values()]) for a in ticket])]

comp = {}
for field, rule in rules.items():
    comp[field] = [all([rule(ticket[i]) for ticket in tickets])
                   for i in range(len(ticket_mine))]
sets = [{field for field, c in comp.items() if c[i]} for i in range(len(ticket_mine))]
f = lambda a, b: (a-b) if a-b else a  # Pairwise filter
for i in range(len(sets)):
    for j in range(len(sets)):
        sets[i] = f(sets[i], sets[j])

values = [ticket_mine[i] for i, field in enumerate(sets) if 'departure' in field.pop()]
print(prod(values))
