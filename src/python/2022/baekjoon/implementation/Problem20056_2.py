# 백준 20056번 마법사 상어와 파이어볼
# 유형: 구현
# 난이도: 골드4

# n : 격자 크기
# m : 파이어볼 개수
# k : 명령 개수
n, m, k = map(int, input().split())

# 파이어볼 정보
fireballs = []

# 파이어볼 정보를 입력
for _ in range(m):
    # (r_, c_) : 파이어볼 위치
    # m_ : 질량
    # s_ : 속력
    # d_ : 방향
    r_, c_, m_, s_, d_ = list(map(int, input().split()))
    # 파이어볼 정보를 담음
    fireballs.append([r_-1, c_-1, m_, s_, d_])

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

temp = [[[] for _ in range(n)] for _ in range(n)]

# k 번 명령 후 남아있는 파이어볼 질량의 합을 구함
for _ in range(k):
    # 1. 모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        # 파이어볼이 이동하게 되는 위치
        nr = (cr + cs * dx[cd]) % n
        nc = (cc + cs * dy[cd]) % n
        # 해당 위치에 파이어볼의 정보를 입력
        temp[nr][nc].append([cm, cs, cd])

    # 2. 이동이 끝난 후
    for i in range(n):
        for j in range(n):
            # 2개 이상의 파이어볼이 있는 칸이 있는지 확인
            if len(temp[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(temp[i][j])
                # 2-1. 같은 칸에 있는 파이어볼은 모두 하나로 합쳐짐
                # 2-2. 파이어볼은 4개의 파이어볼로 나누어짐
                while temp[i][j]:
                    m, s, d = temp[i][j].pop(0)
                    # 질량을 합침
                    sum_m += m
                    # 속력을 합침
                    sum_s += s
                    # 합쳐지는 파이어방향이 모두 홀수이거나 짝수인 경우
                    if d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                # 모두 홀수이거나 짝수인경우
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                # 질량이 0인 경우는 소멸
                if sum_m//5:
                    for dir in nd:
                        # 나누어진 파이어볼 정보를 저장
                        fireballs.append([i, j, sum_m//5, sum_s//cnt, dir])

            # 같은 칸에 파이어볼이 1개인 경우
            if len(temp[i][j]) == 1:
                # 이동한 위치만 담고 나머지 정보는 동일
                fireballs.append([i, j] + temp[i][j].pop())

# 남아있는 파이어볼 질량의 합을 구함
result = 0
for ball in fireballs:
    result += ball[2]

print(result)