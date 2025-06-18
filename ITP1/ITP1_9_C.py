n = int(input())
point_list = [0] * 2
for i in range(n):
    taro_card, hanako_card = map(str, input().split())
    if taro_card > hanako_card:
        point_list[0] += 3
    elif taro_card < hanako_card:
        point_list[1] += 3
    else:
        point_list = [val + 1 for val in point_list]

print(*point_list)
    