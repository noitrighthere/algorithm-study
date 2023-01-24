# 방향 전환 메서드 정의
def change(d):
    # d가 0인 경우 -> 북
    if d == 0:
        # 북에서 왼쪽 = 서
        return 3
    # d가 1인 경우 -> 동
    if d == 1:
        # 동에서 왼쪽 = 북
        return 0
    # d가 2인 경우 -> 남
    if d == 2:
        # 남에서 왼쪽 = 동
        return 1
    # d가 3인 경우 0 -> 서
    if d == 3:
        # 서에서 왼쪽 = 남
        return 2

# 로직 정의
def solution(r, c, d):
    # 로봇 청소기가 청소하는 칸의 개수 정의
    cnt = 1
    # 가로, 세로를 보기 쉽게 x, y로 치환
    x = r
    y = c
    # 1. 현재 위치를 청소
    board[x][y] = 2

    while(1):
        empty = 0
        dc = d

        # 네 방향으로 탐색
        for i in range(4):
            # 현재 방향에서 왼쪽 방향으로 탐색
            dc = change(dc)
            nx = x + dx[dc]
            ny = y + dy[dc]

            # 범위를 벗어나지 않고 청소가 필요한 부분 탐색
            if 0 < nx <= N and 0 < ny <= M and board[nx][ny] == 0:
                # 청소하는 칸의 개수 + 1
                cnt += 1
                # 현재위치 최신화
                x = nx
                y = ny
                board[nx][ny] = 2
                d = dc
                empty = 1
                break

        # 네 방향 모두 청소가 되어 있을 때
        # 뒤쪽 방향이 벽인지 확인
        if empty == 0:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1

            # 벽인 경우에 stop
            if board[x][y] == 1:
                break

    return cnt

# N, M 입력
N, M = map(int, input().split())
# r, c, d 입력
r, c, d = map(int, input().split())
# 영역 입력
board = [list(map(int, input().split())) for _ in range(N)]

# 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(solution(r, c, d))