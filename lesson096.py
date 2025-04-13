import operator
from pprint import pprint

pprint(dir(operator))
print('-'*80)

print(1+2)
print(operator.add(1,2))
print(operator.truediv(3,2))
print(operator.floordiv(13,2))
print(13//2)
print('-'*80)

from functools import reduce
print(reduce(lambda x,y: x*y, [1,2,3,4]))
print(reduce(operator.mul, [1,2,3,4]))

