import sys
input = sys.stdin.readline



def solve(n,k,arr) :
    
    arr = sorted(arr,key=lambda x: x[0])
    arr.insert(0, (0,0))

    dp = [[0 for i in range(k+1)] for _ in range(n+1)]  #물건/무게


    # 점화식은??
    # DP[i][j] : i번째까지 썼을 때 j의 무게를 담았을 때의 최대 무게
    # 그럼 dp[i][j] = arr[i]를 담았을 때 -> dp[i-1][j] + arr[i] / arr[i] or 안 담았을 때 dp[i-1][j]

    for i in range(1,n+1) :
        for j in range(1,k+1) :
            if arr[i][0] > j :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1]) 

    print(max(dp[n]))


if __name__ == "__main__" :
    n,k = map(int, input().split())
    arr =[]

    for i in range(n) :
        wv = tuple(map(int,input().split()))
        arr.append(wv)
    
    solve(n,k,arr)


    