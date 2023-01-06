import sys

# 백준 1946번 신입 사원
# 유형: greedy
# 난이도: 실버1

T = int(sys.stdin.readline())    # 테스트 케이스 입력

for _ in range(T):
    N = int(sys.stdin.readline())    # 지원자의 숫자 입력
    arr = []
    count = 1

    for _ in range(N):
        # a: 서류, b: 면접
        a, b = map(int, sys.stdin.readline().split())
        arr.append([a, b])

    arr.sort()
    tempMax = arr[0][1]

    for i in range(1, N):
        if tempMax > arr[i][1]:
            count += 1
            tempMax = arr[i][1]

    print(count)