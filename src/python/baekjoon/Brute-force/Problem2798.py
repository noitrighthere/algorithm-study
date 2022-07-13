from itertools import combinations

# 백준 2798번 블랙잭
# 유형: 브루트포스
# 난이도: 브론즈2

N, M = map(int, input().split())    # N, M 입력
arr = list(map(int, input().split()))   # 카드 입력

combi = combinations(arr, 3)
temp = []

for i in combi:
    sum_combi = sum(i)
    if sum(i) <= M:
        temp.append(sum_combi)

print(max(temp))