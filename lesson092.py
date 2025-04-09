
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
#print(_reduce(_add, {1,3,4,5}))
print('-' * 80)



