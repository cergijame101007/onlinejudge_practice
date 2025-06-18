n = int(input())
sequence = list(map(int, input().split()))
left = 0
right = len(sequence) - 1

for i in range(len(sequence) - 1):
    if left != len(sequence) / 2:
        temp = sequence[left]
        sequence[left] = sequence[right]
        sequence[right] = temp
        left += 1
        right -= 1 

print(*sequence)