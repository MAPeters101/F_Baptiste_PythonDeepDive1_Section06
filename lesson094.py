from functools import partial
def my_func(a,b,c):
    print(a,b,c)
my_func(10,20,30)
print()

def f(x, y):
    return my_func(10, x, y)
f(20, 30)
f(100, 200)
print('-'*80)

f = lambda x, y: my_func(10, x, y)
f(100, 200)
print('-'*80)

f = partial(my_func, 10)
f(20,30)
print()
f = partial(my_func, 10, 20)
f(30)
#f(10, 20)
print('-'*80)


