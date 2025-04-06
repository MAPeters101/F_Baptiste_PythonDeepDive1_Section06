
def sq(x):
    return x**2

print(type(sq))
print()

print(lambda x: x**2)
print(lambda x,y: x+y)
print()

f = sq
print(hex(id(f)))
print(hex(id(sq)))
print()

print(f(3))
print(sq(3))
print()

print(f)
print(sq)
print()

f = lambda x: x**2
print(f(3))
print()

g = lambda x, y=10: x+y
print(g)
print(g(1, 2))
print(g(1))
print('-'*80)

