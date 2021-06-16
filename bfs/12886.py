g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]

def get_sum(x) :
    
    sum_val = 0
    for comp in x :
        sum_val += comp[1]
    return sum_val



def solution(genres, plays):
    answer = []
    
    genres_dict = dict()
    
    for i in range(len(genres)) :
        if genres[i] in genres_dict :
            genres_dict[genres[i]].append([i,plays[i]]) 
        else :
            genres_dict[genres[i]] = [[i,plays[i]]]

    for key in genres_dict.keys() :
        genres_dict[key].sort(key = lambda x : (-x[1],x[0]))

    print("here!!!!!")
    print(genres_dict.items())
    print()

    sorted_dict = sorted(genres_dict.items(), key = lambda x : get_sum(x[1]), reverse=True)

    for item in sorted_dict :
        if(len(item[1])<=1) :
            answer.append(item[1][0][0])
        else :
         for i in range(2) :
            answer.append(item[1][i][0])

    print(answer)
    
    
    return answer
    
    
    
    


solution(g, p)
