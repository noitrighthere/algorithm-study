# 점수 N 입력
N = input()
# 점수를 반으로 나
half = len(N) // 2

result = 0

# 왼쪽 부분의 자릿수 합
for i in range(half):
    result += int(N[i])

# 오른쪽 부분의 자릿수 합을 왼쪽 부분의 자릿수 합에서 뺌
for i in range(half, len(N)):
    result -= int(N[i])

if result == 0:
    print("LUCKY")
else:
    print("READY")