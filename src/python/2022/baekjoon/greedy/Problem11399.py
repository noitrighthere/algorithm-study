# 백준 11399번 ATM
# 유형: 그리디
# 난이도: 실버4

N = int(input())    # 사람의 수 N 입력
arr = list(map(int, input().split()))   # 인출하는데 걸리는 시간 입력

result = 0

arr.sort()  # 오름차순으로 정렬

for i in range(N):
    result += sum(arr[:i+1])

print(result)