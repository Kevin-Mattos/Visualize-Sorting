import pygame, math, sys, random, time
from Node import Node

RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 200,200,200
GREEN = 0,255,0
BLUE = 0,0,255

blockSize = 15
margin = 5
fullSize = blockSize + margin
qtd = 35
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
        pygame.draw.rect(screen, WHITE, rect)
        #screen.blit(node.surf, node.pos)
    return board

def basicSort(vet, size):

    for i in range(size):
        for j in range(size):
            if(vet[i] < vet[j]):
                aux = vet[i].value
                vet[i].changeValue( vet[j].value, i, height, margin, blockSize)
                vet[j].changeValue(aux, j, height, margin, blockSize)
                vet[i].color = RED
                vet[j].color = GREEN
                drawBoard(vet, size)
    drawBoard(vet, size)

def insertionSort(vet, size):
    #orderedList = []
    for i in range(1, size):
        aux = vet[i].value
        j = i - 1
        while (j >= 0 and aux < vet[j].value):
            vet[j + 1].changeValue(vet[j].value, j+1, height, margin, blockSize)
            vet[i].color = BLUE
            vet[ j + 1].color = RED
            vet[j].color = GREEN
            j-=1
            drawBoard(vet, size)
        vet[j+1].changeValue(aux, j +1, height, margin, blockSize)

    drawBoard(vet, size)

    imp(vet)

def imp(vet):
    for i in range(qtd):
        print(vet[i].value)

def drawBoard(vet, size):
    screen.fill(BLACK)
    for i in range(size):       
        pygame.draw.rect(screen, vet[i].color , vet[i].surf)
        vet[i].color = WHITE
        #time.sleep(0.004)
    pygame.display.flip()
    time.sleep(0.06)

vet = initializeVet(qtd)
board = initializeBoard(vet)
pygame.display.flip()
time.sleep(1)


print("___________________________")
#basicSort(board, qtd)
insertionSort(board, qtd)

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