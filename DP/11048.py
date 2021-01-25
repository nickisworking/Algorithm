import sys

def solve(N,M) :

    miro = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(N)]

    dp = [[0 for i in range(M+1)] for i in range(N+1)]

    for i in range(1,N+1) :
        for j in range(1,M+1) :
            current = miro[i-1][j-1]
            dp[i][j] = max(max(current+dp[i-1][j], current+dp[i][j-1]),current+dp[i-1][j-1])

    return dp[-1][-1]
    

if __name__ == "__main__" :
    N,M = map(int,sys.stdin.readline().split(" "))
    ans = solve(N,M)
    print(ans)

