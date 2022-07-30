# 백준 1541번 잃어버린 괄호
# 유형: 그리디
# 난이도: 실버2

n = input().split('-')
num = []

for i in n:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

temp = num[0]   # 식의 첫 번째

for i in range(1, len(num)):
    temp -= num[i]

print(temp)