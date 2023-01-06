# 문자열 재정렬

s = input()

arrStr = []     # 문자열을 담을 배열
arrNum = []     # 숫자를 담을 배열

# 문자열의 문자가 숫자인 경우 arrNum에 넣고 아닌 경우 arrStr에 넣음
for i in s:
    if i.isdigit():
        arrNum.append(i)
    else:
        arrStr.append(i)

arrStr.sort()   # 문자열을 정렬

num = 0
result = ''

for i in arrNum:
    num += int(i)

for i in arrStr:
    result += i

print(result + str(num))