import random

# deck of cards /  player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        'A', 'J', 'Q', 'K',
        'A', 'J', 'Q', 'K',
        'A', 'J', 'Q', 'K',
        'A', 'J', 'Q', 'K',]

player_hand = []
dealer_hand = []
# deal the cards
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

deal_card(player_hand)
print(player_hand)
# calculate the total of each hand
# check for winner
# game loop