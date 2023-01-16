# 백준 15686번 치킨 배
# 유형: 구현
# 난이도: 골드5

from itertools import combinations

# n, m 입력
n, m = map(int, input().split())
# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 집의 위치를 담을 배열
home = []
# 치킨집의 위치를 담을 배열
chicken = []

# 집과 치킨집의 위치를 기록
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

# 치킨집의 위치를 조합으로 나타
combi = list(combinations(chicken, m))
answer = len(combi) * [0]

for i in home:
    for j in range(len(combi)):
        min_result = 100
        for k in combi[j]:
            temp = abs(i[0]-k[0]) + abs(i[1]-k[1])
            min_result = min(min_result, temp)

        answer[j] += min_result

print(min(answer))