from collections import deque

N, M = map(int, input().split())
board = []

# 1: 이동할 수 있는 칸
# 0: 이동할 수 없는 칸
for _ in range(N):
    board.append(list(map(int, input())))

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[0] * M for _ in range(N)]

q = deque([(0, 0)])
visited[0][0] = 1

while q:
    x, y = q.popleft()

    # 미로 끝에 도달했을 때 값 호출
    if x == N-1 and y == M-1:
        print(visited[x][y])

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and board[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))