N, M = map(int, input().split())

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수를 찾음
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰값을 찾음
    result = max(min_value, result)

print(result)