alfabet_list = 'abcdefghijklmnopqrstuvwxyz'
table = [0] * 26

while True:
    try:
        str = input().lower()
    except:
        break

    for i in str:
        index = 0
        for j in alfabet_list:
            if i == j:
                table[index] += 1
                break
            index += 1

for i in range(len(alfabet_list)):
    print(f"{alfabet_list[i]} : {table[i]}")


"""
from sys import stdin

table = [0] * 26
for line in stdin:
    for ch in line.lower():
        if 'a' <= ch <= 'z':
            table[ord(ch) - ord('a')] += 1

for i in range(26):
    print(f"{chr(ord('a') + i)} : {table[i]}")
"""
    