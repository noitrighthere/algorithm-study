n = int(input())    # 공간의 크기 입력
plans = input().split()
x, y, = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves_plan = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(moves_plan)):
        if plan == moves_plan[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)