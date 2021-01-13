import sys
from copy import deepcopy


maxval = 0

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def check(board, tet,n,m) :
    global maxval
    x_len = len(tet)
    y_len = len(tet[0])
    for startx in range(n) :
        if startx + (x_len-1) >= n :
            continue  
        for starty in range(m) : 
            sumval = 0
            if starty+(y_len-1) >= m :
                continue
            for j in range(x_len) :
                for i in range(y_len) :
                    if tet[j][i] == 1 :
                        sumval += board[startx+ j][starty+i] 
            maxval = max(sumval,maxval)
                    
def solve() :
    n , m = map(int,sys.stdin.readline().split())    
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    tet1 = [[1,1,1,1]]
    tet2 = [[1,1],[1,1]]
    tet3 = [[1,0],[1,0],[1,1]]
    tet4 = [[1,0],[1,1],[0,1]]
    tet5 = [[1,1,1],[0,1,0]]
    tet6 = [[0,1],[1,1],[1,0]]
    tet7 = [[0,1],[0,1],[1,1]]
    tet = [tet1,tet2,tet3,tet4,tet5,tet6,tet7]

    for t in tet :
        for _ in range(4):
            check(board,t,n,m)
            t = rotated(t)

    print(maxval)

if __name__ == "__main__" :
    solve()