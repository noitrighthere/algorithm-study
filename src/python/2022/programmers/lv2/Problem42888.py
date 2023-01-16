# 프로그래머스 오픈채팅
# 2019 KAKAO BLIND RECRUITMENT
# 난이도: LV2

def solution(record):
    answer = []
    dic = {}

    # {아이디:닉네임} 형태로 만듦
    for sentence in record:
        s = sentence.split(' ')

        # 나간 경우는 확인하지 않음
        if len(s) == 3:
            dic[s[1]] = s[2]

    # 명령어대로 출력
    for sentence in record:
        s = sentence.split(' ')

        # Enter의 경우
        if s[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[s[1]])
        elif s[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[s[1]])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

print(solution(record))