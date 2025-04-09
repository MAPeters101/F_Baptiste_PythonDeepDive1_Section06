
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

