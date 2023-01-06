# 백준 1926번 그림
# 유형: DFS/BFS
# 난이도: 실버1
import sys

# n: 세로, m: 가로
n, m = map(int, input().split())
# 그래프 생성
graph = [list(map(int, input().split())) for _ in range(n)]
# 방문한 위치
visited = [[False] * m for _ in range(n)]

# 위치
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 그림의 개수
cnt = 0
# 그림의 넒이
wide = 0

# bfs 메서드 정의
def bfs(x, y):
    # 방문한 노드로 표시
    visited[x][y] = True
    wide = 1
    queue = [(x, y)]

    while queue:
        x, y = queue.pop()
        # 상하좌우를 탐색하면서 그림의 유무를 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 영역을 벗어나지 않아야 함
            if 0 <= nx < n and 0 <= ny < m:
                # 방문하지 않고 그림이 있는 경우 재귀
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    wide += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return wide

# 방문했던 위치가 아니고 그림이 있을 경우 탐색 시작
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            wide = max(wide, bfs(i, j))
            cnt += 1

print(cnt)
print(wide)