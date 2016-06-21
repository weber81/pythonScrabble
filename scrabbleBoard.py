import pygame, sys

TILE_WIDTH = 40

""" e -> empty
    t -> triple word
    w -> double word
    l -> triple letter
    d -> double letter
    s -> start"""

SELECTOR = pygame.image.load("selector.png")

board_data = [[None for i in range(15)] for j in range(15)]

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

def drawBoard(WINDOW, blankBoard, board=board_data):
    for y in range(len(blankBoard)):
        for x in range(len(blankBoard[y])):
            if board[x][y] == None:
                image = TILES[blankBoard[x][y]]
            else:
                image = board[x][y]
            WINDOW.blit(image, (TILE_WIDTH*x, TILE_WIDTH*y))

def drawSelector(WINDOW, pos, horizontal):
    if pos[0] < len(board_data) and pos[1] < len(board_data):
        WINDOW.blit(pygame.transform.rotate(SELECTOR, 0 if horizontal else -90), (TILE_WIDTH*pos[0], TILE_WIDTH*pos[1]))
