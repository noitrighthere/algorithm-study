# 백준 19236번 청소년 상어
# 유형: 구현
# 난이도: 골드2
import copy

# 그래프 입력
graph = [[] for _ in range(4)]

# 물고기의 번호와 위치를 입력
for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([data[2*j], data[2*j+1]-1])
    graph[i] = fish

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기 번호의 합
max_score = 0

def dfs(shark_x, shark_y, score, graph):
    global max_score
    # (0, 0)에 있는 물고기를 먹고 상어의 방향은 (0,0)물고기의 방향과 같음
    score += graph[shark_x][shark_y][0]
    # 상어가 먹을 수 있는 물고기 번호 합의 최댓값을 구함
    max_score = max(max_score, score)
    # 상어가 물고기를 먹었으니 그 자리는 0임
    graph[shark_x][shark_y][0] = 0

    # 물고기 이동
    for f in range(1, 17):
        fish_x, fish_y = -1, -1
        for x in range(4):
            for y in range(4):
                if graph[x][y][0] == f:
                    fish_x, fish_y = x, y
                    break

        # 상어한테 이미 먹힌 물고기는 넘어감
        if fish_x == -1 and fish_y == -1:
            continue
        # 물고기 방향
        fish_dir = graph[fish_x][fish_y][1]

        for d in range(8):
            # 45도 반시계 방향
            nd = (fish_dir + d) % 8
            nx = fish_x + dx[nd]
            ny = fish_y + dy[nd]

            # 물고기가 이동할 수 없는 칸
            # 상어가 있는 곳 or 경계를 넘는 칸
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == shark_x and ny == shark_y):
                continue
            # 각 물고기는 이동할 수 있는 칸을 향한 방향으로 바꿔줘야 함
            graph[fish_x][fish_y][1] = nd

            # 물고기가 다른 칸으로 이동할 때는 서로의 위치를 바꿈
            graph[fish_x][fish_y], graph[nx][ny] = graph[nx][ny], graph[fish_x][fish_y]
            break

    # 물고기 이동이 끝나면 상어가 이동
    # 상어 위치
    shark_dir = graph[shark_x][shark_y][1]
    # 상어는 여러개의 칸을 이동할 수 있음
    for i in range(1, 5):
        nx = shark_x + dx[shark_dir] * i
        ny = shark_y + dy[shark_dir] * i
        # 물고기가 없는 칸으로는 이동하지 않음
        if (0 <= nx < 4 and 0 <= ny < 4) and graph[nx][ny][0] > 0:
            # 상어의 위치, 현재까지 먹은 물고기 합, 물고기가 이동한 그래프
            dfs(nx, ny, score, copy.deepcopy(graph))

dfs(0, 0, 0, graph)
print(max_score)