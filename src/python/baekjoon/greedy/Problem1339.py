# 백준 1339번 단어 수학
# 유형: 그리디
# 난이도: 골드4

N = int(input())
temp = []   # 단어
result = 0
alpha = [0 for _ in range(26)]

for _ in range(N):
    temp.append(input())

for i in temp:
    idx = 0

    while i:
        cur = i[-1]
        alpha[ord(cur) - ord('A')] += pow(10, idx)
        idx += 1
        i = i[:-1]

alpha.sort(reverse=True)

for i in range(9, 0, -1):
    result += i * alpha[9 - i]

print(result)