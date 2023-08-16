# N, M, K를 공백으로 구분하여 입력
N, M, K = map(int, input().split())
# 배열 입력
arr = list(map(int, input().split()))

arr.sort()

first = arr[N-1]
second = arr[N-2]

result = 0

while True:
    for _ in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)