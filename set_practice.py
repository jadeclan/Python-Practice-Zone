setA = set([1,2,3,4,5,'a','b','c',3])
print(setA)

setB = {1,3,5,'c','q'}
print(setB)

print(f'{setA.intersection(setB)}')

print(f'{setA.union(setB)}')
print(f'{setA | setB}')