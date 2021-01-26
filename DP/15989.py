import sys

if __name__ == "__main__" :
    input = sys.stdin.readline

    T = int(input())

    while T :
        N = int(input())
        dp = [0 for i in range(10001)]
        dp[0] = 1
        for i in range(1,4) :
            for j in range(i,N+1) :
                dp[j] += dp[j-i]
        print(dp[N])
        T -=1


