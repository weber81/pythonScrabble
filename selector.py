import itertools, pygame

class Selector():
    STATES = ["horizontal", "vertical", "gone"]
    def __init__(self, pos=(0, 0), horizontal=True, visible=False):
        self.pos = pos
        self.state = 2
        self._stateCylcer = itertools.cycle([0, 1, 2])
        self.imageStates=[pygame.image.load("selector.png"),
                          pygame.transform.rotate(pygame.image.load("selector.png"), -90),
                          None]

    def getImage(self):
        return self.imageStates[self.state]

    def draw(self, WINDOW, tileToPixel=lambda x:x):
        if self.state != 2:
            WINDOW.blit(self.imageStates[self.state],
                    (tileToPixel(self.pos[0]), tileToPixel(self.pos[1])))

    def nextState(self):
        self.state = next(self._stateCycler)

    def getState(self):
        return self.state

    def getStateName(self):
        return STATES[self.state]

    def setPos(self, pos):
        if self.pos != pos:
            self.state = 2
            self._stateCycler = itertools.cycle([0, 1, 2])
            self.pos = pos
        
    def move(self):
        if self.state == 0:
            self.pos = self.pos[0]+1, self.pos[1]
        if self.state == 1:
            self.pos = self.pos[0], self.pos[1]+1

    def selected(self):
        return self.state != 2
