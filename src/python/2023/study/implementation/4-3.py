# 왕실의 나이트

# 방향
steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 현재 나이트가 위치한 곳의 좌표
current = input()
# 행(가로)
row = int(current[1])
# 열(세)
col = int(ord(current[0])) - int(ord('a')) + 1

count = 0

for step in steps:
    n_row = row + step[0]
    n_col = col + step[1]

    if 1 <= n_row <= 8 and 1 <= n_col <= 8:
        count += 1

print(count)