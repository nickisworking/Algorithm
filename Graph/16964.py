import sys
from collections import deque
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline
ans_list = []

def dfs(node, visited, tree) :
    if(visited[node] == True) :return
    visited[node] = True
    ans_list.append(node)

    for element in tree[node] :
        if visited[element] == False :
            dfs(element,visited,tree)

def solve(n, tree, order) :

    visited = [False for i in range(n+1)]
    

    rank = [-1 for i in range(n+1)]

    for i in range(1,n+1) :
        rank[order[i-1]] = i 
    
    
    for i in range(1,n+1) :
        tree[i] = sorted(tree[i], key=lambda x : rank[x])

    dfs(1,visited,tree)

    if ans_list == order :
        print(1)
    else :
        print(0)



if __name__ == "__main__" :
    n = int(input())
    tree = [[] for _ in range(n+1)]
    
    for _ in range(1,n) :
        x,y = map(int,input().split())
        tree[x].append(y)
        tree[y].append(x)

    order = list(map(int,input().split()))


    solve(n,tree,order)    




