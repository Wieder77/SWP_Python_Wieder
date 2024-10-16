import random
#cards = [i for i in range(0, 52)]
suits = ["\u2663", "\u2660", "\u2666", "\u2665"]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def show_cards(cards):
    picked = []
    for i in range(0,5):
        card_suits = suits[cards[i] % 4]
        card_value = values[cards[i] % 13]
        picked.append(card_value + card_suits)
    print(" ".join(picked))


def pick_cards():
    cards = [i for i in range(52)]
    print(cards)
    for i in range(len(cards)):
        ran = random.randint(0, len(cards) - i - 1)
        cards[ran], cards[-i] = cards[-i], cards[ran]
    show_cards(cards)


if __name__ == "__main__":
    random_card = random.randint(0, 51)
    pick_cards()

"""
 ran = random.randint(0, length-i-1)
lotto[ran], lotto[-i] = lotto[-i], lotto[ran]
"""

# Kombinationen: Paar, zwei Paare, Drillinge, Strasse, Flush, Full House, Vierling, Straight Flush, Royale Flush