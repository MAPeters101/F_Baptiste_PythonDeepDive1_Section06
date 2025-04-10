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

