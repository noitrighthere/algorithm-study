import sys
import copy
from itertools import combinations
sys.setrecursionlimit(6**10)

# 지도의 세로 크기(n), 가로 크기(m) 입력
n, m = map(int, input().split())
# 지도 모양 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 바이러스가 있는 위치
virus = []
# 바이러스가 안 걸린 곳 위치
zero = []

# bfs 메서드 정의
def dfs(x, y):
    # 해당 위치 바이러스에 전염
    copy_graph[x][y] = 2

    # 상하좌우로 검색해서 벽에 안막혀 있으면 바이러스에 전염
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if copy_graph[nx][ny] == 0:
                dfs(nx, ny)

for i in range(n):
    for j in range(m):
        # 바이러스가 있는 곳의 위치를 저장
        if graph[i][j] == 2:
            virus.append([i, j])
        # 바이러스가 안 걸린 곳 저장
        elif graph[i][j] == 0:
            zero.append([i, j])

# 벽이 세워질 수 있는 곳의 조합
combi = combinations(zero, 3)

# 안전구역의 수를 저장할 배열
safety_zero = []

for com in combi:
    # 그래프에 복사
    copy_graph = copy.deepcopy(graph)

    # 벽을 세움
    copy_graph[com[0][0]][com[0][1]] = 1
    copy_graph[com[1][0]][com[1][1]] = 1
    copy_graph[com[2][0]][com[2][1]] = 1

    # 바이러스가 퍼짐
    for vi in virus:
        # 바이러스 위치의 가로, 세로 입력
        dfs(vi[0], vi[1])

    cnt = 0

    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:
                cnt += 1

    safety_zero.append(cnt)

print(max(safety_zero))