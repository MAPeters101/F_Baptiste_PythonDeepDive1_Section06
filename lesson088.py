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


