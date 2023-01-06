# 만들 수 없는 금액

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
temp = 1

for i in arr:
    if temp < i:
        break
    temp += i

print(temp)