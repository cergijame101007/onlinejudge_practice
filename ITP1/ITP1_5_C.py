# while True:
#     H, W = map(int, input().split())

#     if H == 0 and W == 0:
#         break

#     for i in range(H):
#         for j in range(W):
#             if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
#                 print('#', end='')
#             elif i%2 == 1 and j%2 == 0:
#                 print('.', end='')
#             else:
#                 print('.', end='')
#         print('')
#     print('')

while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break

    for i in range(H):
        for j in range(W):
            if (i + j) % 2 ==0:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')