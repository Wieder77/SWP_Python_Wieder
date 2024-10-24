import random

# cards = [i for i in range(0, 52)]
suits = ["\u2663", "\u2660", "\u2666", "\u2665"]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# fuer die Statistik
number_combinations = 0
poker_hands = {
    "highcard": 0,
    "pair": 0,
    "twoPair": 0,
    "three": 0,
    "straight": 0,
    "flush": 0,
    "fullHouse": 0,
    "four": 0,
    "straightFlush": 0,
    "royaleFlush": 0
}

def show_cards(cards):
    picked = []
    for i in range(0, 5):
        card_suits = suits[cards[i] % 4]
        card_value = values[cards[i] % 13]
        picked.append(card_value + card_suits)
    print(" ".join(picked))


def statistics(combination):
    global number_combinations
    global poker_hands
    number_combinations += 1
    poker_hands[combination] += 1

def royalflush(cards):
    if straight_flush(cards):
        cards_sorted = [x % 13 for x in cards]
        cards_sorted.sort()
        if cards_sorted == [8, 9, 10, 11, 12]:  # Check for these exact values
            return True
    else:
        return False


def straight_flush(cards):
    if flush(cards) and straight(cards):
        return True
    else:
        return False
def four_pair(cards):
    cards_sorted = [x % 13 for x in cards]
    cards_sorted.sort()
    for i in range(len(cards_sorted) -3):
        if cards_sorted[i + 1] == cards_sorted[i] and cards_sorted[i + 2] == cards_sorted[i] and cards_sorted[i + 3] == cards_sorted[i]:
            return True
    return False

def fullhouse(cards):
    cards_sorted = [x % 13 for x in cards]
    cards_sorted.sort()
    three_pair_location = 100
    for i in range(len(cards_sorted) - 2):
        if cards_sorted[i + 1] == cards_sorted[i] and cards_sorted[i + 2] == cards_sorted[i]:
            three_pair_location = i
            break
    if three_pair_location == 0:
        if cards_sorted[3] == cards_sorted[4]:
            return True
    elif three_pair_location == 2:
        if cards_sorted[0] == cards_sorted[1]:
            return True
    else:
        return False

def flush(cards):
    compare = cards[0] % 4
    result = all(card % 4 == compare for card in cards)
    return result


def straight(cards):
    cards_sorted = [x % 13 for x in cards]
    cards_sorted.sort()
    if cards_sorted == [0, 1, 2, 3, 12]:
        return True
    elif cards_sorted[0] + 1 == cards_sorted[1]:
        for i in range(len(cards) - 1):
            if cards_sorted[i + 1] != cards_sorted[i] + 1:
                return False
        return True
def three_pair(cards):
    cards_sorted = [x % 13 for x in cards]
    cards_sorted.sort()
    for i in range(len(cards_sorted) -2):
        if cards_sorted[i + 1] == cards_sorted[i] and cards_sorted[i + 2] == cards_sorted[i]:
            return True
    return False

def two_pair(cards):
    cards_sorted = [x % 13 for x in cards]
    cards_sorted.sort()
    pair_count = 0
    for i in range(len(cards_sorted) -1):
        if cards_sorted[i + 1] == cards_sorted[i]:
            pair_count += 1
    if pair_count == 2:
        return True
def pair(cards):
    cards_sorted = [x % 13 for x in cards]
    cards_sorted.sort()
    for i in range(len(cards_sorted) -1):
        if cards_sorted[i + 1] == cards_sorted[i]:
            return True
    return False

def check_combination(cards, number_cards):
    if royalflush(cards):
        statistics("royaleFlush")
    elif straight_flush(cards):
        statistics("straightFlush")
    elif four_pair(cards):
        statistics("four")
    elif fullhouse(cards):
        statistics("fullHouse")
    elif flush(cards):
        statistics("flush")
    elif straight(cards):
        statistics("straight")
    elif three_pair(cards):
        statistics("three")
    elif two_pair(cards):
        statistics("twoPair")
    elif pair(cards):
        statistics("pair")
    else:
        statistics("highcard")

def pick_cards(number_cards):
    # list array 52 werte
    cards = [i for i in range(52)]
    # zieht karten
    for i in range(number_cards + 1):
        ran = random.randint(0, len(cards) - i - 1)
        cards[ran], cards[-i] = cards[-i], cards[ran]

    check_combination(cards[-number_cards:], number_cards)
    #print(cards[-number_cards:])
    #show_cards(cards[-number_cards:])


def main():
    for i in range(0, 1000000):
        random_card = random.randint(0, 51)
        pick_cards(5)
    for key, values in poker_hands.items():
        print(key)
        print(values/number_combinations)


if __name__ == "__main__":
    main()
