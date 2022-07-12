from collections import deque

# 백준 2644번 촌수계산
# 유형: DFS/BFS
# 난이도: 실버2

# a: start, b: end
def bfs(a, b):
    count = 0
    q = deque()
    q.append((a, count))

    while q:
        a, count = q.popleft()

        # 목적지에 도착했을 때 count를 리턴
        if a == b:
            return count

        if not visited[a]:
            count += 1
            visited[a] = True
            for e in graph[a]:
                if not visited[e]:
                    q.append((e, count))

    return -1

n = int(input())    # 전체 사람의 수 입력
a, b = map(int, input().split())    # 촌수를 계산해야 하는 두 사람의 번호
m = int(input())    # 관계의 수 입력

graph = [[] for _ in range(n+1)]

# 관계 입력
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
print(bfs(a, b))