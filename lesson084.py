help(sorted)

l = [1,5,4,10,9,6]
print(l)
print(sorted(l))
print()
l = ['c', 'B', 'D', 'a']
print(l)
print(sorted(l))
print()
print(ord('a'))
print(ord('A'))
print()

print(sorted(l, key=lambda s: s.upper()))
print('-'*80)

d = {'abc': 200, 'def': 300, 'ghi':100}
for e in d:
    print(e)
print(sorted(d))
print(sorted(d, key= lambda e: d[e]))
print('-'*80)

def dist_sq(x):
    return (x.real)**2 + (x.imag)**2
print(dist_sq(1+1j))
l = [3+3j, 1-1j, 0, 3]
#print(sorted(l))
print(sorted(l, key=dist_sq))
print(sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2))
print('-'*80)





