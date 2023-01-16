# 백준 14891번 톱니바퀴
# 유형: 구현
# 난이도: 골드5

from collections import deque

gear = {}

# 시계방향으로 회전
def rotate_right(x, d):
    if x > 4 or gear[x - 1][2] == gear[x][6]:
        return

    if gear[x - 1][2] != gear[x][6]:
        rotate_right(x + 1, -d)
        gear[x].rotate(d)

# 반시계방향으로 회전
def rotate_left(x, d):
    if x < 1 or gear[x][2] == gear[x + 1][6]:
        return

    if gear[x][2] != gear[x + 1][6]:
        rotate_left(x - 1, -d)
        gear[x].rotate(d)

# 톱니바퀴 입력
for i in range(1, 5):
    gear[i] = deque((map(int, input())))

# 회전 횟수
k = int(input())

# 회전시킨 톱니바퀴 번호, 방향 입력
for _ in range(k):
    x, d = map(int, input().split())

    rotate_right(x + 1, -d)
    rotate_left(x - 1, -d)
    gear[x].rotate(d)

result = 0
for i in range(4):
    result += gear[i + 1][0] * (2**i)

print(result)