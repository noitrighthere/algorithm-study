# 백준 23290번 마법사 상어와 복제
# 유형: 구현
# 난이도: 골드1
import copy
import sys
sys.setrecursionlimit(10 ** 6)

# m : 물고기 수
# s : 마법 연습 횟수
m, s = map(int, input().split())

# 물고기 정보 입력
fish = [list(map(int, input().split())) for _ in range(m)]

# 격자 입력
board = [[[] for _ in range(4)] for _ in range(4)]

# 입력된 물고기 정보로 격자에 입력함
for f_x, f_y, f_d in fish:
    board[f_x - 1][f_y - 1].append(f_d - 1)

# 상어의 위치 입력
shark = tuple(map(lambda x: int(x) - 1, input().split()))

# 물고기 냄새
smell = [[0] * 4 for _ in range(4)]

# 물고기가 이동할 수 있는 방향
f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어가 이동할 수 있는 방향
s_dx = [-1, 0, 1, 0]
s_dy = [0, -1, 0, 1]

# 물고기 이동을 정의하는 메서드
def move():
    res = [[[] for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                # 물고기가 이동할 수 있는 방향으로 45도 반시계 이동
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    # 물고기는 상어가 있는 칸, 물고기 냄새가 있는 칸, 격자를 벗어나서 이동할 수 없음
                    if 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny] and (nx, ny) != shark:
                        # 해당 위치로 물고기가 이동
                        res[nx][ny].append(i)
                        break
                    # 이동할 수 없으면 가만히 있음
                    else:
                        res[x][y].append(d)

    return res

# 상어 이동을 정의하는 메서드
def dfs(x, y, dep, cnt, visited):
    global max_eat, shark, eat

    # 상어가 세번 이동한 경우 이동을 멈춤
    if dep == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visited[:]
        return

    # 상어는 상하좌우로 이동
    for d in range(4):
        nx, ny = x + s_dx[d], y + s_dy[d]
        # 격자를 벗어날 수 없음
        if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visited)
            visited.pop()
        else:
            dfs(nx, ny, dep + 1, cnt, visited)


# 복제 마법 시전
for _ in range(s):
    eat = list()
    max_eat = -1

    # 1. 모든 물고기 복제
    temp = copy.deepcopy(board)
    # 2. 물고기 이동
    temp = move()
    # 3. 상어 이동
    dfs(shark[0], shark[1], 0, 0, list())

    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3

    # 4. 냄새가 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

    # 5. 복제 마법
    for i in range(4):
        for j in range(4):
            board[i][j] += temp[i][j]

# 물고기의 수를 구함
result = 0

for i in range(4):
    for j in range(4):
        result += len(board[i][j])

print(result)
