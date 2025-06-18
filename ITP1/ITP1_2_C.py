# list = list(map(int, input().split()))
# sortedlist = sorted(list)
# print(*sortedlist)

list = list(map(int, input().split()))
for i in range(len(list) - 1):
    left = 0
    right = 1
    while right < len(list):
        if list[left] > list[right]:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
        left += 1
        right += 1
print(*list)
