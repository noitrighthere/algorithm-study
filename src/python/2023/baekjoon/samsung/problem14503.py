# 로봇청소기

# 방 크기 입력
n, m = map(int, input().split())

# 로봇 청소기 초기 위치, 방향 입력
r, c, d = map(int, input().split())

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 로봇이 청소하는 칸의 개수
cnt = 1
# 현재 위치 청소
graph[r][c] = 2

def change(d):
    if d == 0:
        return 3
    if d == 3:
        return 2
    if d == 2:
        return 1
    if d == 1:
        return 0

while(True):

    dc = d
    empty = 0

    # 4방향으로 탐색
    for _ in range(4):
        dc = change(dc)
        nx = r + dx[dc]
        ny = c + dy[dc]

        # 범위를 벗어나지 않고 빈칸인 경우
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            # 청소시작
            cnt += 1
            r = nx
            c = ny
            graph[nx][ny] = 2
            d = dc
            empty = 1
            break

    if empty == 0:
        if d == 0:
            r += 1
        elif d == 1:
            c -= 1
        elif d == 2:
            r -= 1
        elif d == 3:
            c += 1

        if graph[r][c] == 1:
            break

print(cnt)