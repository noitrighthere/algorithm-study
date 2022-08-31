# 문자열 압축

s = input()     # 문자열 입력
result = []     # 전체 결과를 받을 배

# 1. N/2 까지의 모든 경우의 수를 구함
for i in range(1, len(s)//2 + 1):

    temp = ""       # 출력되는 문자열 결과
    prev = s[0:i]   # 문자열 단위
    count = 1
    # 2. 단위대로 비교해서 입축되는 길이가 같은 수를 구함
    for j in range(i, len(s), i):
        # 문자열 단위대로 맞아떨어지면 count + 1을 해줌
        if prev == s[j:j+i]:
            count += 1
        # 문자열 단위대로 안맞아 떨어지면 문자열을 count와 붙임
        else:
            # count가 1이상일 때만 count를 붙이고 아니면 그냥 단위로 붙임
            if count >= 2:
                temp += str(count) + prev
            else:
                temp += prev
            # prev를 초기화
            prev = s[j:j+i]
            count = 1

    # 남아있는 문자열에 대해서 처리
    temp += str(count) + prev if count >= 2 else prev
    # 만들어진 문자열을 result 배열에 넣음
    result.append(temp)

print(len(min(result)))