# 적록색약
from collections import deque

# 크기 입력
N = int(input())
# 그리드 입력
grid = [list(input()) for _ in range(N)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 넓이우선탐색
def bfs(x, y, color):
    # 현재 위치를 방문 처리
    visited[x][y] = True
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        # 상하좌우로 탐색 시작
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 이동한 위치가 그리드를 벗어나면 안됨 + 현재의 색과 같은 색이어야 함
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and grid[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# 적록인 사람이 아닐 때
cnt1 = 0
# 방문 플래그
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt1 += 1
            bfs(i, j, grid[i][j])

# 적록인 사람일 때
cnt2 = 0
visited = [[False] * N for _ in range(N)]

# G -> R로 바꿔줌
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

# 똑같이 bfs 탐색으로 영역의 개수를 구함
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt2 += 1
            bfs(i, j, grid[i][j])

print(cnt1, cnt2, end=' ')