num = int(input())

sodduck_ls = list(input())

# 짝수일때 비교 인덱스 , 0 ~ n/2 -1 , n/2 ~ n-1
# 홀수일때, 0 ~ n//2 -1 , n//2 + 1 ~ n-1
answer = 0

if num % 2 == 0 :
    for i in range(num//2):
        if sodduck_ls[i] != sodduck_ls[num-1-i]:
            answer += 1
else:
    for i in range(num//2):
        if sodduck_ls[i] != sodduck_ls[num-1-i]:
            answer += 1

print(answer)


