# 프로그래머스 짝지어 제거하기
# 2017 팁스타운
# 난이도: LV2

def solution(s):
    answer = -1
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)

        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer

print(solution("cdcd"))