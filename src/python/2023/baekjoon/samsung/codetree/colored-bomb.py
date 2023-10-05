# 색깔 폭탄

from collections import deque

# n: 격자의 크기
# m: 폭탄의 종류
n, m = map(int, input().split())

# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

RED = 0
STONE = -1
EMPTY = -2

result = 0

def search_bombs(x, y, color, visited):

    temp = [[False]*n for _ in range(n)]
    temp[x][y] = True

    bundle = []
    count_of_red = 0

    # 큐 생성
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        bundle.append((x, y))

        # 현재 위치가 빨간색 폭탄이면 +1
        if graph[x][y] == 0:
            count_of_red += 1

        # 상하좌우로 탐색 하면서 폭탄 묶음을 찾음
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 격자를 벗어나면 안됨
            if 0 <= nx < n and 0 <= ny < n and not temp[nx][ny]:
                # 빨간색이 있거나 현재의 색과 같은 색인 경우
                if (graph[nx][ny] == RED or graph[nx][ny] == color) and graph[nx][ny] != STONE and graph[nx][ny] != EMPTY :
                    q.append((nx, ny))
                    temp[nx][ny] = True

    # 방문한 묶음들을 표시, 단 빨간색 폭탄은 제외
    for i in range(n):
        for j in range(n):
            if graph[i][j] != RED and temp[i][j]:
                visited[i][j] = temp[i][j]


    return (bundle, count_of_red)

# 기준점을 찾는 메소드
def get_point(pos):
    tx = -1
    ty = -1

    for x, y in pos:
        # 빨간색 폭탄인 경우 넘어감
        if graph[x][y] == RED:
            continue

        # 행이 가장 큰칸 -> 열이 가장 작은 칸
        if tx < x:
            tx = x
            ty = y

        if tx == x:
            if ty > y:
                ty = y

    return (tx, ty)

# 크기가 가장 큰 폭탄 묶음을 찾는 메소드
def get_target(bombs):
    max_bomb = 0
    min_red = 0
    target = []

    for count_of_red, bomb in bombs:
        # 폭탄의 개수가 가장 큰 것을 선택
        if len(bomb) > max_bomb:
            max_bomb = len(bomb)
            min_red = count_of_red
            target = bomb

        # 크기가 큰 폭탄 묶음이 여러개인 경우
        if len(bomb) == max_bomb:
            # 1. 빨간색 폭탄이 가장 적게 포함된 것 부터 선택
            if count_of_red < min_red:
                min_red = count_of_red
                target = bomb

            # 1번 조건이까지 동일한 폭탄 묶음이 여러개인 경우
            if count_of_red == min_red:
                x1, y1 = get_point(bomb)
                x2, y2 = get_point(target)

                # 기준점을 이용하여 선택
                if x1 > x2:
                    target = bomb

                if x1 == x2:
                    if y1 < y2:
                        target = bomb

    return target

# 폭탄을 제거하는 메서드
def delete_bomb(bomb):
    for x, y in bomb:
        graph[x][y] = EMPTY

# 중력이 작용하는 메서드
def gravity():

    for j in range(n):
        row_idx = n - 1

        for i in range(n-1, -1, -1):
            if graph[i][j] == STONE:
                row_idx = i - 1

            if graph[i][j] != STONE and graph[i][j] != EMPTY:
                while row_idx >= 0 and graph[row_idx][j] == STONE:
                    row_idx -= 1

                graph[row_idx][j] = graph[i][j]

                if i != row_idx:
                    graph[i][j] = EMPTY

                row_idx -= 1

# 반시계 방향으로 90도 회전하는 메서드
def rotate():
    # 임시 배열을 생성
    temp = [[EMPTY] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 반시계 방향으로 회전된 위치
            temp[n - 1 - j][i] = graph[i][j]

    return temp

while True:
    # 현재 격자에서 폭탄 묶음을 찾음

    bombs = []
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != STONE and graph[i][j] != RED and graph[i][j] != EMPTY and not visited[i][j]:
                # 방문 플래그
                bundle, count_of_red = search_bombs(i, j, graph[i][j], visited)

                if len(bundle) > 1:
                    bombs.append((count_of_red, bundle))

    # 크기가 가장 큰 폭탄 묶음을 찾음
    target_bomb = get_target(bombs)

    if len(target_bomb) <= 1:
        break

    result += (len(target_bomb) ** 2)

    # 폭탄제거(돌 제외)
    delete_bomb(target_bomb)

    # 중력 작용
    gravity()

    # 반시계 방향으로 90도 회전
    graph = rotate()

    gravity()

print(result)