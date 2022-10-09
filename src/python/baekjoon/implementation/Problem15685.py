# 백준 15685번 드래곤 커브
# 유형: 구현
# 난이도: 골드4

# n : 드래곤 커브의 개수
n = int(input())

# 방향
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 드래곤 커브
board = [[0] * 101 for _ in range(101)]

for _ in range(n):
    # (x, y) : 드래곤 커브의 시작점
    # d : 시작 방향
    # g : 세대
    x, y, d, g = map(int, input().split())
    board[x][y] = 1

    # 세대를 저장할 배열
    move = [d]

    # 세대 만큼 반복
    for _ in range(g):
        temp = []
        # 이전 세대의 정보를 뒤집어서 +1 (규칙)
        for i in range(len(move)):
            temp.append((move[-i-1] + 1) % 4)
        # 세대를 저장할 배열에 추가함
        move.extend(temp)

    # 드래곤 커브에 해당하는 좌표에 추가
    for i in move:
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 101 and 0 <= ny < 101:
            board[nx][ny] = 1
            # 드래곤 커브의 끝점을 갱신
            x, y = nx, ny

# 모든 꼭짓점이 드래곤 커브의 일부인 정사각형 개수 구함
result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

print(result)
