# 백준 2583번 영역 구하기
# 유형: DFS/BFS
# 난이도: 실버1

# M: 세로, N: 가로, K: 직사각형 수
M, N, K = map(int, input().split())
# 그래프 생성
graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 영역의 넒이를 담을 배열
result = []
# 나눠지는 영역
area_cnt = 1

# bfs 정의 메소드
def bfs(x, y):
    visited[x][y] = True
    queue = [(x, y)]
    cnt = 1

    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return cnt

# 직사각형 수 만큼 영역을 표시해야 됨
for _ in range(K):
    # 왼쪽 아래 꼭짓점, 오른쪽 위 꼭지점 입력
    x1, y1, x2, y2 = map(int, input().split())

    # 영역을 표시
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        # 영역 표시가 안되어 있으면 탐색을 하고 넓이를 구해야 함
        if graph[i][j] == 0 and not visited[i][j]:
            area_cnt += 1
            result.append(bfs(i, j))

# 결과를 오름차순
result.sort()

print(area_cnt - 1, end = '\n')
print(*result, end = ' ')
