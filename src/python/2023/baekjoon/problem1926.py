# 그림
from collections import deque

# n: 세로, m: 가로
n, m = map(int, input().split())
# 그래프 입력
graph =[list(map(int, input().split())) for _ in range(n)]
# 방문 플래그
visited = [[False] * m for _ in range(n)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

pic_cnt = 0
pic_area = 0

def bfs(x, y):
    # 현재 위치 방문 플래그에 True로 변경
    visited[x][y] = True
    area = 1
    q = deque([(x, y)])

    while q:
        # 큐에서 맨 앞에 있는 것을 꺼냄
        x, y = q.popleft()

        # 상하좌우로 갈 수 있는 방향을 탐색
        for i in range(4):
            nx, ny = x + dx[i], y +dy[i]
            # 영역을 벗어나거나 이미 방문한 곳이면 안됨
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    area += 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return area

for i in range(n):
    for j in range(m):
        # 그래프가 1(그림)인 경우와 아직 방문하지 않은 곳을 탐색한다.
        if graph[i][j] == 1 and not visited[i][j]:
            pic_area = max(pic_area, bfs(i, j))
            pic_cnt += 1

print(pic_cnt)
print(pic_area)