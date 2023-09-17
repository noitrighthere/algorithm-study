# 마법사 상어와 파이어볼


# n: 크기, m: 파이어볼 수, k: 명령
n, m, k = map(int, input().split())

# 파이어볼 정보
fireballs = []

# 파이어볼 정보를 입력
for _ in range(m):
    # 위치, 질량, 방향, 속력
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

graph = [[[] for _ in range(n)] for _ in range(n)]

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# k번에 명령
for _ in range(k):
    # 파이어볼의 정보를 격자에 넣어줘야 함
    while fireballs:
        r, c, m, s, d = fireballs.pop(0)
        # 모든 파이어볼은 자신의 방향 d로 속력 s칸 만큼 이동
        nr = (r + s * dx[d]) % n
        nc = (c + s * dy[d]) % n
        graph[nr][nc].append([m, s, d])

    # 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는지 확인
    for i in range(n):
        for j in range(n):
            # 2개 이상인 경우
            if len(graph[i][j]) > 1:

                # sum_m: 합쳐진 질량, sum_s: 합쳐진 속력, cnt: 합쳐진 파이어볼 수
                sum_m, sum_s, cnt = 0, 0, len(graph[i][j])
                # 홀수의 개수 짝수의 개수 변수
                cnt_odd, cnt_even = 0, 0
                while graph[i][j]:
                    tm, ts, td = graph[i][j].pop(0)
                    sum_m += tm
                    sum_s += ts
                    # 홀수인 경우
                    if td % 2:
                        cnt_odd += 1
                    # 짝수인 경우
                    else:
                        cnt_even += 1

                # 모두 홀수이거나 모두 짝수인 경우
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                # 파이어볼을 4개로 나누고 질량이 0인 경우 소멸
                if sum_m // 5:
                    for d in nd:
                        fireballs.append([i, j, sum_m//5, sum_s//cnt, d])

            if len(graph[i][j]) == 1:
                fireballs.append([i, j] + graph[i][j].pop())

print(sum([f[2] for f in fireballs]))