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



