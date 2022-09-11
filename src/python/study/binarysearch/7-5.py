# 실전 문제 - 부품 찾기

# 매장 부품 입력
n = int(input())
# 부품 리스트 입력
n_list = list(map(int, input().split()))
# 문의한 부품 입력
m = int(input())
# 문의한 부품 리스트 입력
m_list = list(map(int, input().split()))

# 이진 탐색을 하기 위해 리스트를 정렬
n_list.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

    return None

# 손님이 주문한 부품이 있는지 확인하고 있으면 yes, 없으면 no 입력
for i in m_list:
    # 해당 부품이 있는지 확인
    result = binary_search(n_list, i, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')