import random

# Deck Setup 
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

# Helper Functions 
def parse_card(card):
    """Return color and value, ignoring declared color in parentheses."""
    if "(" in card:  # e.g., Wild (Red)
        base, declared = card.split("(")
        return declared.strip(")"), base.strip()
    if card.startswith("Wild"):
        return "Wild", card
    color, value = card.split(" ", 1)
    return color, value

def get_wild_color():
    colors = ["Red", "Yellow", "Green", "Blue"]
    while True:
        color = input(f"Choose a color ({'/'.join(colors)}): ").capitalize()
        if color in colors:
            return color
        print("Invalid color. Try again.")

def is_playable(card, top_card):
    card_color, card_value = parse_card(card)
    top_color, top_value = parse_card(top_card)
    return (
        card_color == "Wild"
        or card_color == top_color
        or card_value == top_value
    )

# Game Setup
num_players = int(input("How many players? "))

deck = create_uno_deck()
random.shuffle(deck)

hands = deal_hands(deck, num_players)

# Initialize discard pile and handle first card if Wild
top_card = deck.pop()
if top_card.startswith("Wild"):
    chosen_color = get_wild_color()
    top_card = f"{top_card} ({chosen_color})"

discard_pile = [top_card]
current_player = 0

# Main Game Loop
while True:
    print("\n----------------------------")
    print(f"Top card: {discard_pile[-1]}")
    print(f"Player {current_player + 1}'s turn")
    print("Hand:")
    for i, card in enumerate(hands[current_player]):
        print(f"{i}: {card}")

    # Determine playable cards
    playable_indices = [
        i for i, card in enumerate(hands[current_player])
        if is_playable(card, discard_pile[-1])
    ]

    # Draw if no playable cards
    if not playable_indices:
        print("No playable cards — drawing one.")
        if deck:
            hands[current_player].append(deck.pop())
        else:
            print("Deck is empty, skipping draw.")
    else:
        # Player chooses a card to play
        while True:
            try:
                choice = int(input("Choose a card index to play: "))
                if choice in playable_indices:
                    chosen_card = hands[current_player].pop(choice)

                    # Handle Wild cards
                    if chosen_card.startswith("Wild"):
                        chosen_color = get_wild_color()
                        chosen_card = f"{chosen_card} ({chosen_color})"

                    discard_pile.append(chosen_card)
                    break
                else:
                    print("That card is not playable. Try again.")
            except ValueError:
                print("Please enter a valid number.")

    # Check for win
    if len(hands[current_player]) == 0:
        print(f"\n Player {current_player + 1} wins!")
        break

    # Next player
    current_player = (current_player + 1) % num_players

