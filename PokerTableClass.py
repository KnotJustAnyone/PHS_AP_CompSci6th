#Texas Hold Em Sepcific

class poker_table:

    hand_values = {} #A dictionary identifying the name of numerically ordered hands

    def __init__(self):
        self.players = [] #List of players, need a player class
        self.pot = 0
        self.bets = []
        self.deck = None #Need a deck class
        self.table_cards = []
        self.current_player = None
        self.button_player = None

    def deal_hands(self): #Gives each player their initial two pocket cards
        return None

    def deal_table(self): #Adds cards to the table as needed
        return None

    #Identifies the best hand which can be made with the set of cards
    def best_hand(self,cards):
        hand_value = 0
        return hand_value #A number identifying the strength of the hand

    def add_player(self): #adds a new player at the table
        return None

    def remove_player(self): #removes a player
        return None

    def deal_round(self): #Goes through the steps of a poker round
        #gets blinds
        #deals pocket hands
        #calls for bets
        #deals to table and calls for bets (x3)
        #determines winning player or players
        #distributes winnings
        #moves button
        return None

    #Asks the player what they want to bet
    def player_bet(self,player,game_state):
            # simple checks
        if amount < table.min_bet:
            raise ValueError(f"Bet {amount} is below minimum {table.min_bet}")
        if amount > self.chips:
            raise ValueError(f"Cannot bet {amount}; only {self.chips} chips available")
        # perform bet
        self.chips -= amount
        self.current_bet += amount
        table.pot += amount
        # track last_bet / raise
        if amount > table.last_bet:
            table.last_bet = amount
            table.was_raised = True
        else:
            # if equal or lower, maybe not a raise
            table.was_raised = False  # or leave as is depending on logic


#Tests ---------------------------------------------
def test_best_hand():
    table = poker_table()
    hands = [
        ['c8'], #8 high
        ['c9','d9'], #pair of 9s
        ['c9','c6'], #9 high
        ['c6','c2'], #6 high
        ['d3','c3','h3'], #Three of 3s
        ['d3','c3','h4'], #pair of 3s
        ['cj','d3','dj'], #pair of jacks
        ['ck','d5','h2'], #king high
        ['c7','d7','h7','s7'], #four of a kind, 7s
        ['c7','d7','h7','ck']] #three 7s
    print(f"Identifies high card v1: {table.best_hand(hands[0]) < table.best_hand(hands[2])}")
    print(f"Identifies high card v2: {table.best_hand(hands[0]) > table.best_hand(hands[3])}")
    print(f"Identifies high card v2: {table.best_hand(hands[2]) > table.best_hand(hands[3])}")
    print(f"Identifies high card v3: {table.best_hand(hands[0]) < table.best_hand(hands[7])}")
    print(f"Identifies pair beats high card v1: {table.best_hand(hands[1]) > table.best_hand(hands[2])}")
    print(f"Identifies pair beats high card v2: {table.best_hand(hands[1]) > table.best_hand(hands[3])}")
    print(f"Identifies pair beats high card v3: {table.best_hand(hands[1]) > table.best_hand(hands[7])}")
    print(f"Identifies pair beats high card v4: {table.best_hand(hands[5]) > table.best_hand(hands[2])}")
    print(f"Identifies pair beats high card v5: {table.best_hand(hands[5]) > table.best_hand(hands[3])}")
    print(f"Identifies pair beats high card v6: {table.best_hand(hands[6]) > table.best_hand(hands[7])}")
    print(f"Identifies better pair: {table.best_hand(hands[1]) > table.best_hand(hands[5])}")
    print(f"Identifies three of a kind beats pair: {table.best_hand(hands[4]) > table.best_hand(hands[6])}")
    print(f"Identifies better three of a kind: {table.best_hand(hands[4]) < table.best_hand(hands[9])}")
    print(f"Identifies four of a kind beats three of a kind: {table.best_hand(hands[8]) > table.best_hand(hands[9])}")

