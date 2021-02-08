import sys

sys.setrecursionlimit(10**9)

dx = [-1,0,1,1,0,-1]
dy = [0,-1,-1,0,1,1]

ans = 0

def main() :
    def dfs(startx, starty,color,board,char_board,n) :
        global ans
        
        board[startx][starty] = color
        ans = max(ans,1)
        
        for i in range(6) :
            newx = startx+dx[i]
            newy = starty+dy[i]
            
            #범위체크
            if newx<0 or newx>=n or newy<0 or newy>=n : continue
            #범위여도 X가 아니면 끝
            if char_board[newx][newy] != "X" : continue
            #범위고 X고 아직 칠하지 않은 칸이면 DFS
            if board[newx][newy] == -1 : dfs(newx,newy,1-color,board,char_board,n)
            ans = max(2,ans)
            if board[newx][newy] == color :
                ans = max(3,ans)

    N = int(sys.stdin.readline())
    char_board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    board = [[-1 for i in range(N)] for _ in range(N)]


    for i in range(N) :
        for j in range(N) :
            if char_board[i][j] == 'X' and board[i][j] == -1 :
                dfs(i,j,0,board,char_board,N)
    
    print(ans)


if __name__ == "__main__" :
    sys.exit(main())