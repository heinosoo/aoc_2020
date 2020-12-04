import numpy as np


##########
# Part 1 #
##########


def check_passport1(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return np.all([field in passport for field in req_fields])


with open('04.txt') as f:
    lines = [line.strip('\n') for line in f.readlines()]
passports = np.split(lines, np.where(np.array(lines) == '')[0])
passports = [' '.join(p).strip().split(' ') for p in passports]
passports = [{field.split(':')[0]:field.split(':')[1] for field in p} for p in passports]

np.count_nonzero(np.vectorize(check_passport1)(passports))

##########
# Part 2 #
##########


def check_passport2(p):
    if not check_passport1(p):
        return False

    if not 1920 <= int(p['byr']) <= 2002:
        return False
    elif not 2010 <= int(p['iyr']) <= 2020:
        return False
    elif not 2020 <= int(p['eyr']) <= 2030:
        return False

    if 'cm' in p['hgt'] and 150 <= int(p['hgt'].split('cm')[0]) <= 193:
        pass
    elif 'in' in p['hgt'] and 59 <= int(p['hgt'].split('in')[0]) <= 76:
        pass
    else:
        return False

    ht = '0123456789abcdef'
    if not p['hcl'][0] == '#' or not all([c in ht for c in p['hcl'][1:]]):
        return False

    et = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not p['ecl'] in et:
        return False

    d = '0123456789'
    if not len(p['pid']) == 9 or not all([c in d for c in p['pid']]):
        return False

    return True


np.count_nonzero(np.vectorize(check_passport2)(passports))
