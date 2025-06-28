def insertationSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v

def shellSort(A, n):
    G = [1]
    for i in range(99):
        if n < 1 + 3*G[-1]:
            break
        G.append(1 + 3*G[-1])
    m = len(G)
    print(m)
    G.reverse()
    for i in range(m):
        insertationSort(A, n, G[i])
    print(*G)


n = int(input())
A = [int(input()) for i in range(n)]
cnt = 0

shellSort(A, n)
print(cnt)
print(*A, sep="\n")