import pygame, math

class Node:
    def __init__(self, pos, fullSize, rect, value):
        self.value = value
        self.surf = rect#pygame.image.load('resources/blank.png').convert()
        self.pos = self.getPos(pos, fullSize)

    def writeOnImage(self, value, screen):
        self.value = value
        #self.surf = pygame.image.load('resources/{}.png'.format(value)).convert()
        screen.blit(self.surf, self.pos)

    def getPos(self, pos, fullSize):
        linha = math.floor((pos[0] - fullSize/2)/fullSize)
        coluna = math.floor((pos[1] - fullSize/2)/fullSize)    
        return coluna, linha 
