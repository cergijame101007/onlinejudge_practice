n = int(input())
array = list(input().split())

def BubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if int(C[j][1]) < int(C[j - 1][1]):
                C[j], C[j - 1] = C[j - 1], C[j]
    return C

def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def isStable(ary, out, N):
    for i in range(N):
        for j in range(i + 1, N):
            for a in range(N):
                for b in range(a + 1, N):
                    if ary[i][1] == ary[j][1] and ary[i] == out[b] and ary[j] == out[a]:
                        print("Not stable")
                        return
    print("Stable")

bubble_result = BubbleSort(array.copy(), n)
selection_result = SelectionSort(array.copy(), n)

print(*bubble_result)
print("Stable")
print(*selection_result)
isStable(array, selection_result, n)