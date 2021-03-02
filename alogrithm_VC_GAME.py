# Import module
from tkinter import *
import tkinter
import winsound

# Create object
root = Tk()

# Adjust size
root.geometry("1000x750")
# root.resizable(0,0)

# Create canvas___________________________________________________________________________________________________
canvas = Canvas( root, width = 800, height = 600)
canvas.pack(fill = "both", expand = True)

# Variable________________________________________________________________________________________________________
array = []

# Function________________________________________________________________________________________________________

def moveRight(event):
    global array
    X = 0
    Y = 50
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9:
                number.append(pig1)
                number.append(pig2)
    print(number)
    if array[number[0]][number[1]+1] == 1:
        array[number[0]][number[1]+1] = 9
        array[number[0]][number[1]] = 1
    for index1 in range(len(array)):
        for index2 in range(len(array[index1])):
            if array[index1][index2] == 0:
                canvas.create_image( X, Y, image = wall, anchor = "nw", tags="gp")
            elif array[index1][index2] == 9:
                canvas.create_image( X, Y, image = piggy, anchor = "nw", tags="pig")
            elif array[index1][index2] == 1:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
            elif array[index1][index2] == 8:
                canvas.create_image( X, Y, image = Exitway, anchor = "nw", tags="gp")
            X +=30
        Y += 30
        X = 0
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav", winsound.SND_FILENAME)
def moveLeft(event):
    global array
    # print(array)
    X = 0
    Y = 50
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9:
                number.append(pig1)
                number.append(pig2)
    print(number)
    if array[number[0]][number[1]-1] == 1:
        array[number[0]][number[1]-1] = 9
        array[number[0]][number[1]] = 1
    for index1 in range(len(array)):
        for index2 in range(len(array[index1])):
            if array[index1][index2] == 0:
                canvas.create_image( X, Y, image = wall, anchor = "nw", tags="gp")
            elif array[index1][index2] == 9:
                canvas.create_image( X, Y, image = piggy, anchor = "nw", tags="pig")
            elif array[index1][index2] == 1:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white",tags="gp")
            elif array[index1][index2] == 8:
                canvas.create_image( X, Y, image = Exitway, anchor = "nw", tags="gp")
            X +=30
        Y += 30
        X = 0
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)
def moveDown(event):
    global array
    # print(array)
    X = 0
    Y = 50
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9:
                number.append(pig1)
                number.append(pig2)
    print(number)
    if array[number[0]+1][number[1]] == 1:
        array[number[0]+1][number[1]] = 9
        array[number[0]][number[1]] = 1
    for index1 in range(len(array)):
        for index2 in range(len(array[index1])):
            if array[index1][index2] == 0:
                canvas.create_image( X, Y, image = wall, anchor = "nw", tags="gp")
            elif array[index1][index2] == 9:
                canvas.create_image( X, Y, image = piggy, anchor = "nw", tags="pig")
            elif array[index1][index2] == 1:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
            elif array[index1][index2] == 8:
                canvas.create_image( X, Y, image = Exitway, anchor = "nw", tags="gp")
            X +=30
        Y += 30
        X = 0
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)
def moveUp(event):
    global array
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)
    # print(array)
    X = 0
    Y = 50
    number = []
    for pig1 in range(len(array)):
        for pig2 in range(len(array[pig1])):
            if array[pig1][pig2] ==9:
                number.append(pig1)
                number.append(pig2)
    print(number)
    if array[number[0]-1][number[1]] == 1:
        array[number[0]-1][number[1]] = 9
        array[number[0]][number[1]] = 1
    for index1 in range(len(array)):
        for index2 in range(len(array[index1])):
            if array[index1][index2] == 0:
                canvas.create_image( X, Y, image = wall, anchor = "nw", tags="gp")
            elif array[index1][index2] == 9:
                canvas.create_image( X, Y, image = piggy, anchor = "nw", tags="pig")
            elif array[index1][index2] == 1:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
            elif array[index1][index2] == 8:
                canvas.create_image( X, Y, image = Exitway, anchor = "nw", tags="gp")
            X +=30
        Y += 30
        X = 0
