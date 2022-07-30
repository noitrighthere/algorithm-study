# 백준 1931번 회의실 배정
# 유형: 그리디
# 난이도: 실버1

N = int(input())
arr = []

for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

last = 0
cnt = 0

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

for i, j in arr:
    if i >= last:
        cnt += 1
        last = j

print(cnt)