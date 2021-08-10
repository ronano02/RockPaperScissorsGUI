from tkinter import *
from PIL import ImageTk, Image
import random

# Defining gui
gui = Tk()
gui.title('Ronan\'s Rock, Paper, Scissors Game')
gui.geometry('600x600')
gui.resizable(0, 0)

# Frames
visualFrame = LabelFrame(gui, bg='black', width=600, height=200).grid(row=0, column=0, columnspan=3)
controlFrame = LabelFrame(gui, bg='bisque4', width=600, height=400).grid(row=1, column=0, columnspan=3)

# Assigning images
vsImg = ImageTk.PhotoImage(Image.open('RPS/vs.png'))
comImg = ImageTk.PhotoImage(Image.open('RPS/com.png'))
comRock = ImageTk.PhotoImage(Image.open('RPS/comRock.png'))
comPaper = ImageTk.PhotoImage(Image.open('RPS/comPaper.png'))
comScissors = ImageTk.PhotoImage(Image.open('RPS/comScissors.png'))
userImg = ImageTk.PhotoImage(Image.open('RPS/user.png'))
userRock = ImageTk.PhotoImage(Image.open('RPS/userRock.png'))
userPaper = ImageTk.PhotoImage(Image.open('RPS/userPaper.png'))
userScissors = ImageTk.PhotoImage(Image.open('RPS/userScissors.png'))
tieImg = ImageTk.PhotoImage(Image.open('RPS/tie.png'))
wonImg = ImageTk.PhotoImage(Image.open('RPS/won.png'))
lostImg = ImageTk.PhotoImage(Image.open('RPS/lost.png'))
rockB = ImageTk.PhotoImage(Image.open('RPS/rockB.png'))
paperB = ImageTk.PhotoImage(Image.open('RPS/paperB.png'))
scissorsB = ImageTk.PhotoImage(Image.open('RPS/scissorsB.png'))
exitB = ImageTk.PhotoImage(Image.open('RPS/exitB.png'))

# Global variables for scoreboard and options for computer to choose from when playing
userScore = 0
comScore = 0
options = [[comRock, 'Rock'], [comPaper, 'Paper'], [comScissors, 'Scissors']]


# Randomises computers input, displays user vs computer inputs, determines who wins and updates scoreboard
def play(img, userIn):
    global userScore, comScore
    comIn = random.choice(options)
    Label(visualFrame, image=img, borderwidth=0, highlightthickness=0).grid(row=0, column=0)
    Label(visualFrame, image=comIn[0], borderwidth=0, highlightthickness=0).grid(row=0, column=2)
    Label(visualFrame, image=vsImg, borderwidth=0, highlightthickness=0).grid(row=0, column=1)

    if userIn == comIn[1]:
        gui.after(1500, lambda: Label(visualFrame, image=tieImg, borderwidth=0, highlightthickness=0).grid(row=0, column=0, columnspan=3))
    elif (userIn == "Rock" and comIn[1] == "Scissors") or (userIn == "Scissors" and comIn[1] == "Paper") \
            or (userIn == "Paper" and comIn[1] == "Rock"):
        gui.after(1500, lambda: Label(visualFrame, image=wonImg, borderwidth=0, highlightthickness=0).grid(row=0, column=0, columnspan=3))
        userScore += 1
    else:
        gui.after(1500, lambda: Label(visualFrame, image=lostImg, borderwidth=0, highlightthickness=0).grid(row=0, column=0, columnspan=3))
        comScore += 1

    gui.after(1500, lambda: Label(visualFrame, text=str(userScore)+':'+str(comScore), bg='bisque4', width=10, font=('arial', 24, 'bold')).place(x=202, y=202))


# Start images display
user = Label(visualFrame, image=userImg, borderwidth=0, highlightthickness=0).grid(row=0, column=0)
versus = Label(visualFrame, image=vsImg, borderwidth=0, highlightthickness=0).grid(row=0, column=1)
com = Label(visualFrame, image=comImg, borderwidth=0, highlightthickness=0).grid(row=0, column=2)

# Buttons
rockButton = Button(controlFrame, image=rockB, borderwidth=0, highlightthickness=0, command=lambda: play(userRock, 'Rock'))
paperButton = Button(controlFrame, image=paperB, borderwidth=0, highlightthickness=0, command=lambda: play(userPaper, 'Paper'))
scissorsButton = Button(controlFrame, image=scissorsB, borderwidth=0, highlightthickness=0, command=lambda: play(userScissors, 'Scissors'))
exitButton = Button(controlFrame, image=exitB, borderwidth=0, highlightthickness=0, command=gui.quit)

# Positioning buttons on screen
scoreBoard = Label(visualFrame, text=str(userScore)+':'+str(comScore), bg='bisque4', width=10, font=('arial', 24, 'bold')).place(x=202, y=202)
rockButton.grid(row=1, column=0)
paperButton.grid(row=1, column=1)
scissorsButton.grid(row=1, column=2)
exitButton.place(x=235, y=550)


gui.mainloop()
