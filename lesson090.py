def fact(n):
    return 1 if n<2 else n*fact(n-1)

print(fact(3))
print(fact(4))

results = map(fact, range(6))
print(results)
for x in results:
    print(x)
print('.'*20)

for x in results:
    print(x)
print('.'*20)

results = list(map(fact, range(6)))
print(results)
print('-'*80)


