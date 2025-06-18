import math

a, b, C = map(int, input().split())
C_rad = math.radians(C)
S = 0.5 * a * b * math.sin(C_rad)
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C_rad))
h = b * math.sin(C_rad)
print(f'{S:.8f}')
print(f'{L:.8f}')
print(f'{h:.8f}')