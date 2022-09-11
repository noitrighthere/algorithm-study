from collections import deque

# N: 도시의 개수
# M: 도로의 개수
# K: 최단거리 정보
# X: 출발도시의 번
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

distance = [-1] * (N+1)
distance[X] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([X])

while q:
    current = q.popleft()

    for e in graph[current]:
        # 아직 방문하지 않은 도시라면
        if distance[e] == -1:
            distance[e] = distance[current] + 1
            q.append(e)

check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)