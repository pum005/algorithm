
from collections import deque


n = int(input())

graph = [[] for i in range(n+1)]

for i in range(1 , n+1):
    graph[i] = [' '] + list(map(int, input()))

visited = [[False] * (n+1) for i in range(n+1)]

result = []

def bfs(x, y):
    dx = [-1, 1, 0 , 0]
    dy = [0 , 0 ,-1, 1]

    house_cnt = 0

    q = deque()

    if graph[x][y] != 0 and visited[x][y] == False:
        q.append([x,y])

    while q:
        x,y = q.popleft()

        house_cnt += 1

        if x+dx[0] >= 1 and graph[x+dx[0]][y] != 0 and visited[x+dx[0]][y] == False:
            q.append([x+dx[0] , y])
            visited[x+dx[0]][y] = True
        if x+dx[1] <= n and graph[x+dx[1]][y] != 0 and visited[x+dx[1]][y] == False:
            q.append([x+dx[1] , y])
            visited[x+dx[1]][y] = True
        if y+dy[2] >= 1 and graph[x][y+dy[2]] != 0 and visited[x][y+dy[2]] == False:
            q.append([x , y+dy[2]])
            visited[x][y+dy[2]] = True
        if y+dy[3] <= n and graph[x][y+dy[3]] != 0 and visited[x][y+dy[3]] == False:
            q.append([x , y+dy[3]])
            visited[x][y+dy[3]] = True

    
    return house_cnt

for i in range(1,n+1):
    for j in range(1,n+1):
        answer = bfs(i,j)
        if answer != 0:
            result.append(answer - 1)

result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])



    



