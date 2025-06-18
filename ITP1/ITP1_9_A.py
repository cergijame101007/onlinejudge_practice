lists = []

while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    lists.append(line)


word = lists[0].lower()
count = 0
for row in lists[1:]:
    for token in row.lower().split():
        if token == word:
            count += 1

print(count)

