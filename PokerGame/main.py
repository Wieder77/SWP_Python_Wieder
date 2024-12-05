import random



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

def get_cards_looks(cards):
    suits = ["\u2663", "\u2660", "\u2666", "\u2665"]
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return suits, values

def show_cards(cards):
    picked = []
    suits, values = get_cards_looks(cards)
    for i in range(0, 5):
        card_suits = suits[cards[i] % 4]
        card_value = values[cards[i] % 13]
        picked.append(card_value + card_suits)
    print(f"Cards indices: {cards}")
    print(f"Picked cards: {' '.join(picked)}")


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

def has_pair(cards):
    card_values = [x % 13 for x in cards]
    count = {}
    for value in card_values:
        count[value] = count.get(value, 0) + 1
    values = list(count.values())
    values.sort(reverse=True)
    if 4 in values:
        return "four"
    elif 3 in values and 2 in values:
        return "fullHouse"
    elif 3 in values:
        return "three"
    elif values.count(2) == 2:
        return "twoPair"
    elif 2 in values:
        return "pair"

def check_combination(cards, number_cards):
    if royalflush(cards):
        statistics("royaleFlush")
    elif straight_flush(cards):
        statistics("straightFlush")
    elif has_pair(cards) == "four":
        statistics("four")
    elif has_pair(cards) == "fullHouse":
        statistics("fullHouse")
    elif flush(cards):
        statistics("flush")
    elif straight(cards):
        statistics("straight")
    elif has_pair(cards) == "three":
        statistics("three")
    elif has_pair(cards) == "twoPair":
        statistics("twoPair")
    elif has_pair(cards) == "pair":
        show_cards(cards)
        statistics("pair")
    else:
        statistics("highcard")

def pick_cards(number_cards):
    try:
        cards = [i for i in range(52)]
        for i in range(number_cards + 1):
            ran = random.randint(0, len(cards) - i - 1)
            cards[ran], cards[-i] = cards[-i], cards[ran]
        check_combination(cards[-number_cards:], number_cards)
    except IndexError as e:
        print("Error picking cards: not enough cards left.")
        raise e


def main():
    for i in range(0, 1000000):
        pick_cards(5)
    for key, values in poker_hands.items():
        print(f"{key} :  {(values/number_combinations) * 100}%")


if __name__ == "__main__":
    main()
