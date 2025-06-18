import sys

lists = sys.stdin.read().splitlines()

nums = list(map(int, lists[0].split()))
num_query = int(lists[1])
queries = [tuple(map(int, line.split())) for line in lists[2:]]

# 面番号
labels = [1, 2, 3, 4, 5, 6]
dice_dict = { label : num for label, num in zip(labels, nums) }

# 初期状態の面のラベル：[top, front, right, left, back, bottom]
dice = [dice_dict[label] for label in labels]

def roll_north(dice):
    return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

def roll_south(dice):
    return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

def roll_east(dice):
    return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

def roll_west(dice):
    return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

def roll_right(dice):
    return [dice[0], dice[3], dice[1], dice[4], dice[2], dice[5]]

for i in range(num_query):
    for j in range(4):
        if queries[i][1] == dice[1]:
            break
        dice = roll_north(dice)
    for j in range(4):
        if queries[i][1] == dice[1]:
            break
        dice = roll_right(dice)
    
    for j in range(4):
        if queries[i][0] == dice[0]:
            break
        dice = roll_east(dice)
    print(dice[2])