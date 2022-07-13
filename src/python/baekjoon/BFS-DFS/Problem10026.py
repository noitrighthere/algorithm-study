import sys
sys.setrecursionlimit(100000)

# 백준 10026번 적록색약
# 유형: DFS/BFS
# 난이도: 골드5

def dfs(x, y, color):

    # 1. 먼저 해당 위치를 방문한 노드로 만듬
    visited[x][y] = True

    # 2. 상하좌우로 탐색함
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 3. grid의 범위를 벗어나지 않아야 함
        if 0 <= nx < N and 0 <= ny < N:
            # 4. 이전에 방문하지 않은 노드이어야 한다.
            if not visited[nx][ny]:
                # 5. 같은 색이어야 한다.
                if grid[nx][ny] == color:
                    dfs(nx, ny, color)

N = int(input())    # 그리드의 크기 입력
grid = []

# 방향 표시
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    grid.append(list(input()))


# case 1. 정상인
cnt = 0     # 구역
visited = [[False] * N for _ in range(N)]   # 방문 노드 플래그

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, grid[i][j])
            cnt += 1

print(cnt)

# case 2. 적록생약
cnt = 0     # 구역
visited = [[False] * N for _ in range(N)]   # 방문 노드 플래그

# 적록색약인 경우 초록색 지역을 전부 빨간색 지역으로 바꿔줌
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, grid[i][j])
            cnt += 1

print(cnt)