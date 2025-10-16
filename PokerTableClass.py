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
        bet = 0
        return bet #A number for the size of the bet



        
