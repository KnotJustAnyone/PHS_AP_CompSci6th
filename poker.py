class player():
    def __init__(self):
        self.holecards = []
        self.communitycards = []
        self.handranking = 0
        self.bigblinds =1
        self.stack = 2
        self.BBstack = self.stack/self.bigblinds
        self.handlog = []
        # players individual strategies to determine action at each stage
        self.preflopstrategy = ""
        self.postflopstrategy = ""
        self.turnstrategy = ""
        self.riverstrategy = ""

    def rankhand(self):
        # ranks hand
        return None

    def gamestage(self):
        # determine stage of game, and route corresponding strategy
        self.handranking = self.rankhand()
        return None
