# 백준 16236 아기 상어
# 유형: 구현
# 난이도: 골드3
from collections import deque

# 공간의 크기 입력
n = int(input())
# 공간의 상태 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 상어의 현재 사이즈
shark_size = 2
# 현재 상어의 위치
x, y = 0, 0

# 엄마 상어한테 도움을 요청하지 않는 시간
cnt = 0

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 상어의 위치를 알아냄
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j
            graph[x][y] = 0

def bfs():
    dist = [[-1]*n for _ in range(n)]
    queue = deque([(x, y)])
    dist[x][y] = 0


while True:
    value = find(bfs())