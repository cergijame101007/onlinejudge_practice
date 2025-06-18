card_list = []
suits = ['S', 'H', 'C', 'D']
for suit in suits:
    for i in range(1,14):
        card_list.append(f"{suit} {i}")

card_num = int(input())
input_card_list = []
for i in range(card_num):
    input_card_list.append(input())

# missing_cards = set(card_list) - set(input_card_list)

# for card in card_list:
#     if card in missing_cards:
#         print(card)

for card in card_list:
    if card not in input_card_list:
        print(card)