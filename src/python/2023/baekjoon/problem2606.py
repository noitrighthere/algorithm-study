# 바이러스

# 컴퓨터 수가 주어진다.
n = int(input())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍
m = int(input())
# 그래프
graph = [[] for _ in range(n+1)]
# 방문 플래그
visited = [False] * (n+1)
# 결과
result = 0

# 그래프 입력
for _ in range(m):
    x, y = map(int, input().split())
    # 양방향으로 입력
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    global result

    for i in graph[v]:
        if not visited[i]:
            result += 1
            dfs(graph, i, visited)

dfs(graph, 1, visited)

print(result)