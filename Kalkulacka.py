# Vyytvoř kalkulačku  +- */ s tkinter
import tkinter as tk
from functools import partial


window = tk.Tk()
window.geometry("750x720")
window.title("Kalkulačka")

entry1 = tk.Entry(
    width=32,
    font=("Arial", 40),
    background="white",
    foreground="black"
)
entry1.grid(row=0, column=1, columnspan=4)

a = 0
r = 1
c = 1
num = ""
computer = ""

def calc(a):
    global num
    num = num + str(a)
    entry1.delete(0, tk.END)
    entry1.insert(0, num)

def answer():
    global num
    answer = eval(num)
    print(answer)
    entry1.delete(0, tk.END)
    entry1.insert(0, answer)

def reset():
    global num
    num = ""
    entry1.delete(0, tk.END)

while a in range(0,9):
    if a == 0:
        calca = partial(calc, "+")
        print("jj")
        buttona = tk.Button(
            text="+",
            bg="white",
            fg="black",
            width=20,
            height=10,
            command=calca,
        )
        buttona.grid(row=1, column=4)

    a += 1
    calca = partial(calc, a)

    buttona = tk.Button(
        text=a,
        background="black",
        fg="black",
        width=20,
        height=10,
        command=calca,
    )
    buttona.grid(row=r, column=c)
    if a >= 3:
        r=2
    if a >= 6:
        r=3
    if a == 3:
        calca = partial(calc, "-")
        buttona = tk.Button(
            text="-",
            bg="white",
            fg="black",
            width=20,
            height=10,
            command=calca,
        )
        buttona.grid(row=r, column=c+1)
        c=0
    elif a == 6:
        calca = partial(calc, "*")
        buttona = tk.Button(
            text="*",
            bg="white",
            fg="black",
            width=20,
            height=10,
            command=calca,
        )
        buttona.grid(row=r, column=c+1)
        c=0
    c += 1

a=0
calca = partial(calc, a)

button0 = tk.Button(
    text="0",
    bg="white",
    fg="black",
    width=20,
    height=10,
    command=calca,
)
button0.grid(row=4, column=1)

buttonReady = tk.Button(
    text="Vypocitat",
    bg="white",
    fg="black",
    width=20,
    height=10,
    command=answer,
)
buttonReady.grid(row=4, column=2)

buttonDelete = tk.Button(
    text="Vymazat",
    bg="white",
    fg="black",
    width=20,
    height=10,
    command=reset,
)
buttonDelete.grid(row=4, column=3)

calca = partial(calc, "/")
buttonDivide = tk.Button(
    text="/",
    bg="white",
    fg="black",
    width=20,
    height=10,
    command=calca,
)
buttonDivide.grid(row=4, column=4)


window.mainloop()



