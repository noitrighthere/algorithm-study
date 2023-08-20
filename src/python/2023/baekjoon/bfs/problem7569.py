# 토마토
from collections import deque

# M: 가로, N: 세로, H: 상자의 수
M, N, H = map(int, input().split())
# 그래프 생성
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 방문 플래그
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

# 방향(dz는 위-아래)
dx = [0, 0, -1, 0, 1, 0]
dy = [0, 0, 0, -1, 0, 1]
dz = [1, -1, 0, 0, 0, 0]

cnt = 0
q = deque()
# 넓이우선탐색
def bfs():

    while q:
        x, y, z = q.popleft()

        # 위아래상하좌우로 탐색 시작
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            # 이동할 위치가 영역 안에서만 있어야 함
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                # 익지 않은 토마토가 있는 곳 + 아직 방문하지 않은 곳이어야 함
                if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                    # 해당 위치를 일단 방문 처리함
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    # 해당 위치의 토마토가 익음
                    graph[nx][ny][nz] = 1
                    q.append((nx, ny, nz))

for i in range(H):
    for j in range(N):
        for k in range(M):
            # 탐색한 곳이 익은 토마토가 위치한 곳이고 아직 방문하지 않은 곳이라면 + 1
            if graph[i][j][k] == 1 and visited[i][j][k] == 0:
                q.append((i, j, k))
                visited[i][j][k] = 1

bfs()

# 0이 있으면 모두 익지 않은 상태이므로 -1을 호출하고 종료된다.
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            exit()

for i in visited:
    for j in i:
        cnt_max = max(j)
        cnt = max(cnt, cnt_max)

print(cnt-1)