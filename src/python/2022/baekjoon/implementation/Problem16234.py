# 백준 16234번 인구 이동
# 유형: 구현
# 난이도: 골드5
from collections import deque

# N : 땅 크기
# L, R : 두 나라의 인구 차이
N, L, R = map(int, input().split())

# 각 나라의 인구 입력
board = [list(map(int, input().split())) for _ in range(N)]

result = 0

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a, b):
    q = deque()
    # 국경이 열리는 국가의 수를 세기 위한 배열
    temp = []
    q.append((a, b))
    temp.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 땅 크기를 벗어나지 않고 방문하지 않은 나라이어야 함
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # 국경선을 공유하는 두 나라의 인구차이가 L 이상, R 이하
                if L <= abs(board[nx][ny]-board[x][y]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    temp.append((nx, ny))

    return temp


# 인구 이동이 없을 때까지 지속
while True:
    visited = [[0] * (N+1) for _ in range(N+1)]
    # 국경 open/close flag
    flag = 0
    # 1. 국경선을 공유하는 두 나라의 인구차이가 L명 이상, R명 이하면
    # => 국경선 open
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                # 2. 국경선을 연 국가들이 있으면 인구이동 시작
                if len(country) > 1:
                    flag = 1
                    # 4. 연합을 이루고 있는 각 칸의 인구 수 = (연합의 인구 수)/연합을 이루고 있는 칸의 개수
                    people = sum([board[x][y] for x, y in country]) // len(country)

                    # 인구가 이동
                    for x, y in country:
                        board[x][y] = people
    # 만약 조건을 만족하는 국가가 없으면 종료
    if flag == 0:
        break

    result += 1

print(result)