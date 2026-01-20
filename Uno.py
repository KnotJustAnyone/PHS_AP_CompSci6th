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

num_players = int(input("How many players? "))

deck = create_uno_deck()
random.shuffle(deck)  

hands = deal_hands(deck, num_players)

print("\nYour hand:")
for card in hands[0]:
    print(card)
