# 백준 21608번 상어 초등학교
# 유형: 구현
# 난이도: 골드5

# n : 교실 크기
n = int(input())

# 교실 입력
board = [[0] * n for _ in range(n)]

# 학생 입력
student_list = [list(map(int, input().split())) for _ in range(n**2)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 학생 수 만큼 자리를 배치
for idx in range(n**2):
    student = student_list[idx]

    # 가능한 자리를 담아서 정렬 후 앉힘
    temp = []
    for i in range(n):
        for j in range(n):
            # 이미 교실안에 학생이 자리에 있으면 패스
            if board[i][j] == 0:
                like = 0
                blank = 0

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    # 교실 밖으로 벗어나지 않아야 함
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생이 인접해 있으면 like에 +1
                        if board[nx][ny] in student[1:]:
                            like += 1
                        # 해당위치가 비어있는 칸이면 blank에 +1
                        if board[nx][ny] == 0:
                            blank += 1

                # 학생 배치 조건을 임시 배열에 넣음
                # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
                # 2. 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
                # 3. 행의 번호가 가장 작은 칸, 열의 번호가 가장 작은 칸
                temp.append([like, blank, i, j])

    # like와 blank는 내림차순, 행과 열은 내림차순으로 정렬
    temp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    # 제일 앞에 있는 리스트의 행과 열 번호에 학생을 배치
    board[temp[0][2]][temp[0][3]] = student[0]

result = 0
# 만족도를 매기기 전에 학생을 정렬해줌
student_list.sort()

for i in range(n):
    for j in range(n):
        score = 0
        # 상하좌우를 살펴서 해당 학생 위치에 인접한 좋아하는 학생의 수를 구함
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            # 교실 밖을 벗어나지 않아야 함
            if 0 <= nx < n and 0 <= ny < n:
                # 좋아하는 학생이 인접해 있는지 확인
                if board[nx][ny] in student_list[board[i][j]-1]:
                    score += 1
        # 만족도가 0이 아니면 계산
        if score != 0:
            result += 10 ** (score-1)

print(result)