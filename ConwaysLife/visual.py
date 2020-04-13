import pygame
import lifeSoup
import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#will create an image from the current state
def generateImage(width, height, array):
    data = np.zeros((height,width,3),dtype = np.uint8)
    white = [255,255,255]
    for r in range(len(array)):
        for c in range(len(array[0])):
            if(array[r][c] == 1):
                data[r*3][c*3] = white
                data[r*3+1][c*3] = white
                data[r*3+2][c*3] = white
                data[r*3][c*3+1] = white
                data[r*3][c*3+2] = white
                data[r*3+1][c*3+1] = white
                data[r*3+2][c*3+2] = white
                data[r*3+1][c*3+2] = white
                data[r*3+2][c*3+1] = white
    return data


#    will determine if the cell should live or die true is live false is die
#    corner cases are if width = 0,right bound and if height =0 or bottom bound
# x=0 y=0 x=0 y = rightbound x=
def liveOrDead(array,height, width):
    liveNeighbors = 0
    arrayWidth = len(array[0])
    arrayHeight = len(array)
    liveNeighbors += array[(height-1)%arrayHeight][(width-1)%arrayWidth]+array[(height-1)%arrayHeight][(width)%arrayWidth]+array[(height-1)%arrayHeight][(width+1)%arrayWidth]+array[(height)%arrayHeight][(width-1)%arrayWidth]+array[(height)%arrayHeight][(width+1)%arrayWidth]+array[(height+1)%arrayHeight][(width-1)%arrayWidth]+array[(height+1)%arrayHeight][(width)%arrayWidth]+array[(height+1)%arrayHeight][(width+1)%arrayWidth]
    if(array[height][width]==1):
        if(liveNeighbors==2 or liveNeighbors==3):
            return True
        else:
            return False
    else:
        if(liveNeighbors==3):
            return True
        else:
            return False

#will  update the current state
def updateCells(array):
    row = len(array)
    column = len(array[0])
    newArray = []
    for y in range(row):
        newArray.append([])
        for x in range(column):
            if(liveOrDead(array,y,x)):
                newArray[y].append(1)
            else:
                newArray[y].append(0)
    return newArray


if __name__ == "__main__":

    array = lifeSoup.generateSoup()
    y = 3*len(array)
    x = 3*len(array[0])
    pygame.init()
    GOLdisplay = pygame.display.set_mode([x,y])
    pygame.display.set_caption("Conway's game of life")
    # currentState.show() <-- this is a very very bad idea
    #currentState.save('gameState.png')
    #now = pygame.image.load(currentState)
    #GOLdisplay.blit(now,(0,0))
    #pygame.display.update()
    #time.sleep(.25)
    #image.save("gameState.png")
    iterations = 1000
    for l in range(iterations):
        currentState = Image.fromarray(generateImage(x,y,array),'RGB')
        #currentState.show() <-- bad idea
        #currentState.save('gameState.png')
        mode = currentState.mode
        size = currentState.size
        data = currentState.tobytes()
        now = pygame.image.fromstring(data,size,mode)
        now.convert()
        GOLdisplay.blit(now,(0,0))
        pygame.display.update()
        array = updateCells(array)
        #time.sleep(.1)
