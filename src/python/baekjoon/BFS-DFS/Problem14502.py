# 백준 14502번 연구소
# 유형: DFS/BFS
# 난이도: 골드4

import sys
import copy
from itertools import combinations
sys.setrecursionlimit(6**10)

# N: 세로, M: 가로 입력
N, M = map(int, input().split())
# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(N)]

virus = []
zero = []

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# dfs 메서드 정의
def dfs(x, y):
    # 바이러스에 걸림
    copy_graph[x][y] = 2

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if copy_graph[nx][ny] == 0:
                dfs(nx, ny)

for i in range(N):
    for j in range(M):
        # 바이러스가 있는 곳의 위치를 저장
        if graph[i][j] == 2:
            virus.append([i, j])
        # 아직 바이러스가 안 걸린 곳 저장
        elif graph[i][j] == 0:
            zero.append([i, j])

# 벽이 세워질 수 있는 조합
combi = combinations(zero, 3)

# 안전구역의 수를 저장할 배열
safety_zone = []

for com in combi:
    # 그래프에 깊은 복사함
    copy_graph = copy.deepcopy(graph)

    # 벽을 세움
    copy_graph[com[0][0]][com[0][1]] = 1
    copy_graph[com[1][0]][com[1][1]] = 1
    copy_graph[com[2][0]][com[2][1]] = 1

    # 바이러스가 퍼짐
    for vi in virus:
        dfs(vi[0], vi[1])

    safe_cnt = 0

    # 안전구역 카운트
    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 0:
                safe_cnt += 1

    safety_zone.append(safe_cnt)

print(max(safety_zone))