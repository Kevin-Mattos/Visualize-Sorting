import pygame, math

class Node:
    def __init__(self, pos, fullSize, rect, value, height, margin, blockSize):
        self.value = value
        self.surf = rect#pygame.image.load('resources/blank.png').convert()
        self.color = 255, 255, 255
        self.fullsize = fullSize
        
        self.height = height
        self.margin = margin
        self.blockSize = blockSize

        self.fixedColor = False

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value

    def changeValue(self, value, i):
        self.value = value
        
        self.surf = pygame.Rect( i*(self.fullsize) + math.ceil(self.fullsize/2), self.height - self.margin - value , self.blockSize , self.blockSize + value )
        

    def changeColor(self, color, isFixed = False):
        if(not self.fixedColor):
            self.color = color  

    def getPos(self, pos, fullSize):
        linha = math.floor((pos[0] - fullSize/2)/fullSize)
        coluna = math.floor((pos[1] - fullSize/2)/fullSize)    
        return coluna, linha 
