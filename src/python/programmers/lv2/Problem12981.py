# 프로그래머스 영어 끝말잇기
# Summer/Winter Coding(~2018)
# 난이도: LV2

def solution(n, words):

    for i in range(1, len(words)):
        # 같은 단어가 반복하거나 앞 글자의 마지막과 뒷 글자의 첫번째가 다른 경우
        if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
            # 가장 먼저 탈락하는 사람, 몇 번째 차례인지 구함
            return [(i%n)+1, (i//n)+1]
    # 아닌 경우 [0, 0]
    return [0, 0]

words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(3, words))