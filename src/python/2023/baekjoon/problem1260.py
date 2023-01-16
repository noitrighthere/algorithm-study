from collections import deque

def dfs(v):
    print(v, end = ' ')
    visited[v] = True

    for e in graph[v]:
        if not visited[e]:
            dfs(e)

def bfs(v):
    q = deque([v])

    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')
            for e in graph[v]:
                if not visited[e]:
                    q.append(e)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 간선의 양방향을 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for e in graph:
    e.sort()

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)