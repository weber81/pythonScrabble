import scrabbleBoard as board
import scrabbleTiles as tiles
import scrabblePlayer as player
import selector as Selector
import pygame, sys, random

TILE_WIDTH = board.TILE_WIDTH

BOARD_BOTTOM_MARGIN = 3
HAND_SIZE = 7

tileToPixel=lambda x: x*TILE_WIDTH
pixelToTile=lambda x: x//TILE_WIDTH

def main():
    pygame.init()

    selector = Selector.Selector()
    player1 = player.Player()

    WIDTH = tileToPixel(15)
    HEIGHT = tileToPixel(15) + TILE_WIDTH + BOARD_BOTTOM_MARGIN

    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    board.drawBoard(WINDOW)

    boardData = board.board_data

    for i in range(HAND_SIZE):
        value = random.choice(tiles.SCRABBLE_TILES)
        tiles.SCRABBLE_TILES.remove(value)
        player1.hand.append(value)
    
    for i in range(len(tiles.SCRABBLE_TILES)):
        WINDOW.blit(tiles.SCRABBLE_TILES[i].tile, (TILE_WIDTH*(i%15), TILE_WIDTH*(i//15)))
        boardData[(i%15)][(i//15)] = tiles.SCRABBLE_TILES[i].tile

    startX = WINDOW.get_size()[0]/2 - len(player1.hand)*TILE_WIDTH/2
    
    player1.displayHand(pygame, WINDOW, (startX, TILE_WIDTH*15+BOARD_BOTTOM_MARGIN))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pixelToTile(event.pos[0]), pixelToTile(event.pos[1])

                if (pos[0] < len(board.BLANK_BOARD)
                        and pos[1] < len(board.BLANK_BOARD)):
                    selector.setPos(pos)
                    selector.nextState()
                    
                board.drawBoard(WINDOW, boardData)
                selector.draw(WINDOW, tileToPixel)
                pygame.display.update()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F5:
                    player1.shuffleHand(pygame, WINDOW, (startX, TILE_WIDTH*15 + BOARD_BOTTOM_MARGIN), TILE_WIDTH)
                    continue

                if selector.selected() and selector.pos[0] < 15 and selector.pos[1] < 15:
                    for card in player1.hand:
                        if card.letter == chr(event.key).upper():
                            pos = selector.pos
                            boardData[pos[0]][pos[1]] = card.tile

                            board.drawBoard(WINDOW, boardData)
                            selector.move()
                            selector.draw(WINDOW, tileToPixel)

                            player1.playTile(card)
                            player1.displayHand(pygame, WINDOW, (startX, TILE_WIDTH*15+BOARD_BOTTOM_MARGIN))
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
