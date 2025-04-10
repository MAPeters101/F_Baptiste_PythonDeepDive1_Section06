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

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)
my_func(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)

def f(x, *vars, kw, **kwvars):
    return my_func(10, x, *vars, k1='a', k2=kw, **kwvars)

f(20, 100, 200, kw='b',k3=1000, k4=2000)
print('-'*80)


