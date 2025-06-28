n, q = map(int, input().split())
queue = []
for _ in range(n):
    name, time = input().split()
    queue.append((name, int(time)))

result = []
elapsed_time = 0

while queue:
    name, time = queue.pop(0)
    if time <= q:
        elapsed_time += time
        result.append((name, elapsed_time))
    else:
        elapsed_time += q
        queue.append((name, (time - q)))

for name, time in result:
    print(name, time)
