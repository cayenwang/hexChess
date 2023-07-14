#K Q R B N P
import pygame

import board

class piece:
    def __init__(self, screen, board, position, colour, type):
        self.screen = screen
        self.board = board
        self.position = position
        self.colour = colour
        self.type = type

        self.icon = pygame.image.load_extended("./pieces-png/" + self.colour + "-" + self.type + ".png")
        self.icon = pygame.transform.scale(self.icon, (board.tileHeight * 1.8, board.tileHeight * 1.8))
        self.rect = self.icon.get_rect()
        self.rect.center = eval("self.board.tiles['tile" + self.position + "'].centre")
        #self.rect.center = board.origin
        self.screen.blit(self.icon, self.rect)
        
class rook(piece):
    def __init__(self, screen, board, position, colour):
        super().__init__(screen, board, position, colour, "rook")

    # def validMoveSquares(self):
    #     self.position +- [1,0] # along constant number
    #     self.position +- [0,1] # along constant letter
    #     self.position +- [1,1] # 3rd direction
