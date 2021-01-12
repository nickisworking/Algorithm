import sys

count  = 0

def dfs(idx,sum,n,s,a) :
    if idx >= n :
        return

    if sum+a[idx] == s   :
        global count
        count+=1

    dfs(idx+1,sum,n,s,a)
    dfs(idx+1,sum + a[idx],n,s,a) 


def solve() :
    n,s = map(int,sys.stdin.readline().split())

    global count
    count = 0

    a = list(map(int,sys.stdin.readline().split()))
    dfs(0,0,n,s,a)

    print(count)

if __name__ == "__main__" :
    solve()
