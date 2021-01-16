def solution(n, stations, w):
    answer = 0   
    stations_idx = 0
    location = 1
    count = 0
    
    while location <= n :   
        if stations_idx < len(stations) and stations[stations_idx]-w <= location <= stations[stations_idx]+w :
            location = stations[stations_idx]+w+1
            stations_idx +=1
        else :
            print(location)
            location += 2*w+1
            answer+=1
        
    return answer