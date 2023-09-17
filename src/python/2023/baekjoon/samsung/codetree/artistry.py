# 예술성

from collections import deque

# N 입력
n = int(input())
# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):

    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == graph[cx][cy]:
                    visited[nx][ny] = True
                    group[nx][ny] = group_num
                    group_cnt[group_num] += 1
                    q.append((nx, ny))

def score():

    # 예술 점수
    value = 0

    for i in range(n):
        for j in range(n):
            for k in range(4):
                mx = i + dx[k]
                my = j + dy[k]

                if 0 <= mx < n and 0 <= my < n:
                    if group[mx][my] != group[i][j]:
                        g_x, g_y = group[i][j], group[mx][my] # 번호가 다른 칸들의 좌표
                        g_x_num, g_y_num = graph[i][j], graph[mx][my] # 번호가 다른 칸들의 숫자
                        g_x_cnt, g_y_cnt = group_cnt[g_x], group_cnt[g_y] # 번호가 다른 칸들의 좌표를 활용한 그룹 번호 개수
                        value += (g_x_cnt + g_y_cnt) * g_x_num * g_y_num

    return value // 2 # 한 경우에 대해 2번 계산하게 되므로 2로 나누어 줌.

def plus_rotate():

    for i in range(n):
        for j in range(n):
            if i == n//2:
                arr_temp[i][j] = graph[j][i]
            if j == n//2:
                arr_temp[i][j] = graph[n-j-1][n-i-1]

def square_rotate(x, y, l):

    for i in range(x, x+l):
        for j in range(y, y+l):
            ox, oy = i - x, j - y
            rx, ry = oy, l - ox -1
            arr_temp[rx + x][ry + y] = graph[i][j]

result = 0
# 총 4번의 예술 점수를 구해야 함.
for _ in range(4):

        # 그룹을 분리하기 위해 만든 2차원 배열
    group = [[0] * n for _ in range(n)]
    # 그룹별로 개수를 세기 위한 배열
    group_cnt = [0] * (n * n + 1)
    # 그룹 번호
    group_num = 0
    # 방문 플래그
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_num += 1
                group[i][j] = group_num
                group_cnt[group_num] += 1
                bfs(i, j)

    # 예술 점수를 구함
    result += score()

    # 배열 회전을 위한 임시 배열
    arr_temp = [[0] * n for _ in range(n)]
    half = n // 2

    # 십자 모양을 반시계 방향으로 90도 회전
    plus_rotate()

    # 정사각형 모양 시계 방향으로 90도 회전
    square_rotate(0, 0, half)
    square_rotate(0, half+1, half)
    square_rotate(half+1, 0, half)
    square_rotate(half+1, half+1, half)

    for i in range(n):
        for j in range(n):
            graph[i][j] = arr_temp[i][j]

print(result)