# 백준 7568번 덩치
# 유형: 브루트포스
# 난이도: 실버5

N = int(input())    # 전체 사람 수 입력
spec = []

for _ in range(N):
    x, y = map(int, input().split())    # x: 키, y: 몸무게 입력
    spec.append((x, y))

for i in spec:
    rank = 1
    for j in spec:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end = ' ')