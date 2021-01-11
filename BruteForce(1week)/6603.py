from itertools import combinations
import sys
from copy import deepcopy

def solve() :

    while True :
        a = list(map(int,sys.stdin.readline().split(" ")))
        k = deepcopy(a[0])
        S = deepcopy(a[1:])

        if k == 0 : return

        ans = list(combinations(S,6))

        for c in ans :
            print(" ".join(map(str,c)))
        
        print()

if __name__ == "__main__" :
    solve()
            
            










