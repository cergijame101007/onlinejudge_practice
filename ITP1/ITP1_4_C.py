while True:
    table = input().split()
    a = int(table[0])
    op = str(table[1])
    b = int(table[2])

    if op == '?':
        break
    elif op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    else:
        print(a//b)

    # match op:
    #     case '?':
    #         break
    #     case '+':
    #         print(a + b)
    #     case '-':
    #         print(a - b)
    #     case '*':
    #         print(a * b)
    #     case _:
    #         print(a // b)


    
