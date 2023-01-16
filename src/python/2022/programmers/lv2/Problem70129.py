# 프로그래머스 이진 변환 반복하기
# 월간 코드 챌린지 시즌1
# 난이도: LV2

def solution(s):
    answer = []
    zero_cnt = 0
    case_cnt = 0

    while True:
        # 문자열 s가 '1'일 때 종료
        if s == '1':
            break

        # 문자열 s에서 '0'의 개수를 셈
        zero_cnt += s.count('0')
        # 문자열 s에서 '0'을 제거
        s = s.replace('0', '')

        # 제거된 문자열 s의 글자수를 이진법으로 변환
        s = bin(len(s))[2:]
        case_cnt += 1

    answer = [case_cnt, zero_cnt]

    return answer