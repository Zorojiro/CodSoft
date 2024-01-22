from tkinter import Tk, Label, Button, Menu
from PIL import Image, ImageTk
import random

master = Tk()
master.configure(background='white')
master.title("Rock Paper Scissors")
icon_img = ImageTk.PhotoImage(Image.open("icon.jpeg"))
master.iconphoto(False, icon_img)

titleLabel = Label(master, text="Rock Paper Scissors", font=("Arial", 30, "bold"), bg="black", fg="white")
titleLabel.grid(row=0, column=2)

menu = Menu(master)
master.config(menu=menu)
options = Menu(menu)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="New Game", command=lambda: newGame())
options.add_command(label="Exit", command=lambda: master.quit())

def newGame():
    userScore.config(text=0)
    compScore.config(text=0)
    msg.config(text="")

paper_user = ImageTk.PhotoImage(Image.open("paper_u.jpeg").resize((250, 250)))
rock_user = ImageTk.PhotoImage(Image.open("rock_u.jpeg").resize((250, 250)))
scissor_user = ImageTk.PhotoImage(Image.open("scissors_u.jpeg").resize((250, 250)))

scissor_comp = ImageTk.PhotoImage(Image.open("scissors.jpeg").resize((250, 250)))
paper_comp = ImageTk.PhotoImage(Image.open("paper.jpeg").resize((250, 250)))
rock_comp = ImageTk.PhotoImage(Image.open("rock.jpeg").resize((250, 250)))

user = Label(master, image=scissor_user)
comp = Label(master, image=scissor_comp)
comp.grid(row=1, column=0)
user.grid(row=1, column=4)

userName = Label(master, text="You", bg="white")
compName = Label(master, text="Computer", bg="white")
compName.grid(row=0, column=0)
userName.grid(row=0, column=4)

userScore = Label(master, text=0, font=100, bg="white")
compScore = Label(master, text=0, font=100, bg="white")
userScore.grid(row=1, column=3)
compScore.grid(row=1, column=1)

rock = Button(master, text="Rock", width=20, height=2, font=("arial", 10, "bold"), bg="red", fg="black", command=lambda: choice("rock"))
rock.grid(row=2, column=1)

paper = Button(master, text="Paper", width=20, height=2, font=("arial", 10, "bold"), bg="yellow", fg="black", command=lambda: choice("paper"))
paper.grid(row=2, column=2)

scissors = Button(master, text="Scissors", width=20, height=2, font=("arial", 10, "bold"), bg="green", fg="black", command=lambda: choice("scissors"))
scissors.grid(row=2, column=3)

choices = ["rock", "paper", "scissors"]

msg = Label(master, font=("arial", 20), bg="white")
msg.grid(row=1, column=2)


def updateWinner(text):
    msg['text'] = text


def updateScoreUser():
    score = int(userScore['text'])
    score += 1
    userScore["text"] = str(score)


def updateScoreComp():
    score = int(compScore['text'])
    score += 1
    compScore["text"] = str(score)


def winner(user_choice, comp_choice):
    if user_choice == "rock":
        if comp_choice == "rock":
            updateWinner("Tie")
        elif comp_choice == "paper":
            updateScoreComp()
            updateWinner("Computer wins!")
        else:
            updateScoreUser()
            updateWinner("You win!")

    elif user_choice == "paper":
        if comp_choice == "paper":
            updateWinner("Tie")
        elif comp_choice == "rock":
            updateScoreUser()
            updateWinner("You win!")
        else:
            updateScoreComp()
            updateWinner("Computer wins!")

    elif user_choice == "scissors":
        if comp_choice == "scissors":
            updateWinner("Tie")
        elif comp_choice == "rock":
            updateScoreComp()
            updateWinner("Computer wins!")
        else:
            updateScoreUser()
            updateWinner("You win!")


def choice(text):
    # comp_user
    comp_choice = choices[random.randint(0, 2)]

    if comp_choice == "rock":
        comp.config(image=rock_comp)
    elif comp_choice == "paper":
        comp.config(image=paper_comp)
    else:
        comp.config(image=scissor_comp)

    # user
    if text == "rock":
        user.config(image=rock_user)
    elif text == "paper":
        user.config(image=paper_user)
    else:
        user.config(image=scissor_user)

    winner(text, comp_choice)


master.mainloop()
