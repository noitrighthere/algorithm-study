# 영역 구하기

# M: 세로, N: 가로, K: 직사각형수
M, N, K = map(int, input().split())
# 그래프 입력
graph = [[0] * N for _ in range(M)]
# 방문 플래그
visited = [[False] * N for _ in range(M)]

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 영역의 넓이
result = []
# 영역의 개수
area = 1

def bfs(x, y):
    visited[x][y] = True
    q = [(x, y)]
    cnt = 1

    while q:
        x, y = q.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 영역을 벗어나면 안됨.
            if 0 <= nx < M and 0 <= ny < N:
                # 그래프의 영역이 0이고 방문하지 않은 곳이어야 함
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return cnt

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            area += 1
            result.append(bfs(i, j))

result.sort()

print(area - 1, end = '\n')
print(*result, end = ' ')