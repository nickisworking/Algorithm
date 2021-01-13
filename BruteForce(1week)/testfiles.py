def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

tet1 = [[1,1,1,1]]
tet2 = [[1,1],[1,1]]
tet3 = [[1,0],[1,0],[1,1]]
tet4 = [[1,0],[1,1],[0,11]]
tet5 = [[1,1,1],[0,1,0]]

print(tet3)
print("====================")

tet3 = rotated(tet3)
print(tet3)