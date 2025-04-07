print(callable(print))
result = print('hello')
print(result)
print()

l = [1,2,3]
print(callable(l.append))
result = l.append(4)
print(l)
print(result)
print()

s = 'abc'
print(callable(s.upper))
print(callable(s.upper()))
result = s.upper()
print(result)
print(hex(id(result)))
print(hex(id(s.upper())))
print(hex(id(s.upper)))
print(result == s.upper())
print(result is s.upper())
print('-'*80)

from decimal import Decimal
print(callable(Decimal))
a = Decimal('10.5')
print(a)
print(type(a))
print(callable(a))
print('-'*80)

class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x
print(callable(MyClass))
a = MyClass(100)
print(a.counter)
print(callable(a))
print('-'*80)

