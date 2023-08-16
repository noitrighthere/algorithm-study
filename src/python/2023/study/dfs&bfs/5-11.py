from collections import deque

# N: 세로, M: 가로
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동한 곳이 미로를 벗어나지 않아야 함
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

    return graph[N-1][M-1]

print(bfs(0, 0))