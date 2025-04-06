import random
#help(random.random)
print(random.random())
print()

l = [i for i in range(1,11)]
print(l)
print(sorted(l))
print(sorted(l, key=lambda x: random.random()))



