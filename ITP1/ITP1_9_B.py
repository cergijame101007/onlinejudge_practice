output = []

while True:
    deck = input()    
    if deck == "-":
        break
    num = int(input())

    for i in range(num):
        h = int(input())
        deck = deck[h:] + deck[:h]

    output.append(deck)

for val in output:
    print(val)