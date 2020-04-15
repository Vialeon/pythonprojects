from PIL import Image, ImageDraw, ImageFont
import numpy as np
def doThePieces():
    fnt = ImageFont.truetype('arial.ttf',15)

    while(True):
        piece = input("name please")
        if(piece == 'yeet'):
            break
        colour = input("color please")
        img = Image.new('RGB',(50,50), color = colour)
        d = ImageDraw.Draw(img)
        d.text((20,25),piece,fqnt=fnt, fill = (0,153,0))
        img.save(colour+piece+'.png')

def nowTheBoard():
    data = np.zeros((640,640,3),dtype = np.uint8)
    for r in range(len(data)):
        for c in range(len(data[0])):
            if(r%160<80):
                if(c%160<80):
                    data[r][c] = [255,153,51]
                else:
                    data[r][c] = [102,102,0]
            else:
                if(c%160<80):
                    data[r][c] = [102,102,0]
                else:
                    data[r][c] = [255,153,51]
    board = Image.fromarray(data)
    board.save("chessBoard.png")

if __name__ == "__main__":
    nowTheBoard()
