from adityavpokerstrat import preflopstrategy, postflopstrategy, turnstrategy, riverstrategy
from treys import Card, Deck, Evaluator
class player():
    def __init__(self, stack, bigblinds, holecards, communitycards):
        self.holecards = holecards
        self.communitycards = communitycards
        self.handranking = 0
        self.bigblind = bigblinds
        self.stack = stack
        self.BBstack = self.stack/self.bigblind
        self.handlog = []

        # players individual strategies to determine action at each stage
        self.preflopstrategy = preflopstrategy
        self.postflopstrategy = postflopstrategy
        self.turnstrategy = turnstrategy
        self.riverstrategy = riverstrategy
    def rankhand(self):
        # ranks hand
        return None

def gamestage(self):
        # Preflop
        if (len(self.communitycards) == 0 and len(self.holecards) == 2):
            print("Game is currently preflop, hole cards are",Card.print_pretty_cards(self.holecards),".")
            print(self.BBstack)
        # Postflop
        elif (len(self.communitycards) == 3 and len(self.holecards) == 2):
            print("Game is currently postflop, hole cards are",Card.print_pretty_cards(self.holecards),"and community cards are",Card.print_pretty_cards(self.communitycards),".")
            print(self.BBstack)
        # Turn
        elif (len(self.communitycards) == 4 and len(self.holecards) == 2):
            print("Game is currently turn, hole cards are",Card.print_pretty_cards(self.holecards),"and community cards are",Card.print_pretty_cards(self.communitycards),".")
            print(self.BBstack)
        # River
        elif (len(self.communitycards) == 5 and len(self.holecards) == 2):
            print("Game is currently river, hole cards are",Card.print_pretty_cards(self.holecards),"and community cards are",Card.print_pretty_cards(self.communitycards),".")
            print(self.BBstack)
        elif (len(self.communitycards) > 0 and len(self.holecards) < 2):
            print("Error: Misdeal")
        else:
            print("Error")
