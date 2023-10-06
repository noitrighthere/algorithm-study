# 원자 충돌

# n: 격자의 크기
# m: 원자의 개수
# k: 실험 시간
n, m, k = map(int, input().split())

# 원자의 정보를 담을 배열
atoms = []

# 원자의 정보 입력
for _ in range(m):
    # x, y: 위치
    # m: 질량
    # s: 속력
    # d: 방향
    x, y, m, s, d = map(int, input().split())
    atoms.append([x-1, y-1, m, s, d])

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 원자를 담을 임시 배열
temp = [[[] for _ in range(n)] for _ in range(n)]

# 원자를 이동시키는 메소드
def move():
    while atoms:
        x, y, m, s, d = atoms.pop(0)
        # 모든 원자들은 자신의 방향으로 자신의 속력만큼 이동
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        # 임시배열에 이동한 원자의 정보를 넣음
        temp[nx][ny].append([m, s, d])

# 원자를 합성하는 메소드
def fusion():
    for i in range(n):
        for j in range(n):
            # 하나의 칸에 2개 이상의 원자가 있는 경우
            if len(temp[i][j]) > 1:
                sum_m, sum_s, cnt = 0, 0, len(temp[i][j])
                # 홀수, 짝수를 판단하기 위한 변수
                cnt_odd, cnt_even = 0, 0

                while temp[i][j]:
                    m, s, d = temp[i][j].pop(0)
                    # 원자의 질량과 속력을 모두 하나로 합침
                    sum_m += m
                    sum_s += s
                    # 홀수인 경우
                    if d % 2:
                        cnt_odd += 1
                    # 짝수인 경우
                    else:
                        cnt_even += 1

                # 방향이 모두 상하좌우거나 대각선인 경우
                if cnt_odd == cnt or cnt_even == cnt:
                    # 상하좌우 방향을 가짐
                    nd = [0, 2, 4, 6]
                # 그렇지 않은 경우
                else:
                    nd = [1, 3, 5, 7]
                # 원자를 5로 나누고 이후 질량이 0인 경우 소멸
                if sum_m // 5:
                    for d in nd:
                        # 해당 위치에 새로운 원자의 정보를 넣음
                        atoms.append([i, j, sum_m // 5, sum_s // cnt, d])

            # 원자가 1개인 경우엔 아무일도 일어나지 않음
            if len(temp[i][j]) == 1:
                atoms.append([i, j] + temp[i][j].pop())

# k번 만큼 로직을 수행
for _ in range(k):
    # step1. 원자 이동
    move()

    # step2. 원자 합성
    fusion()

print(sum([a[2] for a in atoms]))