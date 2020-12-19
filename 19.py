# import numpy as np
import re


def parse(fn):
    with open(fn) as f:
        rules = {}
        while True:
            line = f.readline().strip()
            if not line:
                break
            nr, x = line.split(': ')
            rules[nr] = ''.join(x).strip('"')
        messages = [line.strip() for line in f.readlines()]
    return rules, messages


def resolve(rule, i=-1):
    if i == 0:  # Limit the recursion depth.
        return ''
    new_rule = ''
    for c in rules[rule].split(' '):
        if c.isdigit():
            new_rule += '({})'.format(resolve(c, i-1))
        else:
            new_rule += c
    rules[rule] = new_rule
    return new_rule


##########
# Part 1 #
##########

rules, messages = parse('19.txt')
a = re.compile(resolve('0'))
len([m for m in messages if a.fullmatch(m)])

##########
# Part 1 #
##########

rules, messages = parse('19.txt')
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'
a = re.compile(resolve('0', 20))  # Seems to be stable after recursion depth limit of 15.
len([m for m in messages if a.fullmatch(m)])
