import sys
from collections import deque

sys.setrecursionlimit(10**9)

def main() :

    def dfs(start,count,current,visited,subway):

        if count >=3 and start == current :
            return True

        if(visited[current]) :
            return

        visited[current] = True
        
        for point in subway[current] :
            if(dfs(start,count+1,point,visited,subway)) :
                return True

        return False
    
    def bfs(is_cycle,distance,subway) :
        q= deque()

        for i in range(1,len(is_cycle)) :
            if is_cycle[i] == True :
                q.append(i)
        
        while q :
            front = q.popleft()
            for next in subway[front] :
                if is_cycle[next] == False :
                    is_cycle[next] = True
                    q.append(next)
                    distance[next] = distance[front]+1 

        for s in range(1,len(distance)) :
            print(distance[s], end=" ")
            


    N = int(sys.stdin.readline())

    subway = [[] for _ in range(N+1)]

    is_cycle = [False for _ in range( N+1)]

    distance = [0 for _ in range(N+1)]

    for i in range(N) :
        x,y = map(int,sys.stdin.readline().split())
        subway[x].append(y)
        subway[y].append(x)

    for i in range(1,N+1) :
        visited = [False for _ in range(N+1)]
        check_cycle = dfs(i,0,i,visited,subway)
        is_cycle[i] = check_cycle
    
    bfs(is_cycle,distance,subway)
    





if __name__ == "__main__" :
    sys.exit(main())


    


