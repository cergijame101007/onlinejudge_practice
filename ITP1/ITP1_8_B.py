while True:
    x = input()

    if x == '0':
        break

    digit = 0
    for ch in x:
        digit += int(ch)
    print(digit)
