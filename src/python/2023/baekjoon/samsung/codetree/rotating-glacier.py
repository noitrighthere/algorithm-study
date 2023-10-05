# 회전하는 빙하

from collections import deque

# n: 회전 가능 레벨
# q: 회전 횟수
n, q = map(int, input().split())

# 빙하 입력
graph = [list(map(int, input().split())) for _ in range(2**n)]

# 회전 레벨 입력
levels = map(int, input().split())

# 임시 배열 생성
temp = [[0] * (2 ** n) for _ in range(2 ** n)]

# 방문 플래그
visited = [[False] * (2 ** n) for _ in range(2 ** n)]

# 방향(우-하-상-좌)
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 빙하가 회전하는 메소드
def rotate(level):
    # 임시 배열 초기화
    for i in range(2 ** n):
        for j in range(2 ** n):
            temp[i][j] = 0

    # 격자 사이즈, 격자 사이즈 반의 크기
    box_size, half_size = (2 ** level), (2 ** (level - 1))

    # 조건에 맞게 회전을 진행
    for i in range(0, 2 ** n, box_size):
        for j in range(0, 2 ** n, box_size):
            move(i, j, half_size, 0)
            move(i, j + half_size, half_size, 1)
            move(i + half_size, j, half_size, 2)
            move(i + half_size, j + half_size, half_size, 3)

    # 임시 배열에 입력된 회전한 빙하의 번호를 대입
    for i in range(2 ** n):
        for j in range(2 ** n):
            graph[i][j] = temp[i][j]

# 빙하가 움직이는 메소드
def move(start_row, start_col, half_size, dir):
    # 조건에 맞게 회전시킴
    for x in range(start_row, start_row + half_size):
        for y in range(start_col, start_col + half_size):

            nx = x + dx[dir] * half_size
            ny = y + dy[dir] * half_size

            temp[nx][ny] = graph[x][y]

# 빙하가 녹는 메소드
def melt():

    # 임시배열 초기화
    for i in range(2 ** n):
        for j in range(2 ** n):
            temp[i][j] = 0

    # 인접한 칸에 얼음이 3개 이상 있은 경우 녹지 않음
    # 3개 미만으로 있으면 -1
    # 0 이하인 경우는 얼음이 없는 경우임
    for i in range(2 ** n):
        for j in range(2 ** n):
            cnt = 0

            # 상하좌우 인접한 칸에 얼음을 찾음
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]

                # 범위를 벗어나지 않아야 함
                if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                    # 다음 칸도 얼음이 있어야 함
                    if graph[nx][ny]:
                        cnt += 1

            # 얼음이 3개 이상이 아닌 경우 해당 위치는 -1
            if graph[i][j] and cnt < 3:
                temp[i][j] = graph[i][j] - 1
            else:
                temp[i][j] = graph[i][j]

    # 임시배열의 값을 그래프에 대입
    for i in range(2 ** n):
        for j in range(2 ** n):
            graph[i][j] = temp[i][j]

# 남아있는 빙항의 총 양을 구하는 메소드
def get_remain_glaciers():
    result = 0

    for i in range(2 ** n):
        for j in range(2 ** n):
            result += graph[i][j]

    return result

# 가장 큰 크기를 가지는 얼음군집의 크기를 구하는 메소드
def max_glacier_group():
    max_size = 0

    for i in range(2 ** n):
        for j in range(2 ** n):
            if graph[i][j] and not visited[i][j]:
                max_size = max(max_size, bfs(i, j))

    return max_size

# 군집을 찾는 bfs 메소드
def bfs(x, y):

    cnt = 0

    visited[x][y] = True

    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        cnt += 1

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                if graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return cnt

for level in levels:
    # 0레벨이면 어차피 회전이 안됨
    if level:
        rotate(level)
    melt()

# 남아있는 빙하의 총양
print(get_remain_glaciers())
print(max_glacier_group())