from copy import deepcopy

min_val = float("inf")


def dfs(n,stations,w,visited,start) :
    
    global min_val
    
    if start >= n  :
        if sum(visited) == n :
            min_val = min(min_val, len(stations))
        return 
    
    if visited[start] == 1 :
        dfs(n,stations,w,visited,start+1)
    
    else :
        v = deepcopy(visited)
        st = deepcopy(stations)
        
        st.append(start+1)
        
        for i in range(w+1) :
            if start-i > 0 :
                v[start-i] = 1
            if start+i < n:
                v[start+i] = 1
        
        dfs(n,st,w,v,start+1+w)
        dfs(n,stations,w,visited, start+1)
            
    
def solution(n, stations, w):
    
    global min_val
    
    visited = [0 for _ in range(n)]
    
    for s in stations :
        for i in range(w+1) :
            if s-i-1 >= 0 :
                visited[s-i-1] = 1
            if s+i-1 < n :
                visited[s+i-1] = 1
    
    dfs(n,stations,w,visited,0)
    
    answer = min_val - len(stations)
    

    return answer