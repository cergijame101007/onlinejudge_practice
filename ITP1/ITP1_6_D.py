n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

b = []
for i in range(m):
    b.append(int(input()))

# print(matrix, b)

c = []
for i in range(n):
    product_sum = 0
    for j in range(m):
        product_sum += matrix[i][j] * b[j]
    c.append(product_sum)
# 読みづらい↑

# c = [0] * n
# for i in range(n):
#     for j in range(m):
#             c[i] += matrix[i][j] * b[j]
# こっちの方が読みやすい

for val in c:
    print(val)