def Exit(event):
    winsound.PlaySound("C:\\Users\\student\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)
    canvas.delete("exit")
    canvas.delete("farm")
    canvas.delete("gp")
    canvas.delete("pig")
    # start()

def drawing():
    global array, bgfarm
    canvas.create_image( 0, 0, image = bgfarm, anchor = "nw", tags="farm")
    number = []
    X = 0
    Y = 50
    for index1 in range(len(array)):
        for index2 in range(len(array[index1])):
            if array[index1][index2] == 0:
                canvas.create_image( X, Y, image = wall, anchor = "nw", tags="gp")
            elif array[index1][index2] == 9:
                canvas.create_image( X, Y, image = piggy, anchor = "nw", tags="pig")
            elif array[index1][index2] == 1:
                canvas.create_rectangle(X, Y, X+30, Y+30, fill="white", tags="gp")
            elif array[index1][index2] == 8:
                canvas.create_image( X, Y, image = Exitway, anchor = "nw", tags="gp")
            elif array[index1][index2] == 4:
                canvas.create_image( X, Y-7, image = Enemy, anchor = "nw", tags="gp")
                
            X +=30
        Y += 30
        X = 0
    canvas.create_rectangle(0, 0, 80, 40, outline="black", fill="orange", tags="exit")
    canvas.create_text(40, 20, text = "Back", fill="darkblue", font="consolas 15", tags="exit")

def easy(event):
    global array
    array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0],
                [0,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0],
                [0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,8],
                [0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0],
                [0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0],
                [0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0],
                [0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0],
                [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0],
                [0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0],
                [0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0],
                [0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                [0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
                [0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0],
                [0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,0],
                [0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0],
                [0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0],
                [0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0],
                [0,9,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    drawing()
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)

def medium(event):
    global array
    array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,9,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0],
            [0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0],
            [0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0],
            [0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0],
            [0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0],
            [0,1,1,1,1,1,4,1,1,1,1,0,1,0,1,1,4,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0],
            [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0],
            [0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,0],
            [0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0],
            [0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0],
            [0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,0],
            [0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,4,0,1,1,1,1,0,1,1,0,1,1,0],
            [0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
            [0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,8],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    drawing()
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)
    

def defficult(event):
    global array
    array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
            [0,9,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0],
            [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0],
            [0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0],
            [0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0],
            [0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0],
            [0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0],
            [0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0],
            [0,0,0,1,1,1,0,1,1,1,1,4,0,1,1,0,1,1,4,1,1,1,1,1,1,1,0,1,0,1,1,0],
            [0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0],
            [0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0],
            [0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
            [0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0],
            [0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,4,1,1,1,0,1,1,1,1,0,1,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],
            [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0]]
    drawing()
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)



def comeback(event):
    winsound.PlaySound("C:\\Users\\student\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)
    canvas.delete("easy")
    canvas.delete("medium")
    canvas.delete("defficult")
    canvas.delete("Back")
    graphic()


def setting(event):
    global bg
    canvas.create_rectangle(200, 150,800,650, outline="black", fill="white", tags="setting")
    canvas.create_rectangle(220, 170, 290, 220, fill="orange", outline="black", tags ="SetBack")
    canvas.create_text(255,195, text = "Back", fill="black", font="consolas 15 ", tags="SetBack")
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)


def SetBack(event):
    canvas.delete("setting")
    canvas.delete("SetBack")
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)


def Scenario(event):
    canvas.create_rectangle(200, 150,800,650, outline="black", fill="white", tags="Scenarios")
    canvas.create_text(500,250, text = "Follow by this scenario", fill="black", font="consolas 15", tags="Scenarios")
    canvas.create_text(500,300, text = "1. You need to find exit to win.", fill="black", font="consolas 15", tags="Scenarios")
    canvas.create_text(500,350, text = "2. If you can find exit you will win. .", fill="black", font="consolas 15", tags="Scenarios")
    canvas.create_text(500,400, text = "3. But if you cannot find you will lose.", fill="black", font="consolas 15", tags="Scenarios")
    canvas.create_text(500,450, text = "4. If enemies touch you will lose also", fill="black", font="consolas 15 ", tags="Scenarios")
    
    canvas.create_rectangle(220, 170, 290, 220, fill="orange", outline="black", tags ="ScenBack")
    canvas.create_text(255,195, text = "Back", fill="black", font="consolas 15 ", tags="ScenBack")
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)


