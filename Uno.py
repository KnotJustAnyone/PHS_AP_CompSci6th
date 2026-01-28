import random

def create_uno_deck():
    colors = ["Red", "Yellow", "Green", "Blue"]
    action_cards = ["Skip", "Reverse", "Draw Two"]
    deck = []

    for color in colors:
        deck.append(f"{color} 0")

        for num in range(1, 10):
            deck.extend([f"{color} {num}", f"{color} {num}"])

        for action in action_cards:
            deck.extend([f"{color} {action}", f"{color} {action}"])

    deck.extend(["Wild"] * 4)
    deck.extend(["Wild Draw Four"] * 4)

    return deck

def deal_hands(deck, num_players, cards_per_player=7):
    hands = [[] for _ in range(num_players)]

    for _ in range(cards_per_player):
        for player in range(num_players):
            hands[player].append(deck.pop())

    return hands

def parse_card(card):
    if card.startswith("Wild"):
        return ("Wild", card)
    color, value = card.split(" ", 1)
    return (color, value)


def is_playable(card, top_card):
    card_color, card_value = parse_card(card)
    top_color, top_value = parse_card(top_card)

    return (
        card_color == "Wild"
        or card_color == top_color
        or card_value == top_value
    )

#the set up
num_players = int(input("How many players? "))

deck = create_uno_deck()
random.shuffle(deck)

hands = deal_hands(deck, num_players)

discard_pile = [deck.pop()]
current_player = 0

#the loop

while True:
    print("\n----------------------------")
    print(f"Top card: {discard_pile[-1]}")
    print(f"Player {current_player + 1}'s turn")
    print("Hand:")

    for i, card in enumerate(hands[current_player]):
        print(f"{i}: {card}")

    playable_indices = [
        i for i, card in enumerate(hands[current_player])
        if is_playable(card, discard_pile[-1])
    ]

    if not playable_indices:
        print("No playable cards — drawing one.")
        hands[current_player].append(deck.pop())
    else:
        choice = int(input("Choose a card index to play: "))

        if choice in playable_indices:
            chosen_card = hands[current_player].pop(choice)
            discard_pile.append(chosen_card)
        else:
            print("That card is not playable. Try again.")
            continue

    if len(hands[current_player]) == 0:
        print(f"\n🎉 Player {current_player + 1} wins!")
        break

    current_player = (current_player + 1) % num_players
