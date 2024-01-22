import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


master = Tk() 
icon_img = ImageTk.PhotoImage(Image.open("TicTacToeicon.jpeg"))
master.iconphoto(False, icon_img)
master.title("Tic Tac Toe")


turn = True
count = 0
win = False
#menu

menu = Menu(master)
master.config(menu=menu)
options = Menu(menu)
menu.add_cascade(label="Options", menu=options)
options.add_command(label="New Game", command=lambda: newGame())
options.add_command(label="Exit", command=lambda: master.quit())




def newGame():
    global turn, count, win
    turn = True
    count = 0
    win = False
    b1.config(text="")
    b2.config(text="")
    b3.config(text="")
    b4.config(text="")
    b5.config(text="")
    b6.config(text="")
    b7.config(text="")
    b8.config(text="")
    b9.config(text="")
    b1.config(bg='SystemButtonFace')
    b2.config(bg='SystemButtonFace')
    b3.config(bg='SystemButtonFace')
    b4.config(bg='SystemButtonFace')
    b5.config(bg='SystemButtonFace')
    b6.config(bg='SystemButtonFace')
    b7.config(bg='SystemButtonFace')
    b8.config(bg='SystemButtonFace')
    b9.config(bg='SystemButtonFace')




def disableAllButtons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkIfWin():
    global win, count

    if (b1["text"] == 'X' or b1["text"] == 'O') and (b1["text"] == b2["text"] and b2["text"] == b3["text"]) and (count<=9):
        winner = b1["text"]
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif (b4["text"] == 'X' or b4["text"] == 'O') and b4["text"] == b5["text"] and b5["text"] == b8["text"] and count<=9:
        winner = b4["text"]
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif (b7["text"] == 'X' or b7["text"] == 'O') and b7["text"] == b8["text"] and b8["text"] == b9["text"] and count<=9:
        winner = b7["text"]
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif (b1["text"] == 'X' or b1["text"] == 'O') and b1["text"] == b4["text"] and b4["text"] == b7["text"] and count<=9:
        winner = b1["text"]
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif (b2["text"] == 'X' or b2["text"] == 'O') and b2["text"] == b5["text"] and b5["text"] == b8["text"] and count<=9:
        winner = b2["text"]
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif (b3["text"] == 'X' or b3["text"] == 'O') and b3["text"] == b6["text"] and b6["text"] == b9["text"] and count<=9:
        winner = b3["text"]
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif (b1["text"] == 'X' or b1["text"] == 'O') and b1["text"] == b5["text"] and b5["text"] == b9["text"] and count<=9:
        winner = b1["text"]
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif (b3["text"] == 'X' or b3["text"] == 'O') and b3["text"] == b5["text"] and b5["text"] == b7["text"] and count<=9:
        winner = b3["text"]
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        win = True
        messagebox.showinfo(title="Results", message=f"{winner} Wins")
        disableAllButtons()
    elif count == 9 and win == False:
        messagebox.showinfo(title="Results", message="It's a tie")

def buttonClicked(button):
    global turn, count
    if button["text"] == "":
        if turn:
            button["text"] = 'X'
            turn = False
            count += 1
            checkIfWin()
        else:
            button["text"] = 'O'
            turn = True
            count += 1
            checkIfWin()
    else:
        messagebox.showerror(title="ERROR", message="Click somewhere else...!")

b1 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b1), width=5, height=2)
b2 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b2), width=5, height=2)
b3 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b3), width=5, height=2)
b4 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b4), width=5, height=2)
b5 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b5), width=5, height=2)
b6 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b6), width=5, height=2)
b7 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b7), width=5, height=2)
b8 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b8), width=5, height=2)
b9 = Button(master, text="", font=("Arial", 30), command=lambda: buttonClicked(b9), width=5, height=2)

# Place buttons on the grid
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


mainloop() 
