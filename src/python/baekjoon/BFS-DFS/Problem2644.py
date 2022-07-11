# 백준 2644번 촌수계산
# 유형: DFS/BFS
# 난이도: 실버2

def dfs(a, b):
    global count

    visited[a] = True

    for e in graph[a]:
        if not visited[e]:
            count += 1
            if a == b:
                break;
            dfs(e, count)

n = int(input())    # 전체 사람의 수 입력
x, y = map(int, input().split())    # 촌수를 계산해야 하는 두 사람의 번호
m = int(input())    # 관계의 수 입력

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(graph)
visited = [False] * (n+1)
count = 0
dfs(x, y)
print(count)