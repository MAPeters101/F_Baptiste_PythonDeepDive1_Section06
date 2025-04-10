
l = [5,8,6,10,9]
_max = lambda x, y: x if x > y else y
print(_max(3,4))
print(_max(10,2))
print()

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))
print('-'*80)

_min = lambda a, b: a if a < b else b
def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

print(min_sequence(l))
print('-'*80)

_add = lambda a, b: a+b
def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result

print(add_sequence(l))
print('-'*80)

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(_reduce(_max, l))
print(_reduce(_min, l))
print(_reduce(_add, l))
#print(_reduce(_max, {1,3,4,5}))
print('-' * 80)

from functools import reduce
print(reduce(_max, l))
print(reduce(_add, l))
print(reduce(_max, {1,3,4,5}))
print()
print(min(l))
print(max(l))
print(sum(l))
print(sum({1,2,3}))
print('-' * 80)

s = {True, 1, 0, None}
print(all(s))
s2 = {True, 1,"s"}
print(all(s2))
print(bool(True) and bool(l) and bool('s'))
print(bool(True) and bool(l) and bool(0) and bool(None))
print('-' * 80)

print(any(s))
print(any(s2))
s3 = {False, 0, '', None}
print(any(s3))
print('-' * 80)

print(reduce(lambda a, b: bool(a) and bool(b), s))
print(reduce(lambda a, b: bool(a) or bool(b), s3))
print('-' * 80)

l = [5,8,6,10,9]
print(reduce(lambda a,b: a*b, l))

l = [1,2,3,4] # = 4!
print(reduce(lambda a,b: a*b, l))
print(range(5))
print(range(5)[0])
print(list(range(5)))
print(list(range(1,5+1)))
print(reduce(lambda a, b: a*b, range(1,5+1)))
def fact(n):
    return 1 if n < 2 else n * fact(n-1)
print(fact(5))
print()

def fact(n):
    return reduce(lambda a, b: a*b, range(1,n+1))
print(fact(5))
print(fact(2))
print(fact(2))
print('-'*80)

def _reduce(fn, sequence, initial):
    result = initial
    for x in sequence:
        result = fn(result, x)
    return result
l = [1,2,3,4] # = 4!
print(_reduce(lambda a, b: a+b, l, 0))
print(_reduce(lambda a, b: a+b, l, 100))
print(_reduce(lambda a, b: a+b, {1,2,3,4}, 0))
print(_reduce(lambda a, b: a+b, {1,2,3,4}, 100))
print()

print(reduce(lambda a, b: a+b, {1,2,3,4}, 0))
print(reduce(lambda a, b: a+b, {1,2,3,4}, 100))
print()






