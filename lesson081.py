help(print)
help(int)

def my_func(a, b=1):
    return a * b

help(my_func)
print('.'*80)

def my_func(a, b=1):
    'returns a * b'
    return a * b

help(my_func)
print()

def my_func(a, b=1):
    '''returns a * b

    some additional docs here

    Inputs:

    Outputs:
    '''
    return a * b

help(my_func)
print()

def my_func(a, b=1):
    # some comment here
    '''returns a * b

    some additional docs here

    Inputs:

    Outputs:
    '''
    return a * b

help(my_func)
print()

def my_func(a, b=1):
    # some comment here
    'some string here'
    '''returns a * b

    some additional docs here

    Inputs:

    Outputs:
    '''
    return a * b

help(my_func)
print()

def my_func(a, b=1):
    # some comment here
    i = 10
    '''returns a * b

    some additional docs here

    Inputs:

    Outputs:
    '''
    return a * b

help(my_func)
print()

def my_func(a, b=1):
    # some comment here
    '''returns a * b

    some additional docs here

    Inputs:

    Outputs:
    '''
    return a * b

help(my_func)
print()
print('-'*80)

print(my_func.__doc__)
print('-'*80)

def my_func(a: 'annotation for a',
            b: 'annotation for b' = 1) -> 'something with a long annotation for the return value':
    """Documentation for my_func"""
    return a * b
help(my_func)
print(my_func.__doc__)
print(my_func.__annotations__)
print()

x = 3
y = 5
def my_func(a: 'some character', b=max(x,y)) -> 'character a repeated ' + str(max(x, y)) + ' times':
    print(b)
    return a * max(x, y)
print(my_func('a'))
print(my_func.__annotations__)
print()

x=10
print(my_func('a'))
print(my_func.__annotations__)
print('-'*80)

def my_func(a: str,
            b: 'int > 0' = 1,
            *args: 'some extra positional args',
            k1: 'keyword-only arg 1',
            k2: 'keyword-only arg 2' = 100,
            **kwargs: 'some extra keyword-only args') -> 'something':
    print(a, b, args, k1, k2, kwargs)
help(my_func)
print(my_func.__annotations__)
print()
my_func(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)





