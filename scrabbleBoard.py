import pygame, sys

TILE_WIDTH = 40

""" e -> empty
    t -> triple word
    w -> double word
    l -> triple letter
    d -> double letter
    s -> start"""

SELECTOR = pygame.image.load("selector.png")

def getTiles():
    images = {}
    images.update({"e": pygame.image.load("empty.png")})
    images.update({"t": pygame.image.load("tws.png")})
    images.update({"w": pygame.image.load("dws.png")})
    images.update({"l": pygame.image.load("tls.png")})
    images.update({"d": pygame.image.load("dls.png")})
    images.update({"s": pygame.image.load("start.png")})
    images.update({"tile": pygame.image.load("tile.png")})
    return images

TILES = getTiles()

def getBlankBoard():
    upper = ["teedeeeteeedeet",
            "eweeeleeeleeewe",
            "eeweeededeeewee",
            "deeweeedeeeweed",
            "eeeeweeeeeweeee",
            "eleeeleeeleeele",
            "eedeeededeeedee"]
    
    return upper + ["teedeeeseeedeet"] + upper[::-1]

def drawBoard(WINDOW, blankBoard, letters):
    for y in range(len(blankBoard)):
        for x in range(len(blankBoard[y])):
            image = TILES[blankBoard[x][y]]
            WINDOW.blit(image, (TILE_WIDTH*x, TILE_WIDTH*y))
