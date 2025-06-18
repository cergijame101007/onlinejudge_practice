r, c = map(int, input().split())

table = []
for i in range(r):
    table.append(list(map(int, input().split())))

for row in table:
    row.append(sum(row))

col_sum = []
for col in zip(*table):
    col_sum.append(sum(col))

table.append(col_sum)

for row in table:
    print(*row)
