# 백준 7576번 토마토
# 유형: DFS/BFS
# 난이도: 골드5
from collections import deque

# bfs 메서드 정의
def bfs():
    # 날짜
    result = 0

    while queue:

        result += 1

        for _ in range(len(queue)):

            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                # 익지 않은 토마토를 찾아서 익게 만듬
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        queue.append([nx, ny])

    # 익지 않은 토마토가 남았을 경우
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1

    # 모두 익었을 경우
    return result - 1

# m: 가로, n: 세로
m, n = map(int, input().split())
# 그래프 생성
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()

for i in range(n):
    for j in range(m):
        # 토마토가 있는 위치이어야 함
        if graph[i][j] == 1:
            queue.append([i, j])

print(bfs())