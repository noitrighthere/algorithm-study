# 프로그래머스 예상 대진표
# 2017 팁스타운
# 난이도: LV2
import math

def solution(n,a,b):
    answer = 0

    while a != b:
        a, b = math.ceil(a/2), math.ceil(b/2)
        answer += 1

    return answer

print(solution(8, 4, 7))