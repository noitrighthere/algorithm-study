n, m = map(int, input().split())   # 얼음의 틀의 세로 길이(N)와 가로 길이(M) 입력
graph = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):

    if graph[x][y] == 0:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                graph[x][y] = 1
                dfs(nx, ny)

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)