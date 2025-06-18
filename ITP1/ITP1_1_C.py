n = input()

N0 = int(n.split()[0])
N1 = int(n.split()[1])

if (N0 >= 1 and N1 <= 100):
    print(f"{N0*N1} {N0*2 + N1*2}")
