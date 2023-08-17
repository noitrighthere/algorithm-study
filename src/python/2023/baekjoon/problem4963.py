# 섬의 개수
import sys
from collections import deque

# 방향
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        # 상하좌우 + 대각선 방향을 탐색한다.
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            # 영역을 벗어나거나 그래프가 1인 경우 그리고 방문하지 않은 곳이어야 함
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))

while(1):
    # w: 넓이, h: 높이
    w, h = map(int, input().split())
    result = 0

    if w == 0 and w == h:
        sys.exit()

    # 그래프 입력
    graph = [list(map(int, input().split())) for _ in range(h)]
    # 방문 플래그
    visited = [[False] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                result += 1

    print(result)