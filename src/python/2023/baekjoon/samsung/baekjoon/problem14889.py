# 스타트와 링크
from itertools import combinations

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
members = list(range(N))
team = []

combi = list(combinations(members, N//2))

answer = 1000

for i in combi:
    team.append(i)

for i in range(len(team)//2):
    start = team[i]

    start_sum = 0

    for j in range(N//2):
        temp = start[j]
        for k in start:
            start_sum += graph[temp][k]

    link = team[-i-1]
    link_sum = 0

    for j in range(N//2):
        temp = link[j]
        for k in link:
            link_sum += graph[temp][k]

    answer = min(answer, abs(start_sum - link_sum))

print(answer)