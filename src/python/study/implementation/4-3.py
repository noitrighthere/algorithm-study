# 현재 나이트 위치 입력
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0

for step in steps:
    # 이동하고자 하는 현재 위치 확인
    next_row = row + step[0]
    next_col = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)