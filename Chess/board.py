import pygame
from pygame.locals import *
import sys
from PIL import Image, ImageDraw, ImageFont

#img = Image.new('RGB',(80,80), color = (0,153,153))
#img.save('pil_brown.png')
#d = ImageDraw.Draw(img)

# this is going determine the
#location stored [xloc,yloc]
class piece:
    def __init__(self,name,color,location):
        self.name = name
        self.alive = True
        self.color = color
        self.location = location
        self.img ='pieces/'+color+name+'.png'

#going to make board 640x640 and have each space be 80x80
# array stored in form [yloc,xloc]
class chessBoard:
    def __init__(self):

        self.spaces = []
        for i in range(8):
            self.spaces.append([])
            for x in range(8):
                self.spaces[i].append(None)
        #self.image = boardImage
        self.spaces[0][0]  = (piece('rook','black',[0,0]))
        self.spaces[0][1]  = (piece('knight','black',[1*80,0]))
        self.spaces[0][2]  = (piece('bishop','black',[2*80,0]))
        self.spaces[0][3]  = (piece('king','black',[3*80,0]))
        self.spaces[0][4]  = (piece('queen','black',[4*80,0]))
        self.spaces[0][5]  = (piece('bishop','black',[5*80,0]))
        self.spaces[0][6]  = (piece('knight','black',[6*80,0]))
        self.spaces[0][7]  = (piece('rook','black',[7*80,0]))
        for i in range(8):
            self.spaces[1][i]  = (piece('pawn','black',[i*80,1*80]))
            self.spaces[6][i]  = (piece('pawn','white',[i*80,6*80]))
        self.spaces[7][0]  = (piece('rook','white',[0,7*80]))
        self.spaces[7][1]  = (piece('knight','white',[1*80,7*80]))
        self.spaces[7][2]  = (piece('bishop','white',[2*80,7*80]))
        self.spaces[7][3]  = (piece('queen','white',[3*80,7*80]))
        self.spaces[7][4]  = (piece('king','white',[4*80,7*80]))
        self.spaces[7][5]  = (piece('bishop','white',[5*80,7*80]))
        self.spaces[7][6]  = (piece('knight','white',[6*80,7*80]))
        self.spaces[7][7]  = (piece('rook','white',[7*80,7*80]))


if __name__ == "__main__":
    chess = Image.open("pieces/chessBoard.png")
    height,width = chess.size
    example = chessBoard()
    pygame.init()
    #sets size of pygame display
    screen = pygame.display.set_mode([height,width])
    #loads image in and converts to readable pygame surface
    theBoard = pygame.image.load("pieces/chessBoard.png").convert()
    # draws image to screen with TL being at (x,y)
    i=0
    clock = pygame.time.Clock()
    screen.blit(theBoard,(0,0))

    for c in range(len(example.spaces)):
        for r in range(len(example.spaces[0])):
            print(r,' ',c)
            try:
                print(example.spaces[r][c].img)
                print(example.spaces[r][c].name)

            except:
                print("none")
            if(example.spaces[r][c]!= None):
                screen.blit(pygame.image.load(example.spaces[r][c].img).convert(),(example.spaces[r][c].location[0],example.spaces[r][c].location[1]))
                pygame.display.flip()



    running = True
    #updates screen
    pygame.display.flip()
    clock = pygame.time.Clock()
    block = [int(height/8),int(width/8)]
    while running:

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
            if event.type ==pygame.MOUSEBUTTONDOWN and event.button ==1:
                mouse = pygame.mouse.get_pos()
                print("x",mouse[0],"y",mouse[1])
                for i in example.spaces:
                    for j in i:
                        if j!=None:
                            if(j.location[0]<mouse[0]<j.location[0]+80)and(j.location[1]<mouse[1]<j.location[1]+80):
                                print(j.img)
