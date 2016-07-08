class Player:
    def __init__(self):
        self.hand = []
        self.inPlay = []

    def setHand(self, hand):
        self.hand = hand

    def drawTiles(self, tiles):
        self.hand += tiles

    def playTile(self, tile):
        if tile not in self.hand:
            return False
        self.hand.remove(tile)
        self.inPlay.append(tile)
        return True

    def submitPlay(self):
        self.inPlay = []

    def undo(self):
        self.hand.append(self.inPlay.pop())

    def displayHand(self, pygame, WINDOW, startPos):
        for i in range(len(self.hand)):
            tile = self.hand[i].tile
            WINDOW.blit(tile, (startPos[0]+tile.get_width()*i,
                               startPos[1]))


    def shuffleHand(self, pygame, WINDOW, startPos, tileWidth):
        import random
        import math
        newHand = self.hand.copy()
        random.shuffle(newHand)

        windowCopy = WINDOW.copy()

        radii = []
        for i1 in range(len(self.hand)):
            i2 = newHand.index(self.hand[i1])

            dist = i2 - i1
            radius = dist*tileWidth/2
            radii.append(radius)

        NUM_FRAMES = 30
        clock = pygame.time.Clock()
        clock.tick()
        x, y = startPos
        for i in range(NUM_FRAMES, -1, -1):
            WINDOW.blit(windowCopy, (0, 0))
            pygame.draw.rect(WINDOW, (0, 0, 0), (startPos[0], startPos[1], tileWidth*len(newHand), tileWidth))
            for j in range(len(newHand)):
                x1 = x + j*tileWidth
                y1 = y

                dx = radii[j] * math.cos(i*math.pi/NUM_FRAMES)
                dy = -radii[j] * math.sin(i*math.pi/NUM_FRAMES)
                if radii[j] < 0:
                    dy = -dy
                x2, y2 = x1+dx+radii[j], y1+dy
                WINDOW.blit(self.hand[j].tile, (x2, y2))
            pygame.display.update()
            clock.tick(60)
        self.hand = newHand
