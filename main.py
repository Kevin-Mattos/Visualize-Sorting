import pygame, math, sys, random
from Node import Node

RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 200,200,200
blockSize = 15
margin = 5
fullSize = blockSize + margin
qtd = 25
width, height = qtd*(fullSize), 3 * (fullSize)

size = width + blockSize, height + blockSize 
pygame.init()

screen = pygame.display.set_mode(size)
screen.fill(BLACK)
def initializeVet(qtd):
    vet = []
    for i in range(qtd):
        vet.append(random.randint(0,45))
    return vet
    
def initializeBoard(vet):
    board = []
    i = 0
    for linha in range(math.floor(width/(fullSize))): 
        size = vet[i]
        i += 1
        rect = pygame.Rect(linha*(fullSize) + math.ceil(fullSize/2), height - margin - size , blockSize , blockSize + size )
        node = Node((linha*fullSize, height-6), fullSize, rect, size)
        board.append(node)
        pygame.draw.rect(screen, RED, rect)
        #screen.blit(node.surf, node.pos)
    return board
vet = initializeVet(qtd)
initializeBoard(vet)

while 1:    
# proceed events
    pygame.display.flip()
    ev = pygame.event.get()
    
    for event in ev: 

        #print(event)       
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                print("arrow pressed, exiting game")
                pygame.display.quit()
                pygame.quit()
                sys.exit()