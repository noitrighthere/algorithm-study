# 토스트 계란틀

from collections import deque

# n: 총 칸의 크기
# L: 범위 최솟값, R: 범위 최댓값
n, L, R = map(int, input().split())

# 그래프
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 계란이 총 이동한 횟수
result = 0

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    # 조건에 해당하는 계란의 위치를 담을 배열
    temp = []
    temp.append([x, y])

    # 계란의 총합
    total_sum = 0
    total_sum += graph[x][y]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # L 이상 R 이하 여야 함
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    visited[nx][ny] = True
                    temp.append([nx, ny])
                    total_sum += graph[nx][ny]
                    q.append((nx, ny))

    # 계란이 이동하면서 합쳐짐
    for tmp in temp:
        graph[tmp[0]][tmp[1]] = total_sum // len(temp)

    if len(temp) > 1:
        return True
    return False

while True:
    # 루프를 끝낼 플래그
    cnt = 0
    # 방문 플래그
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1

    if cnt == n*n:
        print(result)
        break

    result += 1