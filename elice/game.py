from itertools import combinations

# def solve(n,m,time_list) :
#     comb = list(combinations(time_list,m))
#     ret = []

#     for c in comb :
#         result = check_overlapped(n,m,c)
#         if result == -1 :
#             continue
#         ret.append(result)    
    
#     if not ret :
#         return -1

#     return min(ret)

def swap(tup) :
    if tup[0] > tup[1] :
        return (tup[1],tup[0])
    return tup


def swap(tup) :
    if tup[0] > tup[1] :
        return (tup[1],tup[0])
    return tup


def check_overlapped(n,m,time_list) :
    time_list = list(map(lambda x : swap(x), time_list))
    sorted_time_list = sorted(time_list,key = lambda x : x[0]) #시작 시간으로 정렬
    stack = []
    people_count = 0

    if m == 1 :
        return sorted_time_list[0][0]

    for i in range(0,len(sorted_time_list)) :
        time = sorted_time_list[i]

        if not stack :
            stack.append(time)
            people_count = 1
            continue
        
        top = stack.pop()

        if top[1] >= time[0] and top[0] <= time[1] :
            overlapped = (max(top[0],time[0]),min(top[1],time[1]))
            stack.append(overlapped)
            people_count += 1
        else :
            stack = []
            stack.append(time)
            people_count = 1
    
        if people_count == m  :
            return stack[-1][0]

    return -1


if __name__ == "__main__" :
    
    n,m = map(int,input().split())

    if m > n :
        print(-1)
    else :     
        time_list = [tuple(map(int,input().split())) for _ in range(n)]
        # print("-===")
        result = check_overlapped(n,m,time_list)
        print(result)
