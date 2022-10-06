# 백준 14499번 주사위 굴리기
# 유형: 구현
# 난이도: 골드4

# n : 세로크기
# m : 가로크기
# x, y : 주사위를 놓은 곳의 좌표
# k : 명령의 개수
n, m, x, y, k = map(int, input().split())

# 지도 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 명령 입력
order = list(map(int, input().split()))

# 방향(동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 표시
dice = [0, 0, 0, 0, 0, 0]

# 주사위를 명령코드에 맞게 굴렸을 때 바뀌는 주사위 표시를 정의하는 메서드
def turn(dir):
    # 1, 2, 3, 4, 5, 6
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    # 동쪽으로 이동할 때
    if dir == 1:
        # a->c, c->f, f->d, d->a
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]= c, b, f, a, e, d
    # 서쪽으로 이동할 때
    elif dir == 2:
        # a->d, d->f, f->c, c->a
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]= d, b, a, f, e, c
    # 북쪽으로 이동할 때
    elif dir == 3:
        # a->b, b->f, c, d, e->a, f->e
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]= b, f, c, d, a, e
    # 남쪽으로 이동할 때
    elif dir == 4:
        # a->e, b->a, c, d, e->f, f->b
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]= e, a, c, d, f, b

# 명령대로 주사위를 굴림
for num in order:
    # 방향대로 주사위를 굴려 지도의 바깥으로 이동하는지 확인
    nx, ny = x + dx[num-1], y + dy[num-1]
    # 지도의 범위에서 넘어가면 한 번 건너뜀
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx, ny = nx - dx[num-1], ny - dy[num-1]
        continue

    x, y = nx, ny

    # 벗어나지 않으면 계산 시작
    turn(num)

    # 이동한 칸의 점수가 0인 경우
    # 주사위 바닥면의 수가 칸에 복사
    if graph[x][y] == 0:
        graph[x][y] = dice[-1]
    # 이동한 칸의 점수가 0이 아닌 경우
    # 주사위 바닥면으로 복사, 바닥 칸은 0으로 됨
    else:
        dice[-1] = graph[x][y]
        graph[x][y] = 0
    # 주사위 위를 출력
    print(dice[0])
