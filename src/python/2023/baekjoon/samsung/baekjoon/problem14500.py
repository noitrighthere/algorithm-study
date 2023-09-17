# 테트로미노

# N: 세로, M: 가로
N, M = map(int, input().split())

# 그래프 생성
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 결과값
result = 0

def dfs(x, y, score, cnt):
    global result

    # 테트로노미노가 칸에 놓여질 경우 더 큰값을 계산
    if cnt == 4:
        result = max(result, score)
        return

        # 테트로미노를 만듬
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 테트로미노를 만들 때 경계를 벗어나지 않아야 함
        # 그리고 겹치지 않아야 함
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, score + graph[nx][ny], cnt + 1)
            visited[nx][ny] = False

def other(x, y):
    global result

    for i in range(4):
        # 가운데 위치
        temp = graph[x][y]

        # ㅗ, ㅏ, ㅜ, ㅓ 방향의 테트로미노를 구함
        for d in range(3):
            t = (i+d)%4
            nx, ny = x + dx[t], y + dy[t]

            if 0 <= nx < N and 0 <= ny < M:
                temp += graph[nx][ny]

        result = max(result, temp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False

        other(i, j)

print(result)