import math

x1, y1, x2, y2 = map(float, input().split())

result = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(f'{result:.8f}')