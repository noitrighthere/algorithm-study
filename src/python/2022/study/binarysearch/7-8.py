# 실전 문제 - 떡볶이 떡 만들기

# 떡의 개수와 요청한 떡의 길이를 입력
n, m = map(int, input().split())
# 각 떡의 개별 높이 입력
arr = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점을 설정
start = 0
end = max(arr)

result = 0

while (start <= end):
    # 전체 잘린 떡의 길이
    total = 0
    mid = (start + end) // 2

    for i in arr:
        # 잘랐을 때 떡의 양 계산
        if i > mid:
            total += i - mid

    # 떡의 양이 부족한 경우 더 많이 자름(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)