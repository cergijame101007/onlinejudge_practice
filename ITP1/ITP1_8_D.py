import sys

lines = sys.stdin.read().splitlines()
s = lines[0]
p = lines[1]

str = s + s

if p in str:
    print('Yes')
else:
    print('No')