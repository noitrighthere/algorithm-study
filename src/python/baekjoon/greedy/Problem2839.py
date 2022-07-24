# 백준 2839번 설탕배달
# 유형: 그리디
# 난이도: 실버4

N = int(input())    # N입력
result = 0

# N이 5의 배수 또는 3의 배수가 아닐 경우 -1
while(True):
    if N % 5 == 0:
        result += (N//5)
        break

    N -= 3
    result += 1

    if N < 0:
        result = -1
        break

print(result)