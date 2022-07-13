from collections import deque

# 백준 1260번 DFS와 BFS
# 유형: DFS/BFS
# 난이도: 실버2

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

def DFS(v):
    print(v, end = ' ')
    visited[v] = True

    for e in graph[v]:
        if not visited[e]:
            DFS(e)

def BFS(v):
    q = deque([v])

    while q:
        v = q.popleft()
        if not visited[v]:
            visited[v] = True
            print(v, end = ' ')
            for e in graph[v]:
                if not visited[e]:
                    q.append(e)

visited = [False] * (N+1)
DFS(V)
print()
visited = [False] * (N+1)
BFS(V)