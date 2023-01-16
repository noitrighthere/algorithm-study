from collections import deque

# 백준 2667번 단지번호 붙이기
# 유형: DFS/BFS
# 난이도: 실버1

N = int(input())    # 지도 크기 입력
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = []

def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    # 방문한 노드는 플래그를 1로 바꿈
    graph[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1

    return count

for i in range(N):
    for j in range(N):
        # 방문한 곳이 집이 있을 경우
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])



