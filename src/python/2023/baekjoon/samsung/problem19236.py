# 청소년 상어
import copy

# 그래프 입력
graph = [[] for _ in range(4)]

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

result = 0

# 물고기 번호와 방향 입력
for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 짝수 번호는 번호를 나타내고 홀수는 방향을 나타냄
        fish.append([data[2 * j], data[2 * j + 1] - 1])
    graph[i] = fish


def dfs(shark_x, shark_y, score, graph):
    global result
    # 상어가 먹은 물고기의 번호의 합을 더함
    score += graph[shark_x][shark_y][0]
    # 상어가 먹을 수 있는 물고기 번호 합의 최댓값을 구함
    result = max(result, score)
    # 상어가 먹은 자리는 0
    graph[shark_x][shark_y][0] = 0

    # 1. 물고기 이동
    for f in range(1, 17):
        fish_x, fish_y = -1, -1
        for x in range(4):
            for y in range(4):
                # 번호가 작은 물고기 부터 이동
                if graph[x][y][0] == f:
                    fish_x, fish_y = x, y
                    break

        # 이미 상어한테 먹힌 물고기는 넘어감
        if fish_x == -1 and fish_y == -1:
            continue
        fish_dir = graph[fish_x][fish_y][1]

        for d in range(8):
            # 45도로 회전
            nd = (fish_dir + d) % 8
            nx, ny = fish_x + dx[nd], fish_y + dy[nd]

            # 물고기가 이동할 수 있는 곳인지 확인
            if not (0 <= nx < 4 and 0 <= ny < 4) or (shark_x == nx or shark_y == ny):
                continue
            # 이동할 수 있는 칸을 향할 때까지 반시계 45도로 회전
            graph[fish_x][fish_y][1] = nd

            # 물고기가 다른 칸으로 이동할 때는 서로의 위치를 바꿔줌
            graph[fish_x][fish_y], graph[nx][ny] = graph[nx][ny], graph[fish_x][fish_y]
            break

    # 2. 상어이동
    shark_dir = graph[shark_x][shark_y][1]

    # 갈 수 있는 모든 경우를 구함
    for i in range(1, 5):
        nx = shark_x + dx[shark_dir] * i
        ny = shark_y + dy[shark_dir] * i

        # 물고기가 없는 칸으로는 이동하지 않음
        if graph[nx][ny][0] > 0 and (0 <= nx < 4 and 0 <= ny < 4):
            dfs(nx, ny, score, copy.deepcopy(graph))

dfs(0, 0, 0, graph)
print(result)
