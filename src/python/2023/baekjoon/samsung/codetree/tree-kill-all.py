from collections import deque

# n: 격자의 크기
# m: 박멸이 진행되는 년 수
# k: 제초제의 확산 범위
# c: 제초제가 남아있는 년 수
n, m, k, c = map(int, input().split())

# 방향(상하좌우)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 그래프
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0

# 나무의 성장에 관한 함수
def grow(x, y):
    # 주변에 있는 나무의 수
    count = 0

    # 인접한 나무가 있는 칸의 수를 구함
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > 0:
                count += 1

    # 인접한 칸의 수 만큼 더함
    graph[x][y] += count

# 나무의 번식에 관한 함수
def breeding(x, y, tree_value):
    # 번식할 수 있는 칸의 수
    count = 0
    breeding_value = 0

    # 번식할 수 있는 칸의 수를 구함
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        # 그래프 범위를 벗어나면 안됨
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                count += 1

    if count > 0:
        # 번식이 되는 나무의 수
        breeding_value = tree_value // count

    # 번식
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                temp[nx][ny] += breeding_value

# 가장 많이 박멸될 만한 곳을 찾음
def count_kill_simulation(x, y, value):

    global k_x, k_y, max_kill
    kill_value = value

    for d in range(4):
        # k칸 만큼 전파
        for i in range(1, k+1):
            nx, ny = x + _dx[d]*i , y + _dy[d]*i

            if 0 <= nx < n and  0 <= ny < n:
                # 나무가 있는 경우
                if graph[nx][ny] > 0:
                    kill_value += graph[nx][ny]
                # 벽을 있거나 나무가 없는 경우
                else:
                    break

    kill_count_graph[x][y] = kill_value

    if max_kill < kill_value:
        k_x, k_y = x, y
        max_kill = kill_value

def cool_down():
    for i in range(n):
        for j in range(n):
            # 제초제가 뿌려진 곳은 -2 이하임
            if graph[i][j] < -1:
                graph[i][j] += 1
            elif graph[i][j] == -2:
                graph[i][j] = 0

def tree_kill(x, y):
    # 현재 위치 = 제초제가 처음 살포되는 위치
    graph[x][y] = (-1 * c) - 1

    for d in range(4):
        # k 칸만큼 살포
        for i in range(1, k+1):
            nx, ny = x + _dx[d]*i , y + _dy[d]*i

            if 0 <= nx < n and 0 <= ny < n:
                # 빈칸일 때는 제초제를 뿌리고 더이상 뿌리지 않음
                if graph[nx][ny] == 0:
                    graph[nx][ny] = (-1 * c) - 1
                    break
                # 나무가 있는 경우
                elif graph[nx][ny] > 0:
                    graph[nx][ny] = (-1 * c) - 1

# m년 동안 진행
for _ in range(m):

    # 대각선 방향
    _dx = [-1, -1, 1, 1]
    _dy = [-1, 1, 1, -1]

    # 1. 나무의 성장
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                grow(i, j)

    # 2. 나무의 번식
    # 방문 플래그
    visited = [[False] * n for _ in range(n)]
    # 임시 그래프
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                breeding(i, j, graph[i][j])

    # 번식이 끝나고 완전한 상태(기존 그래프와 임시 그래프를 합침)
    for i in range(n):
        for j in range(n):
            graph[i][j] += temp[i][j]

    # 3. 제초제 살포
    # 임시 그래프
    kill_count_graph = [[0] * n for _ in range(n)]
    k_x, k_y = 0, 0
    max_kill = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                count_kill_simulation(i, j, graph[i][j])

    # 4. 제초제 경감기
    cool_down()

    # 5. 제초제 살포
    tree_kill(k_x, k_y)

    result += max_kill

print(result)