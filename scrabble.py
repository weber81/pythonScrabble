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

    board.drawBoard(WINDOW, board.getBlankBoard())
    SELECTOR = pygame.image.load("selector.png")
    SELECTOR.convert_alpha()
    WINDOW.blit(SELECTOR, (0, 0))

    hand = []
    boardData = board.board_data

    for i in range(7):
        value = random.choice(tiles.SCRABBLE_TILES)
        tiles.SCRABBLE_TILES.remove(value)
        hand.append(value)
    
    for i in range(len(tiles.SCRABBLE_TILES)):
        WINDOW.blit(tiles.SCRABBLE_TILES[i].tile, (TILE_WIDTH*(i%15), TILE_WIDTH*(i//15)))
        boardData[(i%15)][(i//15)] = tiles.SCRABBLE_TILES[i].tile

    startX = WINDOW.get_size()[0]/2 - len(hand)*TILE_WIDTH/2
    for i in range(len(hand)):
        tile = hand[i].tile
        WINDOW.blit(tile, (startX+TILE_WIDTH*i, TILE_WIDTH*15 + BOARD_BOTTOM_MARGIN))

    pygame.display.update()

    selectedPos = None
    selectedHorizontal = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selectedPos == (event.pos[0]//TILE_WIDTH, event.pos[1]//TILE_WIDTH):
                    selectedHorizontal = not selectedHorizontal
                    if selectedHorizontal == True:
                        board.drawBoard(WINDOW, board.getBlankBoard(), boardData)
                        pygame.display.update()
                        selectedPos = None
                        continue
                else:
                    selectedHorizontal = True
                selectedPos = (event.pos[0]//TILE_WIDTH, event.pos[1]//TILE_WIDTH)
                board.drawBoard(WINDOW, board.getBlankBoard(), boardData)
                board.drawSelector(WINDOW, selectedPos, selectedHorizontal)
                pygame.display.update()
            if event.type == pygame.KEYUP:
                if selectedPos and selectedPos[0] < 15 and selectedPos[1] < 15:
                    for card in hand:
                        if card.letter == chr(event.key).upper():
                            boardData[selectedPos[0]][selectedPos[1]] = card.tile
                            board.drawBoard(WINDOW, board.getBlankBoard(), boardData)
                            if selectedHorizontal:
                                selectedPos = (selectedPos[0] + 1, selectedPos[1])
                            else:
                                selectedPos = (selectedPos[0], selectedPos[1]+1)
                            board.drawSelector(WINDOW, selectedPos, selectedHorizontal)
                            pygame.display.update()
                            break
                
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
