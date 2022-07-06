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

# 방문한 노드 플래그
visited = [[0] * N for _ in range(N)]
cnt = []

def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    # 방문한 노드는 플래그를 1로 바꿈
    visited[a][b] == 1
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
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

for i in cnt:
    print(i)



