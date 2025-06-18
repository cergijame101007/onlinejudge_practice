notices_num = int(input())
notices_list = []
for i in range(notices_num):
    notices_list.append(list(map(int,input().split())))

buildings = [[[0] * 10 for i in range(3)] for j in range(4)]

for b, f, r, v in notices_list:
    buildings[b-1][f-1][r-1] += v

count = 0
for i in range(4):
    if count != 0:
        print('#' * 20)
    count += 1
    for j in range(3):
        # print(*buildings[i][j])    
        print(" " + " ".join(map(str, buildings[i][j])))
