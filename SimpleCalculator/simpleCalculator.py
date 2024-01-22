import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Create a window
master = Tk()
p = PhotoImage(file = "CalculatorIcon.png") 
master.iconphoto(False, p) 

master.title("Calculator")
master.configure(background="#001011")

master.geometry("570x600")
master.resizable(False, False)

label_result = Label(master, width=25, height=2, bg="#DADAD9", text="", font=("arial", 30))
label_result.pack()

equation = ""
def clear():
    global equation
    label_result.config(text="", bg="#DADAD9")
    equation = ""


def show(val):
    global equation
    equation += str(val)
    label_result.config(text=equation)

def calculate():
    global equation
    try:
        str = eval(equation)
        label_result.config(text=str)
        equation = ""
    except:
        clear()
        label_result.config(text="Error !", font=("arial", 30, "bold"), bg="#F63E02")



Button(master, width=5, height=1, text="C", bd=1, fg="#F9FBF2", bg="#6CCFF6", font=("arial", 30, "bold"), command=lambda: clear()).place(x=10, y=100)
Button(master, width=5, height=1, text="/", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("/")).place(x=150, y=100)
Button(master, width=5, height=1, text="%", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("%")).place(x=290, y=100)
Button(master, width=5, height=1, text="*", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("*")).place(x=430, y=100)

Button(master, width=5, height=1, text="7", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("7")).place(x=10, y=200)
Button(master, width=5, height=1, text="8", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("8")).place(x=150, y=200)
Button(master, width=5, height=1, text="9", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("9")).place(x=290, y=200)
Button(master, width=5, height=1, text="-", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("-")).place(x=430, y=200)

Button(master, width=5, height=1, text="4", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("4")).place(x=10, y=300)
Button(master, width=5, height=1, text="5", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("5")).place(x=150, y=300)
Button(master, width=5, height=1, text="6", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("6")).place(x=290, y=300)
Button(master, width=5, height=1, text="+", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("+")).place(x=430, y=300)

Button(master, width=5, height=1, text="1", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("1")).place(x=10, y=400)
Button(master, width=5, height=1, text="2", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("2")).place(x=150, y=400)
Button(master, width=5, height=1, text="3", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show("3")).place(x=290, y=400)

Button(master, width=5, height=3, text="=", bd=1, fg="#F9FBF2", bg="#98CE00", font=("arial", 31, "bold"), command=lambda: calculate(), pady=3).place(x=430, y=400)

Button(master, width=11, height=1, text="0", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"),padx=2, command=lambda: show("0")).place(x=12, y=500)
Button(master, width=5, height=1, text=".", bd=1, fg="#F9FBF2", bg="#757780", font=("arial", 30, "bold"), command=lambda: show(".")).place(x=290, y=500)

master.mainloop()
