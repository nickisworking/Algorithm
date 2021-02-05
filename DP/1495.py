import sys

N,S,M = map(int, sys.stdin.readline().split(" "))
v = list(map(int,sys.stdin.readline().split(" ")))
v.insert(0,0)

dp = [[0 for i in range(M+1)] for _ in range(N+1)]

if S + v[0] <= M : dp[1][S+v[0]] = True
if S - v[0] >= 0 : dp[1][S-v[0]] = True

possible_list = []








