try:
    from adityavpokerstrat import preflopstrategy, postflopstrategy, turnstrategy, riverstrategy
except:
    print("Error importing from adityavpokerstrat, setting imports to None")
    preflopstrategy, postflopstrategy, turnstrategy, riverstrategy = None,None,None,None
try:    
    from treys import Card, Deck, Evaluator
except:
    print("Error importing from treys, setting imports to None")
    Card, Deck, Evaluator = None,None,None


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
            hand_value = Evaluator().evaluate(self.communitycards, self.holecards)
            hand_class = Evaluator().get_rank_class(hand_value)
            print(hand_value)
            print(Evaluator().class_to_string(hand_class))
            print("Game is currently river, hole cards are",Card.print_pretty_cards(self.holecards),"and community cards are",Card.print_pretty_cards(self.communitycards),".")
            print(self.BBstack)
            riverstrategy(self.BBstack,hand_value)
        # Misdeal
        elif (len(self.communitycards) > 0 and len(self.holecards) < 2):
            print("Error: Misdeal")
        else:
            print("Error")
        return None
Testcards = Deck().draw(2)
Communitycards = Deck().draw(5)
player1 = player(100000,500,Testcards,Communitycards)
player1.gamestage()
# player2 = player(50000,500,["As","Ks"],["Ac","Ad","Kh","7h"])
# player2.gamestage()
# player3 = player(2000,500,["As","Ks"],["Ac","Ad","Kh","7h","Ah"])
# player3.gamestage()
# Lucas = player(1000000,500,["7s","2c"],[])
# Lucas.gamestage()
# misdealtest = player(13,500,["2s"],["3h"])
# misdealtest.gamestage()
