from itertools import combinations
from copy import deepcopy
from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def bfs(coboard,n,m,virus_place) :

    c = 0
    visited = [[False for _ in range(m)] for k in range(n)]
    q = deque()
    
    for vp in virus_place :

        
        q.append(vp)
        visited[vp[0]][vp[1]] = True

        while q :
            front = q.popleft()

            for i in range(4) :
                newx = front[0] + dx[i]
                newy = front[1] + dy[i]

                if not (0 <= newx < n and 0<=newy<m) :
                    continue

                if visited[newx][newy] :
                    continue
                    
                if coboard[newx][newy] == 1 :
                    continue

                if coboard[newx][newy] == 0 :
                    coboard[newx][newy] = 2
                    visited[newx][newy] = True
                    q.append((newx,newy))
    
    for i in range(n) :
        for j in range(m) :
            if coboard[i][j] == 0 :
                c += 1
                
    return c

def solve(n,m,board) :

    count = float("-inf")
    
    zero_place = []
    virus_place = []

    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                zero_place.append((i,j))
            elif board[i][j] == 2 :
                 virus_place.append((i,j))   

    zero_combi = list(combinations(zero_place,3))

    for combi in zero_combi :

        coboard = deepcopy(board) 

        first = combi[0]
        sec = combi[1]
        third = combi[2]

        coboard[first[0]][first[1]] , coboard[sec[0]][sec[1]], coboard[third[0]][third[1]] = 1,1,1

        safe_count = bfs(coboard,n,m,virus_place)

        count = max(safe_count, count)

    print(count)

if __name__ == "__main__" :
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]

    solve(n,m,board)