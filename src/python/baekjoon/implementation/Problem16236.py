# 백준 16236 아기 상어
# 유형: 구현
# 난이도: 골드3
from collections import deque

# 공간의 크기 입력
n = int(input())
# 공간의 상태 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 상어의 현재 사이즈
shark_size = 2
# 현재 상어의 위치
x, y = 0, 0

# 엄마 상어한테 도움을 요청하지 않는 시간
cnt = 0
# 상어가 먹은 음식
food = 0

# 최단 거리를 위한 값
INF = 1e9

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 상어의 초기 위치를 알아냄
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j
            graph[x][y] = 0

# 현재 위치에서 각 물고기까지의 거리를 반환하고 지나는 경로마다 값을 저장하는 메서드 정의
def bfs():
    # 현재 위치를 queue에 저장
    queue = deque([(x, y)])

    # 방문 여부
    visited = [[-1] * n for _ in range(n)]
    # 현재 위치는 시작 위치이므로 0
    visited[x][y] = 0

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            nx, ny = current_x + dx[i], current_y + dy[i]
            # 범위 확인
            if 0 <= nx < n and 0 <= ny < n:
                # 상어가 이동 가능한지 확인
                if shark_size >= graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[current_x][current_y] + 1
                    queue.append((nx, ny))

    return visited

# 먹을 물고기 찾는 메서드 정의
def solve(visited):
    current_x, current_y = 0, 0

    # 최단거리
    min_distance = INF

    for i in range(n):
        for j in range(n):
            # bfs에서 지나지 않는 경로는 최단 경로가 아님 + 아기 상어가 먹을 수 있는지 확인
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    current_x, current_y = i, j

    if min_distance == INF:
        return False
    else:
        return current_x, current_y, min_distance


while True:
    result = solve(bfs())

    # result 값이
    if not result:
        print(cnt)
        break
    else:
        x, y = result[0], result[1]
        cnt += result[2]
        # 상어의 현재 위치를 초기화
        graph[x][y] = 0
        food += 1

    if food >= shark_size:
        shark_size += 1
        food = 0