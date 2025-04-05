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


