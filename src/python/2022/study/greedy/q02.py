# 곱하기 혹은 더하기

"""
내가 푼
"""
# s = input()
# result = 0
#
# for i in range(len(s)):
#     # s[i]가 0 또는 1이면 다음에 들어올 s[i+1]는 '+'
#     if s[i] == '0' or s[i] == '1' or result == 0 or result == 1:
#         result += int(s[i])
#     else:
#         result *= int(s[i])
#
# print(result)

"""
답
"""
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)