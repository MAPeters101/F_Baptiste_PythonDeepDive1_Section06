from pprint import pprint

def my_func(a: "mandatory positional",
            b: "optional positional" =1,
            c=2,
            *args: "add extra positional here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "provide extra kw-only here") -> "does nothing":
    """This function does nothing but does have various parameters
    and annotations"""
    i = 10
    j = 20

print(my_func.__doc__)
print(my_func.__annotations__)
pprint(my_func.__annotations__)
#print(my_func.short_description)
my_func.short_description = "This is a function that does nothing much"
print(my_func.short_description)
print(dir(my_func))
pprint(dir(my_func))
print('-'*80)

print(my_func.__name__)
print(hex(id(my_func)))
def func_call(f):
    print(hex(id(f)))
    print(f.__name__)

func_call(my_func)
print('-'*80)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print('-'*80)

print(my_func.__code__)
print(dir(my_func.__code__))
pprint(dir(my_func.__code__))
print()
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)
print('-'*80)

import inspect
from inspect import isfunction, ismethod, isroutine
a = 10
print(isfunction(a))
print(isfunction(my_func))
print(ismethod(my_func))
print(isroutine(my_func))
print('-'*80)

class MyClass:
    def f(self):
        pass

print(isfunction(MyClass.f))
my_obj = MyClass()
print(isfunction(MyClass.f))
print(isfunction(my_obj.f))
print(ismethod(my_obj.f))
print()
print(isroutine(MyClass.f))
print(isroutine(my_obj.f))
print('-'*80)

def my_func(a: "mandatory positional",
            b: "optional positional" =1,
            c=2,
            *args: "add extra positional here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "provide extra kw-only here") -> "does nothing":
    """This function does nothing but does have various parameters
    and annotations"""
    i = 10
    j = 20
    a = i + j
    return a

inspect.getsource(my_func)
print()

print(inspect.getsource(my_func))
print()

f = my_func
print(inspect.getsource(f))
print('-'*80)

print(inspect.getmodule(my_func))
pprint(inspect.getmodule(my_func))
print()
print(inspect.getmodule(print))
print()

import math
print(inspect.getmodule(math.sin))
print('-'*80)



