import math


def solution(fees, records):
    answer = []
    
    d = {}
    id_ls = []
    for s in records:
        ls = s.split()
        number = ls[1]
        
        id_ls.append(ls[1])
        
        time = int(ls[0][0:2])*60
        time += int(ls[0][3:])
        
        if number in d:
            d[number].append(time)
        else:
            d[number] = [time]
    
    
    id_ls.sort()
                     
    for id in id_ls:
        ls = d[id]
        
        diff = 0             
        for i in range(0, len(ls)-1, 2):
            diff += ls[i+1] - ls[i]
        if len(ls) % 2 == 1:
            diff += 1439 - ls[-1] 
        
        if diff < fees[0]:
            answer.append(fees[1])
        else:
            a = math.ceil(((diff - fees[0])/fees[2])*fees[3])  
            answer.append(fees[1] + a)
                     
    
    return answer


solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])