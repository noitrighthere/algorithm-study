# 섬의 개수
from collections import deque

# 방향
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = True

while True:
    # w: 너비, h: 높이
    w, h = map(int, input().split())

    # 섬의 개수
    result = 0

    if w == 0 and h == 0:
        exit(0)

    # 그래프 입력
    graph = [list(map(int, input().split())) for _ in range(h)]
    # 방문 플래그
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                result +=1

    print(result)