import pygame, math, sys, random, time
from Node import Node

RED = 255, 0, 0
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 200,200,200
GREEN = 0,255,0
BLUE = 0,0,255
PURPLE = 128, 0, 128   

blockSize = 17
margin = 5
fullSize = blockSize + margin
qtd = 25
width, height = qtd*(fullSize), 3 * (fullSize)

size = width + blockSize, height + blockSize 
pygame.init()

screen = pygame.display.set_mode(size)
screen.fill(BLACK)

def checkIfQuit():
    ev = pygame.event.get()
    for event in ev: 

        #print(event)  
        if(event.type == pygame.QUIT):
            print('(x) clicked')
            closeWindow()

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_q):
                print('q pressed, closing')
                closeWindow()

def closeWindow():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def initializeVet(qtd):
    vet = []
    for i in range(qtd):
        vet.append(random.randint(0,qtd))
    return vet
    
def initializeBoard(vet):
    board = []
    i = 0
    for linha in range(math.floor(width/(fullSize))): 
        size = vet[i]
        i += 1       
        rect = pygame.Rect(linha*(fullSize) + math.ceil(fullSize/2), height - margin - size , blockSize , blockSize + size )
        node = Node((linha*fullSize, height-6), fullSize, rect, size, height, margin, blockSize)
        board.append(node)
        pygame.draw.rect(screen, WHITE, rect)
        #screen.blit(node.surf, node.pos)
    return board

def basicSort(vet):

    for i in range(len(vet)):
        for j in range(len(vet)):
            if(vet[i] < vet[j]):
                aux = vet[i].value
                vet[i].changeValue(vet[j].value, i)
                vet[j].changeValue(aux, j)
                vet[i].color = RED
                vet[j].color = GREEN
                drawBoard(vet)
    drawBoard(vet)

def quickSort(vet, p, r):
    if(p < r):
        j = separa(vet, p, r)
        quickSort(vet, p, j - 1)
        quickSort(vet, j + 1, r)
    #drawBoard(vet)


def separa(vet, p, r):
    c = vet[r]
    j = p
    print(r, p)
    #pNode = vet[p ]
    rNode = vet[int(r/2)]
    rNode.changeColor(RED)
    #pNode.changeColor(PURPLE)
    #pNode.fixedColor = True
    rNode.fixedColor = True
    for k in range(p, r):
        if(vet[k] <= c):
            t = vet[j].value
            vet[j].changeValue( vet[k].value, j)
            vet[k].changeValue( t, k)
            j+=1
            vet[k].changeColor(BLUE)#color = RED
            vet[j].changeColor(GREEN)#color = GREEN
            fixedNode = vet[r]
            fixedNode.color = GREY
            #fixedNode.fixedColor = True
            

            drawBoard(vet)
            #fixedNode.fixedColor = False
    t = vet[j].value
    vet[j].changeValue( vet[r].value, j)
    vet[r].changeValue( t, r)
    vet[j].color = GREEN
    #vet[r].color = RED
    #pNode.fixedColor = False
    rNode.fixedColor = False
    drawBoard(vet)
    #fixedNode.fixedColor = False
    return j



def insertionSort(vet):    
    for i in range(1, len(vet)):
        aux = vet[i].value
        j = i - 1
        while (j >= 0 and aux < vet[j].value):
            vet[j + 1].changeValue(vet[j].value, j+1)
            vet[i].color = BLUE
            vet[ j + 1].color = RED
            vet[j].color = GREEN
            j-=1
            drawBoard(vet)
        vet[j+1].changeValue(aux, j + 1)

    drawBoard(vet)

    imp(vet)

def bubbleSort(vet):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(len(vet) - 1):
            if(vet[i] > vet[i + 1]):
                aux = vet[i].value
                vet[i].changeValue(vet[i + 1].value, i)
                vet[i + 1].changeValue(aux, i + 1)
                vet[i].changeColor(RED)
                vet[i + 1].changeColor(GREEN)
                drawBoard(vet)
                swapped = True
        drawBoard(vet)
        



def imp(vet):
    for i in range(len(vet)):
        print(vet[i])

def drawBoard(vet, sleepTime = 0.06):
    screen.fill(BLACK)
    for i in range(len(vet)):       
        pygame.draw.rect(screen, vet[i].color , vet[i].surf)
        vet[i].changeColor(WHITE)
        #vet[i].color = WHITE
        #time.sleep(0.004)
    
    checkIfQuit()
    pygame.display.flip()
    time.sleep(sleepTime)

vet = initializeVet(qtd)
board = initializeBoard(vet)
pygame.display.flip()
time.sleep(1)


print('___________________________')
#basicSort(board)
#insertionSort(board)
#quickSort(board, 0, len(vet) - 1)
bubbleSort(board)

drawBoard(board)
imp(board)
while 1:    
# proceed events
    pygame.display.flip()
    checkIfQuit()
    

