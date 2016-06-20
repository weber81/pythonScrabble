import pygame, random

TILE_WIDTH = 40

_tileBase = pygame.image.load("tile.png");

pygame.font.init()
letterFont = pygame.font.SysFont("simsunnsimsun", 34)
numberFont = pygame.font.SysFont("bell", 12)

SCRABBLE_TILES = []

letterValueMap = {"A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2,
                  "H":4, "I":1, "J":8, "K":5, "L":1, "M":3, "N":1,
                  "O":1, "P":3, "Q":10, "R":1, "S":1, "T":1, "U":1,
                  "V":4, "W":4, "X":8, "Y":4, "Z":10, " ":0}

letterCountMap = {"A":9, "B":2, "C":2, "D":4, "E":12, "F":2, "G":3,
                  "H":2, "I":9, "J":1, "K":1, "L":4, "M":2, "N":6,
                  "O":8, "P":2, "Q":1, "R":6, "S":4, "T":6, "U":4,
                  "V":2, "W":2, "X":1, "Y":2, "Z":1, " ":2}

for i in range(26):
    copy = _tileBase.copy()
    l = chr(ord("A")+i)
    letter = letterFont.render(l, False, (0, 0, 0))
    number = numberFont.render(str(letterValueMap[l]), False, (0, 0, 0))
    size = letter.get_size()
    nSize = number.get_size()
    copy.blit(letter, (TILE_WIDTH/2-size[0]/2, TILE_WIDTH/2 - size[1]/2))
    copy.blit(number, (TILE_WIDTH-nSize[0]-2, TILE_WIDTH-nSize[1]))
    for i in range(letterCountMap[l]):
        SCRABBLE_TILES.append(copy.copy())

SCRABBLE_TILES.append(_tileBase.copy())
SCRABBLE_TILES.append(_tileBase.copy())
