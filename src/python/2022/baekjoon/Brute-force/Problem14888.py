# 백준 14888번 연산자 끼워넣기
# 유형: 브루트포스
# 난이도: 실버1

import sys
from itertools import permutations

input = sys.stdin.readline

# 수의 개수 입력
N = int(input())
# 순열 입력
nums = list(map(int, input().split()))
# 연산자 입력
op_num = list(map(int, input().split()))
# 연산자
op_list = ['+', '-', '*', '/']
# 연산자 리스트
op = []

max_num = -1e9
min_num = 1e9

for i in range(len(op_num)):
    for j in range(op_num[i]):
        op.append(op_list[i])

for case in permutations(op, N-1):
    total = nums[0]
    for i in range(1, N):
        if case[i-1] == '+':
            total += nums[i]
        elif case[i-1] == '-':
            total -= nums[i]
        elif case[i-1] == '*':
            total *= nums[i]
        elif case[i-1] == '/':
            total = int(total / nums[i])

    if total > max_num:
        max_num = total
    if total < min_num:
        min_num = total

print(max_num)
print(min_num)