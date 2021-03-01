# Import module
from tkinter import *
import tkinter

# Create object
root = Tk()

# Adjust size
root.geometry("900x600")
root.resizable(0,0)

# Create canvas___________________________________________________________________________________________________
canvas = Canvas( root, width = 800, height = 600)
canvas.pack(fill = "both", expand = True)

# Variable________________________________________________________________________________________________________
X = 50
Y = 40
array = []

# Function________________________________________________________________________________________________________

def easy(event):
    global X,Y,array
    # canvas.bind("<Button-1>", back)
    array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0],
                [0,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,0],
                [0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0],
                [0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0],
                [0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0],
                [0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0],
                [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0],
                [0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0],
                [0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0],
                [0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
                [0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0],
                [0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0],
                [0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0],
                [0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0],
                [0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0],
                [0,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,1,0],
                [0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    # x = open("3.txt", "r")
    # array2D = x.read()
    # print(array)
    # array2D = array.split(';')
    # for num1 in range(len(array2D)):
    #     array2D[num1] = array2D[num1].strip('\n')
    #     array[num1] = array2D[num1].split(',')
    #     for num2 in range(len(array[num1])):
    #         array[num1][num2] = int(array[num1][num2])
    # x.close()
    for index1 in range(len(array)):
        for index2 in range(len(array[index1])):
            if array[index1][index2] == 0:
                canvas.create_rectangle(X, Y, X+20, Y+20, outline="black", fill="black")
            X +=20
        Y += 20
        X = 50

def comeback(event):
    canvas.delete("easy")
    canvas.delete("medium")
    canvas.delete("defficult")
    canvas.delete("<-")
    graphic()

def setting(event):
    global bg
    bg = PhotoImage(file = "C:\\Users\\student\\Pictures\\d757e9a82c599ab4634ebc5f20dbc82f.gif")
    canvas.create_image( 0, 0, image = bg, anchor = "nw")
    canvas.create_text(515,450, text = "Scenario", fill="black", font="Times 30 italic bold", tags="Scenario")

def start(event):
    global bg
    bg = PhotoImage(file = "C:\\Users\\student\\Pictures\\d757e9a82c599ab4634ebc5f20dbc82f.gif")
    canvas.create_image( 0, 0, image = bg, anchor = "nw")
    canvas.create_rectangle(100, 250, 250, 330, outline="black", fill="white", tags="easy")
    canvas.create_text(170, 290, text = "Easy", fill="black", font="Times 27 italic bold", tags="easy")

    canvas.create_rectangle(320, 250, 470, 330, outline="black", fill="white", tags="medium")
    canvas.create_text(390, 290, text = "Medium", fill="black", font="Times 27 italic bold", tags="medium")

    canvas.create_rectangle(520, 250, 670, 330, outline="black", fill="white", tags="defficult")
    canvas.create_text(590, 290, text = "Defficult", fill="black", font="Times 27 italic bold", tags="defficult")

    canvas.create_text(50,130, text = "<-", fill="darkblue", font="Times 30 italic bold", tags="<-")

def back(event):
    canvas.delete("easy")
    canvas.delete("medium")
    canvas.delete("defficult")
    graphic()
    # canvas.create_rectangle(430, 220, 610, 280, fill="white", tags="Start")
    # canvas.create_text(515, 250, text = "Start", fill="black", font="Times 30 italic bold", tags="Start")

    # canvas.create_rectangle(430, 320, 610, 380, fill="white", tags="Setting")
    # canvas.create_text(515,350, text = "Setting", fill="black", font="Times 30 italic bold", tags="Setting")

    # canvas.create_rectangle(430, 420, 610, 480, fill="white", tags="Scenario")
    # canvas.create_text(515,450, text = "Scenario", fill="black", font="Times 30 italic bold", tags="Scenario")


# Display image____________________________________________________________________________________________________

bg = PhotoImage(file = "C:\\Users\\student\\Pictures\\d757e9a82c599ab4634ebc5f20dbc82f.gif")
canvas.create_image( 0, 0, image = bg, anchor = "nw")

def graphic():
    canvas.create_rectangle(430, 220, 610, 280, fill="white", tags="Start")
    canvas.create_text(515, 250, text = "Start", fill="black", font="Times 30 italic bold", tags="Start")
    canvas.tag_bind("Start", "<Button-1>", start)

    canvas.create_rectangle(430, 320, 610, 380, fill="white", tags="Setting")
    canvas.create_text(515,350, text = "Setting", fill="black", font="Times 30 italic bold", tags="Setting")

    canvas.create_rectangle(430, 420, 610, 480, fill="white", tags="Scenario")
    canvas.create_text(515,450, text = "Scenario", fill="black", font="Times 30 italic bold", tags="Scenario")


graphic()
canvas.tag_bind("<-", "<Button-1>", comeback)
canvas.tag_bind("Start", "<Button-1>", start)
canvas.tag_bind("Setting", "<Button-1>", setting)
canvas.tag_bind("easy", "<Button-1>", easy)

# Execute tkinter_____________________________________________________________________________________________________
root.mainloop()