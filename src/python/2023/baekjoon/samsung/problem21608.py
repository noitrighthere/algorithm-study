# 상어 초등학교

N = int(input())

# 교실
graph = [[0]*N for _ in range(N)]

# 학생의 번호와 좋아하는 학생 4명의 번호
students = [list(map(int, input().split())) for _ in range(N**2)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for idx in range(N**2):
    # 순차적으로 학생의 정보를 꺼내서 자리 배치를 시작
    student = students[idx]
    temp = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:

                # 인접한 곳에 좋아하는 학생이 있는 수
                like = 0
                # 인접한 칸 중에서 비어있는 칸의 수
                blank = 0

                # 인접한 칸을 구함
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    # 교실 밖을 벗어나지 않아야 함
                    if 0 <= nx < N and 0 <= ny < N:
                        # 인접한 칸에 좋아하는 학생이 있으면 +1
                        if graph[nx][ny] in student[1:]:
                            like += 1
                        if graph[nx][ny] == 0:
                            blank += 1

                # 자리를 결정하는 우선순위 조건에 따라서 임시 배열에 저장
                temp.append([like, blank, i, j])

    # 우선순위에 맞게 정렬
    temp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    # 해당 위치에 학생의 번호 입력
    graph[temp[0][2]][temp[0][3]] = student[0]

result = 0
students.sort()

# 학생의 만족도를 구해야함
for i in range(N):
    for j in range(N):
        score = 0
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            # 범위를 벗어나지 말아야 함
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] in students[graph[i][j] -1]:
                    score += 1

        if score != 0:
            result += 10 ** (score-1)

print(result)