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

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')

obj = MyClass()
print(obj)
print(obj.a)
print(obj.b)
print(obj.test)
obj.test()

print(operator.attrgetter('a'))
prop_a = operator.attrgetter('a')
print(prop_a(obj))
#print(prop_a())
print()

my_var = 'b'
#print(obj.my_var)
print(operator.attrgetter(my_var))
print(operator.attrgetter(my_var)(obj))
prop_b = operator.attrgetter(my_var)
print(prop_b(obj))
print()

print(prop_b(obj))
my_var = 'c'
print(prop_b(obj))
print('-'*80)

print(operator.attrgetter('a', 'b')(obj))
a, b, test = operator.attrgetter('a', 'b', 'test')(obj)
print(a)
print(b)
print(test)
test()
print('-'*80)

f = lambda x: x.a
print(f(obj))
print()

f = lambda x: x[2]
x = [1,2,3,4]
print(f(x))
print()

f = lambda x: (x[2], x[3])
x = [1,2,3,4]
print(f(x))
print()
print('-'*80)

a = 5 + 10j
print(a)
print(a.real)
print()

l = [5-10j, 3+3j, 2-100j]
#print(sorted(l))
print(sorted(l, key=lambda x: x.real))
print(sorted(l, key=operator.attrgetter('real')))
print('-'*80)

l = [(2,3,4), (1,3,5),(6,), (4,100)]
print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=operator.itemgetter(0)))
print('-'*80)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')

obj = MyClass()
f = operator.attrgetter('test')
print(f(obj))
f(obj)()
print()

f = operator.methodcaller('test')
f(obj)
print('-'*80)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def test(self, c):
        print(self.a, self.b, c)

obj = MyClass()
print(obj.a)
print(obj.b)
#obj.test()
obj.test(100)
print()

#operator.methodcaller('test')(obj)
operator.methodcaller('test', 300)(obj)
print('-'*80)

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def test(self, c, d):
        print(self.a, self.b, c, d)

obj = MyClass()
print(obj.a)
print(obj.b)
#obj.test()
obj.test(100, 200)
print()

#operator.methodcaller('test')(obj)
operator.methodcaller('test', 300, 400)(obj)
print('-'*80)

