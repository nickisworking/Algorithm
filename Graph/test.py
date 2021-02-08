from itertools import permutations

a = [1,3]

combi = list(permutations(a,2))

for s in combi :
    print(list(s))