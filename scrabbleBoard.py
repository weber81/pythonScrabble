import pygame, sys

TILE_WIDTH = 40

""" e -> empty
    t -> triple word
    w -> double word
    l -> triple letter
    d -> double letter
    s -> start"""

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

BLANK_BOARD = getBlankBoard()
board_data = [[None for i in range(len(BLANK_BOARD[j]))] for j in range(len(BLANK_BOARD))]

def drawBoard(WINDOW, board=board_data):
    for y in range(len(BLANK_BOARD)):
        for x in range(len(BLANK_BOARD[y])):
            if board[x][y] == None:
                image = TILES[BLANK_BOARD[x][y]]
            else:
                image = board[x][y]
            WINDOW.blit(image, (TILE_WIDTH*x, TILE_WIDTH*y))

def clearData():
    global board_data
    board_data = [[None for i in range(len(BLANK_BOARD[j]))] for j in range(len(BLANK_BOARD))]
