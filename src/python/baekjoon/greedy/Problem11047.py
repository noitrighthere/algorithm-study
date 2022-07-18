# 백준 11047번
# 유형: 그리디
# 난이도: 실버4

N, K = map(int, input().split())    # N, K 입력
coin_list = []

result = 0

# 동전 입력
for _ in range(N):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)    # 동전을 내림차순으로 만듬

for i in coin_list:
    temp = K // i
    result += temp
    K -= temp * i

print(result)