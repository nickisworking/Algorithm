import sys
from itertools import combinations

def solve() :
    n,s = map(int,sys.stdin.readline().split())

    a = list(map(int,sys.stdin.readline().split()))

    count = 0

    for i in range(1,n+1) :
        sub = list(combinations(a,i))
        for c in sub :
            if sum(c) == s :
                count +=1
                
    print(count)


if __name__ == "__main__" :
    solve()
