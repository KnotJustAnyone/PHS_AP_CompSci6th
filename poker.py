from adityavpokerstrat import preflopstrategy, postflopstrategy, turnstrategy, riverstrategy
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
        # determine stage of game, and route corresponding strategy
        self.handranking = self.rankhand()
        return None
