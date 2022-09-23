def solution(id_list, report, k):
    answer = []
    
    stop_list = []
    
    d = {}
    id_dic = {}
    
    for i, id in enumerate(id_list):
        id_dic[id] = i
    
    for i in range(len(id_list)):
        answer.append(0)
        
    for s in report:
        ls = s.split()
        id = ls[0]
        aim = ls[1]
        
        if aim in d:
            d[aim] += 1
        else:
            d[aim] = 1
    
    for key in d:
        if d[key] >= k:
            stop_list.append(key)
    
    for s in report:
        ls = s.split()
        id = ls[0]
        aim = ls[1]
        
        if aim in stop_list:
            answer[id_dic[id]] += 1

        
    return answer


solution(["muzi", "frodo", "apeach" , "neo"], ["muzi frodo" , "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2)

# print(1)