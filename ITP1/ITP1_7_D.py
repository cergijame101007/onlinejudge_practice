n, m, l = map(int, input().split())

matrix_A = []
for i in range(n):
    matrix_A.append(list(map(int, input().split())))

matrix_B = []
for j in range(m):
    matrix_B.append(list(map(int, input().split())))

matrix_C = [[0] * l for i in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]

for row in matrix_C:
    print(*row)