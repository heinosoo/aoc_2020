import numpy as np
import re

##########
# Part 1 #
##########


def calculate_inside(expr):
    # Inside parantheses (no nesting to worry about), add parantheses and evaluate.
    return eval('('*len(a.findall(expr)) + a.sub(r'\1)', expr))


def calculate_all(expr):
    while '(' in expr:  # Find evaluate unnested or innermost parantheses and repeat.
        expr = b.sub(lambda match: str(calculate_inside(match.group())), expr)
    return calculate_inside(expr)


a = re.compile(r'(\+ \d+)')
b = re.compile(r'(\([^(]+?\))')  # Matches a parantheses that do not have nested ones.
expressions = np.loadtxt('18.txt', 'U', delimiter='!')
sum([calculate_all(e) for e in expressions])

##########
# Part 1 #
##########


def calculate_all2(expr):
    # Same as above, but just add parantheses around any a1 + .. + an.
    while '(' in expr:
        expr = b.sub(lambda match: str(eval(a2.sub(r'(\1)', match.group()))), expr)
    return eval(a2.sub(r'(\1)', expr))


a2 = re.compile(r'(\d+( \+ \d+)+)')
expressions = np.loadtxt('18.txt', 'U', delimiter='!')
sum([calculate_all2(e) for e in expressions])
