# 백준 21610번 마법사 상어와 비바라기
# 유형: 구현
# 난이도: 골드5

# N : 격자의 크기
# M : 명령어 수
n, m = map(int, input().split())

# 격자 입력
board = [list(map(int, input().split())) for _ in range(n)]

# 구름이 이동할 방향과 거리를 담을 리스트
moves = []

# 구름이 처음 위치한 곳
clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

for _ in range(m):
    # d : 방향
    # s : 거리
    d, s = map(int, input().split())
    # 방향과 거리를 넣어줌
    moves.append([d-1, s])

# 방향
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 명령어 개수대로 구름을 이동
for i in range(m):
    # 1. 모든 구름이 d 방향으로 s 칸 만큼 이동
    move = moves[i]
    # 구름이 옮겨질 위치를 담을 임시 배열
    cloud_next = []

    # 구름을 이동
    for cloud in clouds:
        x = cloud[0]
        y = cloud[1]
        d_ = move[0]
        s_ = move[1]
        nx = (n + x + dx[d_] * s_) % n
        ny = (n + y + dy[d_] * s_) % n
        # 이동된 구름의 위치를 저장
        cloud_next.append([nx, ny])

    # 2. 비가 내려 구름이 있는 칸의 바구니 물의 양이 1증가
    visited = [[False] * n for _ in range(n)]
    for cloud in cloud_next:
        x, y = cloud[0], cloud[1]
        # 물의 양 1증가
        board[x][y] += 1
        # 구름이 있었던 칸을 표시
        visited[x][y] = True

    # 3. 구름이 사라짐
    clouds = []

    # 4. 물이 증가한 칸에 마법시전
    # 대각선 방향으로 거리가 1인 바구니의 수 만큼 (r, c)에 있는 물의 양이 증가
    # 대각선 방향
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]

    for cloud in cloud_next:
        x, y = cloud[0], cloud[1]
        # 바구니의 수를 담을 변수
        count = 0

        for i in range(4):
            nx, ny = x + cx[i], y + cy[i]
            # 경계를 넘어가면 안되고 물이 있어야 함
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] >= 1:
                count += 1

        # 물이 있는 바구니 수만큼 바구니 물의 양이 증가
        board[x][y] += count

    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생김.
    # 물의 양은 2 줄어듦. 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 함
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and not visited[i][j]:
                board[i][j] -= 2
                clouds.append([i, j])


result = 0
# 바구니에 있는 물의 양의 합을 구함
for i in range(n):
    for j in range(n):
        result += board[i][j]

print(result)