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

    x = 6
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

    label = tk.Label(
        window,
        anchor="w",
        background="white",
        foreground="black",
        width=20,
        font=(20),
        text="Rodné číslo",
    )
    label.grid(column=1, columnspan=1, row=0, sticky="W")

    label = tk.Label(
        window,
        anchor="w",
        background="white",
        foreground="black",
        width=20,
        font=(20),
        text="Jméno",
    )
    label.grid(column=1, columnspan=1, row=1, sticky="W")

    label = tk.Label(
        window,
        anchor="w",
        background="white",
        foreground="black",
        width=20,
        font=(20),
        text="Příjmení",
    )
    label.grid(column=1, columnspan=1, row=2, sticky="W")

    label = tk.Label(
        window,
        anchor="w",
        background="white",
        foreground="black",
        width=20,
        font=(20),
        text="Email",
    )
    label.grid(column=1, columnspan=1, row=3, sticky="W")

    label = tk.Label(
        window,
        anchor="w",
        background="white",
        foreground="black",
        width=20,
        font=(20),
        text="Telefon",
    )
    label.grid(column=1, columnspan=1, row=4, sticky="W")

    entry0 = tk.StringVar()
    entry0 = tk.Entry(
        window,
    )
    entry0.grid(row=0, column=2, columnspan=1)

    entry1 = tk.StringVar()
    entry1 = tk.Entry(
        window,
    )
    entry1.grid(row=1, column=2, columnspan=1)

    entry2 = tk.StringVar()
    entry2 = tk.Entry(
        window,
    )
    entry2.grid(row=2, column=2, columnspan=1)

    entry3 = tk.StringVar()
    entry3 = tk.Entry(
        window,
    )
    entry3.grid(row=3, column=2, columnspan=1)


    entry4 = tk.StringVar()
    entry4 = tk.Entry(
        window,
    )
    entry4.grid(row=4, column=2, columnspan=1)

    createExec = partial(create, entry0, entry1, entry2, entry3, entry4, window)
    createButton = tk.Button(
        window,
        text="Přidat",
        command=createExec,
        width=40,
    )
    createButton.grid(row=5, column=1, columnspan=2)

    window.mainloop()

    for row in data:
        print(row)

    con.commit()
    con.close()

    return entry0, entry1, entry2, entry3, entry4, window

def create(entry0, entry1, entry2, entry3, entry4, window):
    entry0 = entry0.get()
    entry1 = entry1.get()
    entry2 = entry2.get()
    entry3 = entry3.get()
    entry4 = entry4.get()

    cur.execute(
        f"INSERT INTO persons "
        "(RodneCislo, Jmeno, Prijmeni, Email, Telefon) "
        "VALUES (" + str(entry0) + ", '" + str(entry1) + "', '" + str(entry2) + "', "
        "'" + str(entry3) + "', '" + str(entry4) + "');"
    "")
    con.commit()

    window.destroy()
    mainWindow()

def delete(data, windowUP):
    print("Tried to delete ID" + str(data[0]))
    cur.execute(
        f"DELETE FROM persons "
        "WHERE RodneCislo = " + str(data[0]) + ";"
    "")
    con.commit()
    windowUP.destroy()
    window.destroy()
    mainWindow()

def update(data, entry1, entry2, entry3, entry4, windowUP):
    entry1 = entry1.get()
    entry2 = entry2.get()
    entry3 = entry3.get()
    entry4 = entry4.get()

    execString = "UPDATE persons SET Jmeno ='" + str(entry1) + "', Prijmeni = '" + str(entry2) + "', " \
                "Email = '" + str(entry3) + "', Telefon = '" + str(entry4) + "' " \
                "WHERE RodneCislo = " + str(data[0]) + ";"
    print(execString)
    cur.execute(execString)
    con.commit()

    windowUP.destroy()
    window.destroy()
    mainWindow()

def newwin(data):
    #global windowUP

    data0, data1, data2, data3, data4 = data

    windowUP = tk.Tk()
    windowUP.geometry("580x80")
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

    delExec = partial(delete, data, windowUP)
    delButton = tk.Button(
        windowUP,
        text="Smazat",
        command=delExec,
        width=40,
    )
    delButton.grid(row=3, column=1, columnspan=2)

    upExec = partial(update, data, entry1, entry2, entry3, entry4, windowUP)
    upButton = tk.Button(
        windowUP,
        text="Upravit",
        command=upExec,
        width=40,
    )
    upButton.grid(row=3, column=3, columnspan=2)

    windowUP.mainloop()
    return entry1, entry2, entry3, entry4, windowUP


con = sqlite3.connect("example.db")
# na jaký soubor se připojujeme

cur = con.cursor()
# jakou DB používáme

cur.execute("CREATE TABLE IF NOT EXISTS persons ("
    "RodneCislo int primary key,"
    "Jmeno varchar(255),"
    "Prijmeni varchar(255),"
    "Email varchar(255),"
    "Telefon varchar(255)"
");")

mainWindow()