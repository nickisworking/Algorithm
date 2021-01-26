import sys


def solve(N,arr) :
    dp = [float("inf") for i in range(N)]

    dp[0] = 0

    for i in range(N) :
        for k in range(arr[i]+1) :
            if i+k < N:
                dp[i+k] = min(dp[i]+1, dp[i+k])
    
    return dp[-1]

if __name__ == "__main__" :
    N = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split(" ")))
    ans = solve(N,arr)

    if ans == float("inf") :
        print(-1)
    else :
        print(ans)



    


    

        