class Player:
    def __init__(self):
        self.hand = []
        self.inPlay = []

    def setHand(self, hand):
        self.hand = hand

    def giveTiles(self, tiles):
        self.hand += tiles

    def playTile(self, tile):
        if tile not in hand:
            return False
        self.hand.remove(tile)
        self.inPlay.append(tile)
        return True

    def submitPlay(self):
        self.inPlay = []

    def undo(self):
        self.hand.append(self.inPlay.pop())
