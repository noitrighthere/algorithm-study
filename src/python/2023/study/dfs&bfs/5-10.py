# N: 세로, M: 가로
N, M = map(int, input().split())

graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):

    if graph[x][y] == 0:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                graph[x][y] = 1
                dfs(nx, ny)

result = 0
for i in range(N):
    for j in range(M):
        # 얼음의 구멍이 뚫려있으면 아이스크림을 만들어야 함
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)