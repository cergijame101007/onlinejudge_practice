n = int(input())
array = list(map(int,input().split()))

count = 0
for i in range(n):
    for j in range(n-1, i, -1):
        if array[j] <  array[j - 1]:
            temp = array[j - 1]
            array[j - 1] = array[j]
            array[j] = temp
            count += 1

print(" ".join(map(str, array)))
print(count)
