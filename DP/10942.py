import sys

if __name__ == "__main__" :
    input = sys.stdin.readline

    N = int(input())
    dp = [[0 for i in range(N)] for _ in range(N)]

    arr = list(map(int,input().split()))

    
    for i in range(N) :
        for start_idx in range(N) :
            end_idx = start_idx + i

            if end_idx >= N :
                break
            if start_idx == end_idx :
                dp[start_idx][end_idx] = 1
                continue
            if start_idx+1 == end_idx :
                if arr[start_idx] == arr[end_idx] :
                    dp[start_idx][end_idx] = 1
                    continue
            
            if arr[start_idx] == arr[end_idx] and dp[start_idx+1][end_idx-1] :
                dp[start_idx][end_idx] = 1

        
    
    # for i in range(N-1) :
    #     if arr[i] == arr[i+1] :
    #         dp[i][i+1] = 1
       
    # #길이가 3 이상
    # for i in range(2,N) :        
    #     for j in range(N-i) :
    #         if arr[j] == arr[j+i] and dp[j+1][j+i-1] == 1 :
    #             dp[j][j+i] = 1

    M = int(input())

    for i in range(M) :
        s,e = map(int,input().split())
        print(dp[s-1][e-1])
