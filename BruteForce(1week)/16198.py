import sys
from copy import deepcopy

max_val = float("-inf")

def dfs(idx,sum_val,N,w) :
    global max_val

    if  (idx-1) < 0 or (idx+1) >= len(w) or len(w) <= 2 :
        return

    for i in range(idx,len(w)-1) :    

        sum1 = sum_val+(w[i-1] * w[i+1])
        max_val = max(max_val, sum1)
        
        w_copied = deepcopy(w)
        
        del w_copied[i]

        dfs(1,sum1, N, w_copied)
        #dfs(i+1,sum_val, N, w)


def solve() :
    global max_val

    N = int(sys.stdin.readline())
    w = list(map(int, sys.stdin.readline().split(" ")))

    dfs(1,0,N,w)
    print(max_val)



if __name__ == "__main__" :
    solve()
    
