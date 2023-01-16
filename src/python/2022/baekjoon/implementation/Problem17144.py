# 백준 27144번 미세먼지 안녕!
# 유형: 구현
# 난이도: 골드4

# (R, C) : 집 크기
# T : 시간
R, C, T = map(int, input().split())

# 공기청정기와 미세먼지가 있는 집 입력
board = [list(map(int, input().split())) for _ in range(R)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

up = -1
down = -1

# 공기청정기 위치를 구함
for i in range(R):
    if board[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지를 확산하는 메서드 정의
def spread():
    arr = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            # 미세먼지의 위치를 알아야 함(0이 아니거나 -1이 아닌 경우)
            if board[i][j] != 0 and board[i][j] != -1:
                temp = 0
                # 4 방향으로 퍼짐
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    # 인접한 방향에 공기청정기가 있거나 칸을 벗어나면 확신이 안됨
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        # 미세먼지가 확산되는 양 : A[R][C] / 5 (소수점 버림)
                        arr[nx][ny] += board[i][j] // 5
                        # (R, C)에 남은 미세먼지 양을 구함
                        temp += board[i][j] // 5

                board[i][j] -= temp

    # 미세먼지가 이동한 후의 집을 재조정
    for i in range(R):
        for j in range(C):
            board[i][j] += arr[i][j]

# 위쪽 공기 청정기 작동 정의 메서드
def clean_up():
    # 위쪽 공기청정기 순환 흐름(반시계방향)
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    dir = 0
    before = 0
    # 현재 바람의 위치
    x, y = up, 1

    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        # 공기청정기가 있는 위치에 도달하면 종료
        if x == up and y == 0:
            break

        # 공기청정기가 범위 밖으로 벗어나면 방향을 전환
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue

        # 이전 위치에 있던 미세먼지를 이동
        board[x][y], before = before, board[x][y]
        x, y = nx, ny

# 아래쪽 공기청정기 작동 정의 메서드
def clean_down():
    # 아래쪽 공기청정기 공기 순환 흐름 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dir = 0
    before = 0

    # 현지 공기 위치
    x, y = down, 1

    while True:
        nx, ny = x + dx[dir], y + dy[dir]
        # 공기청정기가 있는 곳에 위치하면 종료
        if x == down and y == 0:
            break

        # 공기가 범위 밖으로 이동하려고 하면 방향을 전환
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir += 1
            continue

        # 이전 위치에 있는 미세먼지를 이동
        board[x][y], before = before, board[x][y]
        x, y = nx, ny

# 입려된 T 시간동안 일어난 일
for _ in range(T):
    # 1.미세먼지의 확산
    spread()
    # 2.위쪽 공기청정기 작동
    clean_up()
    # 3.아래쪽 공기청정기 작동
    clean_down()

result = 0

# 남아있는 미세먼지의 양을 구함
for i in range(R):
    for j in range(C):
        # 공기청정기와 빈공간은 구하지 않음
        if board[i][j] > 0:
            result += board[i][j]

print(result)
