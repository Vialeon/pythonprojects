import random as rand
def makeSoupSymmetrical(y):
    soup = []
    for i in range(y):
        soup.append([])
        for j in range(y):
            soup[i].append(rand.randint(0,1))
            #print(soup)
    return soup

def makeSoup(x,y):
    soup = []
    for i in range((y)):
        soup.append([])
        for j in range(x):
            soup[i].append(rand.randint(0,1))
            #print(soup)
    return soup

def generateSoup():
    format = ""
    soup = []
    while(format!="xy" and format!="x"):
        format = input("Soup in format x by x or x by y? enter x or xy ")
        if(format != "x" and format !="xy"):
            print("please input a valid format")
        print(format)


    while(True):

        if(format == "xy"):
            try:
                width = int(input("Enter x(width): "))
                height = int(input("enter y(height): "))
                soup = makeSoup(width,height)
                break
            except:
                print("please enter a valid height and width")
        else:
            try:
                size = int(input("enter x by x size: "))
                soup = makeSoupSymmetrical(size)
                break
            except:
                print("please enter a valid number for the size")
    return soup

if __name__ == "__main__":
    generateSoup()
