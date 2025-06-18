while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    sum = m + f

    if m == -1 or f == -1:
        print('F')
    elif sum >= 80:
        print('A')
    elif 65 <= sum < 80:
        print('B')
    elif 50 <= sum < 65:
        print('C')
    elif r >= 50:
        print('C')   
    elif 30 <= sum < 50:
        print('D')
    else:
        print('F')