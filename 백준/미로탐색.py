from collections import deque


n , m = map(int, input().split())

graph = []

for i 기in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for i in range(n)]

dx = [ -1, 1 , 0 , 0]
dy = [ 0 , 0 , -1 , 1]



def bfs(graph , visited):

    q = deque()

    q.append([0,0])

    while q:
        x,y = q.popleft()
        
        visited[x][y] = True

        if x + dx[0]  >= 0  and graph[x+dx[0]][y] != 0:
            if visited[x+dx[0]][y] == False:
                q.append([x + dx[0] , y ])
                graph[x+dx[0]][y] = graph[x][y] + 1
                visited[x+dx[0]][y] = True
        if x + dx[1]  < n and graph[x+dx[1]][y] != 0:
            if visited[x+dx[1]][y] == False:
                q.append( [x + dx[1] , y])
                graph[x+dx[1]][y] = graph[x][y] + 1
                visited[x+dx[1]][y] = True
        if y + dy[2] >= 0 and graph[x][y+dy[2]] != 0:
            if visited[x][y+dy[2]] == False:
                q.append([x,y+dy[2]])
                graph[x][y+dy[2]] = graph[x][y] + 1
                visited[x][y+dy[2]] = True
        if y + dy[3] < m and graph[x][y+dy[3]]:
            if visited[x][y+dy[3]] == False:
                q.append([x , y+dy[3]])
                graph[x][y+dy[3]] = graph[x][y] + 1
                visited[x][y+dy[3]] = True


bfs(graph, visited)

print(graph[n-1][m-1])




    





