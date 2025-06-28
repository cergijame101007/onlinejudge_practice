n = int(input())
array = list(map(int,input().split()))

count = 0
for i in range(n):
    minj = i
    for j in range(i,n):
        if array[j] < array[minj]:
            minj = j
    if i != minj:
        temp = array[i]
        array[i] = array[minj]
        array[minj] = temp
        count += 1

print(" ".join(map(str, array)))
print(count)
