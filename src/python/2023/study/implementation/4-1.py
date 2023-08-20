# 에제 4-1 상하좌우

# 공간의 크기 N 입력
N = int(input())
plans = input().split()

# x,y의 시작 좌표
x, y = 1, 1

# 방향(LRUD)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
mode = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(4):
        if plan == mode[i]:
            nx, ny = x + dx[i], y + dy[i]

    if 1 <= nx < N and 1 <= ny < N:
        x, y = nx, ny

print(x, y)