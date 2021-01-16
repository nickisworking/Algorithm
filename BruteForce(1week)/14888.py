import sys
from copy import deepcopy
"""
op = ["+","-","*","/"]
"""
op = ["+","-","*","/"]

max = float("-inf")
min = float("inf")

def do_operation(ope,val1, val2) :
    if ope == "+" :
        return val1+val2
    elif ope == "-" :
        return val1-val2
    elif ope =="*" :
        return val1*val2
    elif ope == "/" :
        if val1 < 0 :
            val1 = -(val1)
            return -(val1//val2)
        else :
            return val1//val2 


def dfs(n,a,operators,idx,sum) :
    global max,min

    if idx == n :
        if max < sum :
            max = sum
        if min > sum :
            min = sum
        return
        
    for i in range(4) :
        copied_operators = deepcopy(operators)
        if copied_operators[i] > 0  :
            copied_operators[i] -= 1
            dfs(n,a,copied_operators,idx+1,do_operation(op[i],sum,a[idx]))
            
def solve() :
    n = int(sys.stdin.readline())
    a = list(map(int,sys.stdin.readline().split()))
    operators = list(map(int,sys.stdin.readline().split()))

    dfs(n,a,operators,1,a[0])

    print(max)
    print(min)



if __name__ == "__main__" :
    solve()