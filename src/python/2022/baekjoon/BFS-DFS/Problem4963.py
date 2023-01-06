import sys
from collections import deque

# 백준 4963번
# 유형: DFS/BFS
# 난이도: 실버2

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, -1, 0, 1, 1, -1, 1, -1]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx, ny])

while True:

    # w: 너비, h: 높이
    w, h = map(int, input().split())
    answer = 0

    if w == 0 and h == 0:
        sys.exit(0)

    graph = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1

    print(answer)