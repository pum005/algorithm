
bbang , patty = map(int, input().split())

answer = 0

while bbang != 0 and patty != 0 :
    bbang -= 1
    if bbang != 0:
        bbang -= 1
        patty -= 1
        answer += 1

print(answer)