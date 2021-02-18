from collections import deque
import sys
input = sys.stdin.readline

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def solve(n,x,y,endx,endy) :

    board = [[-1 for i in range(n)] for i in range(n)]
    visit = [[False for i in range(n)] for i in range(n)]
    

    board[x][y] = 0
    visit[x][y] = True

    q = deque()

    q.append((x,y))

    while q :

        front = q.popleft()

        for i in range(6) :            
            newx = front[0] + dx[i]
            newy = front[1] + dy[i]

            if not (0 <= newx < n and 0<=newy<n) :
                continue
            
            if visit[newx][newy] == True :
                continue

            visit[newx][newy] = True
            board[newx][newy] = board[front[0]][front[1]]+1
            q.append((newx,newy))
    
    print(board[endx][endy])
    

if __name__ == "__main__" :
    
    n = int(input())

    x,y,endx,endy = map(int,input().split())

    solve(n,x,y,endx,endy)
