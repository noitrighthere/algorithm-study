# 백준 2309번 일곱 난쟁이
# 유형: 브루트포스
# 난이도: 브론즈1

stack = []
for _ in range(9):
    stack.append(int(input()))

flag = False
stack.sort()
sum_stack = sum(stack)

for i in range(9):

    if flag:
        break

    for j in range(i+1, 9):

        if sum_stack - stack[i] - stack[j] == 100:

            stack.pop(i)
            stack.pop(j-1)

            for result in stack:
                print(result)

            flag = True
            break