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
print('-'*80)

print(operator.lt(10,3))
from operator import is_
print(is_('abc', 'def'))
print(is_('abc', 'abc'))
print()
print(operator.truth([]))
print(operator.truth([1]))
print('-'*80)

my_list = [1,2,3,4]
print(my_list[1])
print(operator.getitem(my_list, 1))
print()
my_list[1] = 100
print(my_list)
del my_list[3]
print(my_list)
my_list = [1,2,3,4]
operator.setitem(my_list, 1, 100)
print(my_list)
operator.delitem(my_list, 3)
print(my_list)
print('-'*80)

f = operator.itemgetter(2)
print(f)
print(type(f))
#f()
my_list = [1,2,3,4]
print(f(my_list))
s = 'python'
print(f(s))
print('-'*80)

f = operator.itemgetter(2,3)
print(type(f))
my_list = [1,2,3,4]
print(f(my_list))
print()

f = operator.itemgetter(1,2,3)
my_list = [1,2,3,4]
print(f(my_list))
print()

f = operator.itemgetter(2,3,4)
my_list = [1,2,3,4]
#print(f(my_list))
print()

f = operator.itemgetter(2,3)
print(f('python'))
print()
print('-'*80)



