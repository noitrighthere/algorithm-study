# 미세먼지 안녕!

# R: 행, C: 열, T: 초
R, C, T = map(int, input().split())

# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(R)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 미세먼지가 확산하는 메서드
def spread():
    # 확산되는 양을 담는 배열
    temp = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # 미세먼지가 위치해 있는 곳을 찾아야 함
            if graph[i][j] != 0 and graph[i][j] != -1:
                # 확산되는 양
                spread_cnt = 0

                # 4 방향으로 확산(상하좌우)
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    # 확산되는 곳이 공기청정기가 있거나 칸을 벗어나면 안됨
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        # 미세먼지가 확산되는 양
                        temp[nx][ny] += graph[i][j] // 5
                        # 해당 위치에 남는 미세먼지 양을 구함
                        spread_cnt += graph[i][j] // 5

                graph[i][j] -= spread_cnt

    for i in range(R):
        for j in range(C):
            graph[i][j] += temp[i][j]

# 위쪽 공기 청정기 작동
def clean_up():
    # 위쪽 공기청정기 순환 반향
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    # 현재 방향 (스타트는 '->' 방향)
    dir = 0
    # 현재 바람의 위치
    x, y = up, 1

    before = 0

    # 바람이 불면 미세먼지가 바람의 방향대로 한 칸씩 이동
    while True:
        # 이동한 바람의 위치
        nx, ny = x + dx[dir], y + dy[dir]
        # 바람이 이동한 곳이 공기청정기가 있는 곳이면 종료
        if x == up and y == 0:
            break

        # 공기청정기가 범위 밖으로 벗어나면 방향을 반시계 방향으로 방향 전환
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue

        # 미세먼지를 바람의 방향대로 한칸씩 이동
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

def clean_down():
    # 위쪽 공기청정기 순환 반향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 현재 방향 (스타트는 '->' 방향)
    dir = 0
    # 현재 바람의 위치
    x, y = down, 1

    before = 0

    # 바람이 불면 미세먼지가 바람의 방향대로 한 칸씩 이동
    while True:
        # 이동한 바람의 위치
        nx, ny = x + dx[dir], y + dy[dir]
        # 바람이 이동한 곳이 공기청정기가 있는 곳이면 종료
        if x == down and y == 0:
            break

        # 공기청정기가 범위 밖으로 벗어나면 방향을 반시계 방향으로 방향 전환
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue

        # 미세먼지를 바람의 방향대로 한칸씩 이동
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

# 공기청정기 위치
up = 0
down = 0

# 공기청정기 위치를 구함
for i in range(R):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break

for _ in range(T):
    # 1. 미세먼지의 확산
    spread()
    # 2. 공기청정기 작동
    clean_up()
    clean_down()

result = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)