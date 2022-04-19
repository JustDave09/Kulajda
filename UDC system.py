import sqlite3
import tkinter as tk
from functools import partial


def mainWindow():
    global window

    window = tk.Tk()
    window.geometry("580x220")
    window.title("DB System")
    # window.configure(bg="black")

    data = cur.execute("SELECT * FROM persons;")

    x = 0
    for row in data:
        exec = partial(newwin, row)
        label1 = tk.Button(
            anchor="w",
            background="white",
            foreground="black",
            width=63,
            font=(20),
            text=row,
            command=exec,
        )
        label1.grid(row=x, column=1, columnspan=4, sticky="W")
        x += 1

    # cur.execute("DROP TABLE persons")
    window.mainloop()

    for row in data:
        print(row)

    con.commit()
    con.close()

def create(data):
    cur.execute(
        "INSERT INTO persons "
        "(RodneCislo, Jmeno, Prijmeni, Narozeni, Mesto) "
        "VALUES (data[1], data[2], data[3], data[4], data[5]);"
    "")
    con.commit()

def delete(data):
    cur.execute(
        "UPDATE persons "
        "SET (RodneCislo, Jmeno, Prijmeni, Narozeni, Mesto)"
        "VALUES (data[1], data[2], data[3], data[4], data[5])"
        "WHERE RodneCislo = data[1];"
    "")
    con.commit()

def update(data, entry1, entry2, entry3, entry4):
    entry1 = entry1.get()
    entry2 = entry2.get()
    entry3 = entry3.get()
    entry4 = entry4.get()

    data.append(entry1)
    data.append(entry2)
    data.append(entry3)
    data.append(entry4)
    print(data)

    execString = "UPDATE persons SET Jmeno ='" + str(data[1]) + "', Prijmeni = '" + str(data[2]) + "', " \
                "Narozeni = '" + str(data[3]) + "', Mesto = '" + str(data[4]) + "' " \
                "WHERE RodneCislo = " + str(data[0]) + ";"
    print(execString)
    cur.execute(execString)
    con.commit()

    windowUP.destroy()
    window.destroy()
    mainWindow()

def newwin(data):
    global windowUP

    data0, data1, data2, data3, data4 = data

    windowUP = tk.Tk()
    windowUP.geometry("580x220")
    windowUP.title("Update Me")
    labelUP = tk.Label(
        windowUP,
        anchor="w",
        background="white",
        foreground="black",
        width=63,
        font=(20),
        text=data,
    )
    labelUP.grid(column=1, columnspan=4, sticky="W")

    repeat = 0
    while repeat in range(0, 4):
        repeat += 1
        if repeat == 1:
            entry1 = tk.StringVar()
            entry1 = tk.Entry(
                windowUP,
            )
            entry1.grid(row=2, column=repeat, columnspan=1)
            entry1.insert(0, data1)
        elif repeat == 2:
            entry2 = tk.StringVar()
            entry2 = tk.Entry(
                windowUP,
            )
            entry2.grid(row=2, column=repeat, columnspan=1)
            entry2.insert(0, data2)
        elif repeat == 3:
            entry3 = tk.StringVar()
            entry3 = tk.Entry(
                windowUP,
            )
            entry3.grid(row=2, column=repeat, columnspan=1)
            entry3.insert(0, data3)
        elif repeat == 4:
            entry4 = tk.StringVar()
            entry4 = tk.Entry(
                windowUP,
            )
            entry4.grid(row=2, column=repeat, columnspan=1)
            entry4.insert(0, data4)

    data = []
    data.append(data0)
    print(data)

    delExec = partial(delete, data)
    delButton = tk.Button(
        windowUP,
        text="Smazat",
        command=delExec,
        width=40,
    )
    delButton.grid(row=3, column=1, columnspan=2)

    upExec = partial(update, data, entry1, entry2, entry3, entry4)
    upButton = tk.Button(
        windowUP,
        text="Upravit",
        command=upExec,
        width=40,
    )
    upButton.grid(row=3, column=3, columnspan=2)

    windowUP.mainloop()
    return entry1, entry2, entry3, entry4


con = sqlite3.connect("example.db")
# na jaký soubor se připojujeme

cur = con.cursor()
# jakou DB používáme

cur.execute("CREATE TABLE IF NOT EXISTS persons ("
    "RodneCislo int primary key,"
    "Jmeno varchar(255),"
    "Prijmeni varchar(255),"
    "Narozeni varchar(255),"
    "Mesto varchar(255)"
");")

mainWindow()