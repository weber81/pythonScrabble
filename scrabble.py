import scrabbleBoard as board
import scrabbleTiles as tiles
import pygame, sys, random

TILE_WIDTH = board.TILE_WIDTH
SELECTOR = board.SELECTOR

BOARD_BOTTOM_MARGIN = 3

def main():
    pygame.init()

    WIDTH = TILE_WIDTH*15
    HEIGHT = TILE_WIDTH*15 + TILE_WIDTH + BOARD_BOTTOM_MARGIN

    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    board.drawBoard(WINDOW, board.getBlankBoard(), [])
    SELECTOR = pygame.image.load("selector.png")
    SELECTOR.convert_alpha()
    WINDOW.blit(SELECTOR, (0, 0))

    hand = []

    for i in range(7):
        value = random.choice(tiles.SCRABBLE_TILES)
        tiles.SCRABBLE_TILES.remove(value)
        hand.append(value)
    
    for i in range(len(tiles.SCRABBLE_TILES)):
        WINDOW.blit(tiles.SCRABBLE_TILES[i], (TILE_WIDTH*(i%15), TILE_WIDTH*(i//15)))

    for i in range(len(hand)):
        tile = hand[i]
        WINDOW.blit(tile, (WIDTH*(i)/len(hand), TILE_WIDTH*15 + BOARD_BOTTOM_MARGIN))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

"""def fontTest():
    pygame.init()
    WINDOW = pygame.display.set_mode((1920, 1080))

    fonts = pygame.font.get_fonts()
    index = 0
    for i in range(1080//40):
        size = 40
        while True:
            f = pygame.font.SysFont(fonts[i], size)
            s = f.size("M")
            if s[0] < 40 and s[1] < 40:
                WINDOW.blit(f.render(fonts[i] + " " + str(size), False, (25, 255, 255)), (0, 40*i))
                break
            size -= 1
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return"""
