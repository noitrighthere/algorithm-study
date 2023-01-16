# 모험가 길드

n = int(input())
data = list(map(int, input().split()))
data.sort()     # 오름차순으로 정리

result = 0
count = 0

for i in data:
    count += 1
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹을 형성
        result += 1
        count = 0

print(result)