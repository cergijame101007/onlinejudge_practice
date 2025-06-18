N0, N1 = map(int, input().split())

if N0 >= -1000 and N1 <= 1000:
    if N0 < N1:
        print("a < b")
    elif N0 > N1:
        print("a > b")
    else:
        print("a == b")