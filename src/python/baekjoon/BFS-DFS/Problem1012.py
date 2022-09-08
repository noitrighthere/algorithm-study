# 백준 1012번 유기농 배추
# 유형: DFS/BFS
# 난이도: 실버2

import sys
sys.setrecursionlimit(10 ** 6)

# 테스트케이스 개수 입력
T = int(input())

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# dfs 메서드 정의
def dfs(x, y):
    # 현재 위치를 방문 처리
    visited[x][y] = True

    for i in range(4):
        # 상하좌우 방향으로 배추가 심어져 있는지 탐색함
        nx, ny = x + dx[i], y + dy[i]
        # 배추 밭을 벗어나지 않고 방문하지 위치인 경우에만 통과
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

for _ in range(T):
    # M: 가로길이, N: 세로길이, K: 배추가 심어져 있는 위
    M, N, K = map(int, input().split())
    # 그래프 생성
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 결과값
    result = 0

    # 배추가 심어져 있는 위치 입력
    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1     # 배추표시

    for i in range(N):
        for j in range(M):
            # 방문하지 않은 곳과 배추가 심어져 있는 곳인지 확인하고 탐색 시작
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                # 지렁이 추
                result += 1

    # 결과를 출력
    print(result)