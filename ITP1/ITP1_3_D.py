a, b, c = map(int, input().split())
div = 0

for i in range(a, b+1):
    if c % i == 0:
        div += 1

print(div)
