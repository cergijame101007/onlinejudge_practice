import sys

lists = sys.stdin.read().splitlines()

nums = list(map(int, lists[0].split()))

# 面番号
labels = [1, 2, 3, 4, 5, 6]

command = lists[1]

dice_dict = { label : num for label, num in zip(labels, nums) }

# 初期状態の面のラベル：[top, front, right, left, back, bottom]
dice = [1, 2, 3, 4, 5, 6]

def roll_north(dice):
    return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

def roll_south(dice):
    return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

def roll_east(dice):
    return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

def roll_west(dice):
    return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

for token in command:
    if token == 'N':
        dice = roll_north(dice)
    elif token == 'S':
        dice = roll_south(dice)
    elif token == 'E':
        dice = roll_east(dice)
    elif token == 'W':
        dice = roll_west(dice)

print(dice_dict[dice[0]])