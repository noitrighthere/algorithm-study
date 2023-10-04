# 놀이기구 탑승

# n: 격자의 크기
n = int(input())

# 학생의 번호와 좋아하는 학생 4명의 번호
student_info = [list(map(int, input().split())) for _ in range(n**2)]

# 그래프
graph = [[0]*n for _ in range(n)]

# 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for idx in range(n**2):
    # 순차적으로 학생의 정보를 꺼냄
    student = student_info[idx]
    # 자리 배치를 위한 임시 배열
    temp = []

    for i in range(n):
        for j in range(n):
            # 자리에 학생이 없어야 함
            if graph[i][j] == 0:
                # 인접한 곳에 있는 좋아하는 학생의 수
                like = 0
                # 인접한 칸 중에서 비어있는 칸의 수
                blank = 0

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    # 격자 밖으로 벗어나지 않아야 함
                    if 0 <= nx < n and 0 <= ny < n:
                        # 인접한 칸에 좋아하는 학생이 있으면 +1
                        if graph[nx][ny] in student[1:]:
                            like += 1
                        # 인접한 칸 중 비어있는 칸이 있으면 + 1
                        if graph[nx][ny] == 0:
                            blank += 1

                # 우선순위 요소대로 배열에 붙임
                temp.append([like, blank, i, j])

    # 우선순위에 맞게 정렬
    temp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    graph[temp[0][2]][temp[0][3]] = student[0]

# 최종 점수
result = 0
student_info.sort()

for i in range(n):
    for j in range(n):
        # 좋아하는 친구의 수
        cnt = 0
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            # 격자를 벗어나지 않아야 함
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in student_info[graph[i][j] -1]:
                    cnt +=1

        if cnt != 0:
            result += 10 ** (cnt - 1)

print(result)