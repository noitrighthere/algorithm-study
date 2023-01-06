# N: 볼링공의 수, M: 볼링공의 최대 무게
N, M = map(int, input().split())
# 볼링공의 무게 입력
data = list(map(int, input().split()))
# 1~10까지 담을 수 있는 리스트
arr = [0] * 11

# 각 무게에 해당하는 리스트 카운트
for i in data:
    arr[i] += 1

result = 0

# 1~M까지 무게에 대하여 처리
for i in range(1, M+1):
    # 무게가 i인 볼링공의 개수 제외
    # B가 선택할 수 있는 경우의 수와 곱함
    N -= arr[i]
    result += arr[i] * N

print(result)