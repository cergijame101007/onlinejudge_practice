import sys
import math

lists = sys.stdin.read().splitlines()

n = int(lists[0])
x = list(map(int, lists[1].split()))
y = list(map(int, lists[2].split()))

for i in range(1,4):
    D_xy = 0
    for j in range(n):
        D_xy += pow(abs(x[j] - y[j]), i)
    D_xy = pow(D_xy, (1 / i))
    print(f'{D_xy:.8f}')

D_xy_inf = [(abs(x[i] - y[i])) for i in range(n)] 
print(f'{max(D_xy_inf):.8f}')

