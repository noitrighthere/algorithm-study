from collections import deque

# 백준 2178번 미로탐색
# 유형: DFS/BFS
# 난이도: 실버1

N, M = map(int, input().split())    # N, M 두 정수 입력
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0 , 1]

# 방문 플래그
visited = [[0] * M for _ in range(N)]

# 방문해야 하는 위치
q = deque([(0, 0)])
# 첫 번째 위치가 주어져 있으므로 1로 변경
visited[0][0] = 1

while q:
    x, y = q.popleft()

    # 미로의 끝에 도달 했을 때 해당 미로의 값을 호출
    if x == N-1 and y == M-1:
        print(visited[x][y])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))