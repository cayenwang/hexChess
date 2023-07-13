import pygame

screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth,screenHeight))

origin = (screenWidth / 2, screenHeight / 2)

'''
==================================================
Board Set Up
==================================================
'''

tileWidth = 10
tileHeight = 0.866 * tileWidth * 2

hexPoints = [ # corners of the hex tile relative to the centre of the hex tile
    [tileWidth, tileHeight],
    [2 * tileWidth, 0],
    [tileWidth, -tileHeight],
    [-tileWidth, -tileHeight],
    [-2 * tileWidth, 0],
    [-tileWidth, tileHeight]
]

# create a basis to traverse the board
basis1 = [3 * tileWidth, -tileHeight] # along letter axis
basis2 = [0, 2 * tileHeight] # along number axis

''' Board Coordinates
      a b c d e f g h i j k
11              x x x x x x
10            x x x x x x x
9           x x x x x x x x
8         x x x x x x x x x
7       x x x x x x x x x x
6     x x x x x x x x x x x
5     x x x x x x x x x x
4     x x x x x x x x x
3     x x x x x x x x
2     x x x x x x x
1     x x x x x x
'''

'''
==================================================
Classes
==================================================
'''

class tile:
    def __init__(self, position, colour):
        self.colour = colour

        # Find centre of tile
        self.position = position
        xCoord = int(ord(position[0]) - 97) - 5
        yCoord = int(position[1:]) - 6

        xVector = [xCoord * i for i in basis1]
        yVector = [yCoord * i for i in basis2]

        self.centre = [xVector[0] + yVector[0] + origin[0], xVector[1] + yVector[1] + origin[1]]

        # Find corners
        self.points = []

        for i in range(6):
            corner = (self.centre[0] + hexPoints[i][0], self.centre[1] + hexPoints[i][1])
            self.points.append(corner)

        # Draw tile
        pygame.draw.polygon(screen, self.colour, self.points)

class board:
    def __init__(self):

        self.tiles = []

        for i in range(11): # letters
            letterCoordinate = chr(i+97)

            minJ = max(0, i-5)
            maxJ = min(11, i+6)

            for j in range(minJ, maxJ): # numbers

                position = letterCoordinate + str(j+1)

                coordinateSum = (i + j) % 3
                coordinateSumToColour = {
                    0: (210,140,69),
                    1: (233,173,112),
                    2: (255,207,159)
                }
                colour = coordinateSumToColour[coordinateSum]

                self.tiles.append(tile(position, colour))
