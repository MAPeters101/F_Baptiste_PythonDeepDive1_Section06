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

l1 =[1,2,3,4,5]
l2 = [10, 20, 30]

results = list(map(lambda x, y: x+y, l1, l2))
print(results)
print()

l1 =[1,2,3,4,5]
l2 = [10, 20, 30]
l3 = 100,200,300,400
results = list(map(lambda x, y, z: x+y+z, l1, l2, l3))
print(results)
print('-'*80)

l1 =[1,2,3,4,5]
l2 = [10, 20, 30]
l3 = 100,200,300,400
results = map(lambda x, y: x+y, l1, l2, l3)
print(results)
# for x in results:
#     print(x)



print('-'*80)




