import pygame, math

class Node:
    def __init__(self, pos, fullSize, rect, value):
        self.value = value
        self.surf = rect#pygame.image.load('resources/blank.png').convert()
        self.color = 255, 255, 255
        self.fullsize = fullSize

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return int(self.value)

    def changeValue(self, value, i, height, margin, blockSize):
        self.value = value
        
        self.surf = pygame.Rect( i*(self.fullsize) + math.ceil(self.fullsize/2), height - margin - value , blockSize , blockSize + value )
        
        

    def getPos(self, pos, fullSize):
        linha = math.floor((pos[0] - fullSize/2)/fullSize)
        coluna = math.floor((pos[1] - fullSize/2)/fullSize)    
        return coluna, linha 