def ScenBack(event):
    canvas.delete("ScenBack")
    canvas.delete("Scenarios")
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)

def start(event):
    global bgpig
    canvas.create_image( 0, 0, image = bgpig, anchor = "nw")
    canvas.create_rectangle(120, 430, 300, 510, outline="black", fill="white", tags="easy")
    canvas.create_text(210, 470, text = "Easy", fill="black", font="consolas 30", tags="easy")

    canvas.create_rectangle(400, 430, 580, 510, outline="black", fill="white", tags="medium")
    canvas.create_text(490, 470, text = "Medium", fill="black", font="consolas 30", tags="medium")

    canvas.create_rectangle(680, 430, 860, 510, outline="black", fill="white", tags="defficult")
    canvas.create_text(770, 470, text = "Defficult", fill="black", font="consolas 28 ", tags="defficult")

    canvas.create_rectangle(20, 110, 100, 150, outline="black", fill="orange", tags="Back")
    canvas.create_text(60,130, text = "Back", fill="darkblue", font="consolas 15", tags="Back")
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav",winsound.SND_FILENAME)

def back(event):
    winsound.PlaySound("C:\\Users\\student\\Desktop\\sophanna-VC_Game\\rockHit2.wav", winsound.SND_FILENAME)
    canvas.delete("easy")
    canvas.delete("medium")
    canvas.delete("defficult")
    graphic()
    

# Display image____________________________________________________________________________________________________

bg = PhotoImage(file = "C:\\Users\\student\\Desktop\\sophanna-VC_Game\\Images\\farmpig.gif")
bgpig = PhotoImage(file = "C:\\Users\\student\\Desktop\\sophanna-VC_Game\\Images\\three_pig.gif")
bgfarm = PhotoImage(file = "C:\\Users\\student\\Desktop\\sophanna-VC_Game\\Images\\backpig.gif")
wall = PhotoImage(file = "C:\\Users\\student\\Desktop\\sophanna-VC_Game\\Images\\brickBrown.png")
piggy = PhotoImage(file = "C:\\Users\\student\\Desktop\\sophanna-VC_Game\\Images\\piggy.gif")
Exitway = PhotoImage(file = "C:\\Users\\student\\Desktop\\sophanna-VC_Game\\Images\\signExits.png")
Enemy = PhotoImage(file = "C:\\Users\\student\\Desktop\\sophanna-VC_Game\\Images\\malePerson_walk0.png")


def graphic():
    canvas.create_image( 0, 0, image = bg, anchor = "nw")
    
    canvas.create_rectangle(430, 220, 610, 280, fill="white", tags="Start")
    canvas.create_text(515, 250, text = "Start", fill="black", font="consolas 30", tags="Start")
    canvas.tag_bind("Start", "<Button-1>", start)

    canvas.create_rectangle(430, 320, 610, 380, fill="white", tags="Setting")
    canvas.create_text(515,350, text = "Setting", fill="black", font="consolas 30", tags="Setting")

    canvas.create_rectangle(430, 420, 610, 480, fill="white", tags="Scenario")
    canvas.create_text(520,450, text = "Scenario", fill="black", font="consolas 30 ", tags="Scenario")




graphic()
canvas.tag_bind("Back", "<Button-1>", comeback)
canvas.tag_bind("exit", "<Button-1>", Exit)
canvas.tag_bind("Start", "<Button-1>", start)
canvas.tag_bind("Setting", "<Button-1>", setting)
canvas.tag_bind("Scenario", "<Button-1>", Scenario)
canvas.tag_bind("easy", "<Button-1>", easy)
canvas.tag_bind("medium", "<Button-1>", medium)
canvas.tag_bind("defficult", "<Button-1>", defficult)
canvas.tag_bind("ScenBack", "<Button-1>", ScenBack)
canvas.tag_bind("SetBack", "<Button-1>", SetBack)

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Down>", moveDown)
root.bind("<Up>", moveUp)

# Execute tkinter_____________________________________________________________________________________________________
root.mainloop()