# 백준 3184번 양
# 유형: DFS/BFS
# 난이도: 실버1

# R: 행 C: 열 입력
r, c = map(int, input().split())
# 그래프 생성
graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# dfs 정의 메서드
def bfs(x, y):

    # 큐에 해당 위치 입력
    queue = [(x, y)]
    # 양과 늑대의 수
    sheep, wolf = 0, 0

    while queue:
        x, y = queue.pop()
        visited[x][y] = True

        # 그래프 안에 양이나 늑대가 있으면 수 추가
        if graph[x][y] == 'v':
            wolf += 1
        elif graph[x][y] == 'o':
            sheep += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


    # 늑대가 양의 수보다 같거나 많을 때: 양은 다 죽음
    if wolf >= sheep:
        sheep = 0
    else:
        wolf = 0

    return wolf, sheep

o_cnt, v_cnt = 0, 0

# '#'이지 않을 때 탐색을 시작
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'v' or graph[i][j] == 'o':
            if not visited[i][j]:
                v_temp, o_temp = bfs(i, j)
                o_cnt += o_temp
                v_cnt += v_temp

print(o_cnt, v_cnt)