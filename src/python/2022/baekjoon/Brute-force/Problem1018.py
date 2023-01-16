# 백준 1018번 체스판 다시 칠하기
# 유형: 브루트포스
# 난이도: 실버4

n, m = map(int, input().split())    # N, M 입력
matrix = []
count = []

for _ in range(n):
    matrix.append(input())

for i in range(n-7):
    for j in range(m-7):
        idx1 = 0
        idx2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if matrix[a][b] != 'W':
                        idx1 += 1
                    if matrix[a][b] != 'B':
                        idx2 += 1
                else:
                    if matrix[a][b] != 'B':
                        idx1 += 1
                    if matrix[a][b] != 'W':
                        idx2 += 1

        count.append(min(idx1, idx2))
print(min(count))