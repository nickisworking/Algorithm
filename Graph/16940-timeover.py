import sys
from collections import deque
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline
ans_list = []

def bfs(n,now_string,tree,q,visited) :

    if len(now_string) == n :
        ans_list.append(now_string)
        return
    
    if q :
        front = q.popleft()
        combi = list(permutations(tree[front],len(tree[front])))

        for c in combi :
            temp = list(c)
            new_q = deepcopy(q)
            new_visit =deepcopy(visited)
            new_string = now_string
            
            for k in temp :
                if new_visit[k] == False :
                    new_visit[k] = True
                    new_string += str(k)
                    new_q.append(k)            
                
            bfs(n,new_string,tree,new_q,new_visit)
    
    

def solve(n, tree, order) :

    visited = [False for i in range(n+1)]
    q = deque()

    q.append(1)
    visited[1] = True

    bfs(n,"1",tree,q,visited)

    order_cmp = order.replace(" ","").rstrip()


    for s in ans_list :
        if s == order_cmp :
            print(1)
            return

    print(0)
        

if __name__ == "__main__" :
    n = int(input())
    tree = [[] for _ in range(n+1)]
    
    for _ in range(1,n) :
        x,y = map(int,input().split())
        tree[x].append(y)
        tree[y].append(x)

    order = input()


    solve(n,tree,order)    




