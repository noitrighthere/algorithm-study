# 백준 23288번 주사위 굴리기
# 유형: 구현
# 난이도: 골드3

# n : 세로 크기
# m : 가로 크기
# k : 이동하는 횟수
from collections import deque

n, m, k = map(int, input().split())

# 주사위 표시
dice = [2, 4, 1, 4, 5, 6]

# 지도 입력
board = [list(map(int, input().split())) for _ in range(n)]

# 방향(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# (x, y) : 주사위의 처음 위치
# dir : 처음 이동할 방향(동쪽)
x, y, dir = 0, 0, 0

result = 0

# 주사위가 이동 정의하는 메서드
def move(x, y, d):
    nx, ny = x + dx[d], y + dy[d]

    # 이동 방향에 칸이 없는 경우
    if not (0 <= nx < n and 0 <= ny < m):
        # 반대 방향으로 이동
        nd = (d + 2) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        return nx, ny, nd

    return nx, ny, d

# 주사위가 굴러간 후 정의하는 메서드
def change_dice(dice, dir):
    # 1, 2, 3, 4, 5, 6 = a, b, c, d, e, f
    if dir == 0:
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
        # 남쪽 이동 (전면, 상단, 후면, 바닥)
    elif dir == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
        # 서쪽 이동 (왼쪽, 상단, 오른쪽, 바닥)
    elif dir == 2:
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
        # 북쪽 이동 (전면, 상단, 후면, 바닥)
    elif dir == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]

    return dice

# 연속해서 이동할 수 있는 칸의 개수를 찾는 메서드
def bfs(a, b):

    visited = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append([a, b])

    cnt = 1

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        # 동서남북 방향으로 갈 수 있는지 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위를 벗어나면 안 되고 이전 칸의 정수랑 같은지, 방문했던 곳인지를 확인
            if 0 <= nx < n and 0 <= ny < m and board[x][y] == board[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                # 칸의 개수를 1 추가
                cnt += 1
                queue.append([nx, ny])

    return cnt

# 이동하는 회수에 따라서 계산
for _ in range(k):
    # 주사위 이동
    x, y, dir = move(x, y, dir)
    # 주사위가 굴러갔기 때문에 해당방향으로 주사위 윗면 등을 바꿈
    dice = change_dice(dice, dir)
    # 주사위가 이동한 칸 (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수

    count = bfs(x, y)
    # 점수를 계산
    result += board[x][y] * count

    # 다음 주사위의 이동 방향 결정
    # a : 주사위 아랫면 정수
    # b : 칸 (x, y)에 있는 정수
    a, b = dice[5], board[x][y]

    # A > B인 경우 이동방향을 90도 시계방향 회전
    if a > b:
        dir = (dir + 1) % 4
    # A < B인 경우 이동방향을 90도 반시계방향 회전
    elif a < b:
        dir = (dir + 3) % 4

print(result)