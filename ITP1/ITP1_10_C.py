import math

while True:
    n = int(input())    
    if n == 0:
        break
    table = list(map(int, input().split()))
    m = sum(table) / n
    result = 0
    for i in range(n):
        result +=  pow(table[i] - m, 2) / n
    a = math.sqrt(result)
    print(f'{a:.8f}')

