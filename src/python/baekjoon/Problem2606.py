# 백준 2600번 바이러스
# 유형: DFS/BFS
# 난이도: 실버3

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    global count

    visited[node] = True

    for e in graph[node]:
        if not visited[e]:
            count += 1
            dfs(e)

visited = [False] * (n+1)
dfs(1)
print(count)