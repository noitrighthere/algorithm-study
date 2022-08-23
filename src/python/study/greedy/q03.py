# 문자열 뒤집기

S = input()
temp = []

for i in range(len(S) -1):
    if S[i] != S[i+1]:
        temp.append(S[i])

temp.append(S[-1])

print(min(temp.count('0'), temp.count('1')))