import pygame
from pygame.locals import *
import sys
from PIL import Image, ImageDraw, ImageFont
import copy

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
# array stored in form [yloc,xloc] ie height, width
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

def printBoard(b):
    x = 0
    for r in b.spaces:
        y = 0
        for c in r:
            if(c!=None):
                print(c.img," ",x," ",y)
            y+=1
        x+=1

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

    for r in range(len(example.spaces)):
        for c in range(len(example.spaces[0])):
            print(r,' ',c)
            try:
                print(example.spaces[r][c].img)
                print(example.spaces[r][c].name)

            except:
                print("none")
            if(example.spaces[r][c]!= None):
                screen.blit(pygame.image.load(example.spaces[r][c].img).convert(),(example.spaces[r][c].location[0]+10,example.spaces[r][c].location[1]+10))
                pygame.display.flip()
                #clock.tick(5)



    running = True
    pieceChose = None
    chosenPiece = None
    oneOp = True
    boardPieceOne = pygame.image.load("pieces/boardPiece.png").convert()
    boardPieceTwo = pygame.image.load("pieces/boardPieceTwo.png").convert()

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
                x,y,xin,yin = mouse[0],mouse[1],int(mouse[0]/80),int(mouse[1]/80)
                oneOp = True
                print("x",x,"y",y)
                print("xin",xin,"yin",yin)
                for i in example.spaces:
                    if(oneOp):
                        for j in i:
                            if chosenPiece != None:
                                print(chosenPiece.img)
                                #here I want to make it so that it moves to whatever spot was chosen
                                #if j ==None:
                                #whateva
                                #mouse = pygame.mouse.get_pos()
                                print("you want to move to", int(mouse[0]/80),' ',int(mouse[1]/80))
                                oldxloc,oldyloc,newxloc,newyloc = int(chosenPiece.location[0]/80),int(chosenPiece.location[1]/80),int(mouse[0]/80),int(mouse[1]/80)
                                screen.blit(pygame.image.load(chosenPiece.img).convert(),(newxloc*80+10,newyloc*80+10))
                                newPiece = piece(chosenPiece.name,chosenPiece.color,[newxloc*80,newyloc*80])
                                example.spaces[oldxloc][oldyloc] = None
                                example.spaces[newyloc][newxloc] = newPiece
                                print(newPiece.img,"should be in this shit idk why it aint")
                                print([newxloc,newyloc])


                                oneOp = False
                                chosenPiece = None
                                printBoard(example)
                                print(example.spaces[newyloc][newxloc].img,example.spaces[newyloc][newxloc].location)
                                break

                                #for i in example.spaces:
                                #    for j in i:


                            #else:
                            if j!=None and chosenPiece==None:
                                xloc,yloc,xlocbr,ylocbr = j.location[0],j.location[1],j.location[0]+80,j.location[1]+80

                                if(xloc<x<xlocbr)and(yloc<y<ylocbr):
                                    print("you clicked",xloc," ",yloc)
                                    print("you have selected: ",j.img,"make your move")
                                    if(yloc%160<80):
                                        if(xloc%160<80):

                                            chosenPiece = j
                                            screen.blit(boardPieceOne,(xloc,yloc))
                                            oneOp=False
                                            break
                                        else:
                                            chosenPiece = j
                                            screen.blit(boardPieceTwo,(xloc,yloc))
                                            oneOp=False
                                            break

                                    else:
                                        if(xloc%160<80):
                                            chosenPiece = j
                                            screen.blit(boardPieceTwo,(xloc,yloc))
                                            oneOp=False
                                            break
                                        else:
                                            chosenPiece = j
                                            screen.blit(boardPieceOne,(xloc,yloc))
                                            oneOp=False
                                            break
                    pygame.display.flip()
