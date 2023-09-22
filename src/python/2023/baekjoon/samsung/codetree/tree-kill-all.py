from copy import deepcopy

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
weedkiller = [[0]*n for _ in range(n)]

result = 0

# 나무의 성장에 관한 함수
def grow():
    # 주변에 있는 나무의 수
    temp = [[0] * n for _ in range(n)]

    # 인접한 나무가 있는 칸의 수를 구함
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] > 0:
                            temp[i][j] += 1

    for i in range(n):
        for j in range(n):
            graph[i][j] += temp[i][j]



# 나무의 번식에 관한 함수
def breeding():
    temp = deepcopy(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:

                tree_value = graph[i][j]
                cnt = 0

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]

                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 0 and weedkiller[nx][ny] == 0:
                            cnt += 1

                if cnt != 0:
                    tree_spread = tree_value // cnt

                    for k in range(4):
                        mx, my = i + dx[k], j + dy[k]

                        if 0 <= mx < n and 0 <= my < n:
                            if graph[mx][my] == 0 and weedkiller[mx][my] == 0:
                                if graph[mx][my] == 0 and weedkiller[mx][my] == 0:
                                    temp[mx][my] += tree_spread

    return temp

# 가장 많이 박멸될 만한 곳을 찾음
def count_kill_simulation(x, y):

    global k_x, k_y, max_kill
    kill_value = graph[x][y]

    for d in range(4):
        # k칸 만큼 전파
        cx, cy = x, y
        for _ in range(k):
            nx, ny = cx + _dx[d], cy + _dy[d]

            if not (0 <= nx < n and 0 <= ny < n):
                break
            if graph[nx][ny] <= 0:
                break
            if graph[nx][ny] > 0:
                kill_value += graph[nx][ny]
                cx, cy = nx, ny

    if kill_value > max_kill:
        k_x, k_y = x, y
        max_kill = kill_value

def cool_down():
    for i in range(n):
        for j in range(n):
            if weedkiller[i][j] > 0:
                weedkiller[i][j] -= 1

def tree_kill(x, y):
    # 현재 위치 = 제초제가 처음 살포되는 위치
    weedkiller[x][y] = c
    graph[x][y] = 0

    for d in range(4):
        cx, cy = x, y
        for _ in range(k):
            nx, ny = cx + _dx[d], cy + _dy[d]

            if not (0 <= nx < n and 0 <= ny < n):
                break
            # 벽일 때는 제초제를 안뿌려도 됨
            if graph[nx][ny] == -1:
                break
            # 빈칸일 때는 제초제를 뿌리고 더이상 뿌리지 않음
            if graph[nx][ny] == 0:
                weedkiller[nx][ny] = c
                break
            if graph[nx][ny] > 0:
                weedkiller[nx][ny] = c
                graph[nx][ny] = 0
                cx, cy = nx, ny

# m년 동안 진행
for _ in range(m):

    # 대각선 방향
    _dx = [-1, -1, 1, 1]
    _dy = [-1, 1, 1, -1]

    # 1. 나무의 성장
    grow()

    # 2. 나무의 번식
    graph = breeding()

    # 3. 제초제 살포
    k_x, k_y = 0, 0
    max_kill = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                count_kill_simulation(i, j)

    # 4. 제초제 경감기
    cool_down()

    # 5. 제초제 살포
    tree_kill(k_x, k_y)

    result += max_kill

print(result)