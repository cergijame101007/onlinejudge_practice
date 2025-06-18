a, b, c = map(int, input().split())
if 0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100:
    if a < b and b < c:
        print("Yes")
    else:
        print("No")