# 백준 1026번 보물
# 유형: 그리디
# 난이도: 실버4

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

A.sort()
B.sort(reverse=True)

for i in range(N):
    result += A[i] * B[i]

print(result)