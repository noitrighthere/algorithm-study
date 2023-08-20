# 연구소
from collections import deque
import itertools
import copy

# N: 세로, M: 가로
N, M = map(int, input().split())
# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(N)]

# 빈칸 영역
zero_area = []
# 바이러스 위치
virus = []
# 결과를 담을 리스트
results = []

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 넓이우선탐색
def bfs(x, y):
    # 해당 위치는 바이러스에 감염
    copy_graph[x][y] = 2
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        # 상하좌우로 바이러스가 이동할 구역을 탐색함
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 바이러스는 영역을 벗어나거나 이동핧 곳이 벽이 있으면 안됨.
            if 0 <= nx < N and 0 <= ny < M:
                if copy_graph[nx][ny] == 0:
                    # 이동할 구역은 바이러스에 감염됨
                    copy_graph[nx][ny] = 2
                    q.append((nx, ny))

# 3개의 벽을 세워둘 장소 리스트를 만들어야 함
for i in range(N):
    for j in range(M):
        # 빈칸인 경우
        if graph[i][j] == 0:
            zero_area.append([i, j])
        # 바이러스가 있는 경우
        if graph[i][j] == 2:
            virus.append([i, j])

# 벽이 세워질 곳 리스트
combi = itertools.combinations(zero_area, 3)

for com in combi:

    copy_graph = copy.deepcopy(graph)

    # 벽을 세움
    copy_graph[com[0][0]][com[0][1]] = 1
    copy_graph[com[1][0]][com[1][1]] = 1
    copy_graph[com[2][0]][com[2][1]] = 1

    # 바이러스가 퍼짐
    for vi in virus:
        bfs(vi[0], vi[1])

    cnt = 0
    # 바이러스가 퍼진 후 안전 영역의 크기를 구함
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 0:
                cnt += 1

    results.append(cnt)

print(max(results))