import sys


def solve(idx,count,N,arr,dp) :

    global min_val
    global flag

    if idx == N-1 :
        min_val = min(min_val,count)
        flag = True
        return 

    if idx >= N :
        if flag == True :
            return
        else :
            flag = False
            return
    
    if dp[idx] < count :
        return


    for i in range(1,arr[idx]+1) :
        if idx+i < N :
            dp[idx+i] = count+1
        solve(idx+i,count+1,N,arr,dp)

if __name__ == "__main__" :
    min_val = float("inf")
    flag = False

    N = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split(" ")))

    dp = [float("inf") for _ in range(N)]

    solve(0,0,N,arr,dp)

    if flag :
        print(min_val)
    else :
        print(-1)
        