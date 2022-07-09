# 백준 11724번 연결 요소의 개수
# 유형: DFS/BFS
# 난이도: 실버2

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 0

for _ in range(M):
    # 간선 입력
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = 1

    for e in graph[node]:
        if visited[e] == 0:
            dfs(e)

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)