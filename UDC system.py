import sqlite3
import re
import tkinter as tk
from functools import partial

emailValidator = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def mainWindow():

    window = tk.Tk()
    window.geometry("580x220")
    window.title("DB System")
    # window.configure(bg="black")

    data = cur.execute("SELECT * FROM persons;")

    x = 6
    for row in data:
        exec = partial(newwin, row, window)
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

    # createExec = partial(create, entry0, entry1, entry2, entry3, entry4, window)
    checkCascadeExec = partial(checkCascade, window, entry0, entry0, entry1, entry1, entry2, entry2, entry3, entry3, entry4, entry4)
    createButton = tk.Button(
        window,
        text="Přidat",
        command=checkCascadeExec,
        width=40,
)
    createButton.grid(row=5, column=1, columnspan=2)

    window.mainloop()

    for row in data:
        print(row)

    con.commit()
    con.close()

    return entry0, entry1, entry2, entry3, entry4, window


def newwin(data, window):
    data0, data1, data2, data3, data4 = data

    windowUP = tk.Tk()
    windowUP.geometry("780x80")
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

    delExec = partial(delete, data, windowUP, window)
    delButton = tk.Button(
        windowUP,
        text="Smazat",
        command=delExec,
        width=40,
    )
    delButton.grid(row=3, column=1, columnspan=2)

    upExec = partial(update, data, entry1, entry2, entry3, entry4, windowUP, window)
    #updateCascadeExec = partial(update, window, data, data, entry1, entry1, entry2, entry2, entry3, entry3, entry4, entry4)

    updateCascadeExec = partial(update, data, entry1, entry2, entry3, entry4, windowUP, window)

    upButton = tk.Button(
        windowUP,
        text="Upravit",
        command=updateCascadeExec,
        width=40,
    )
    upButton.grid(row=3, column=3, columnspan=2)

    windowUP.mainloop()
    return entry1, entry2, entry3, entry4, windowUP


def checkCascade(window, dataInput0, label0, dataInput1, label1, dataInput2, label2, dataInput3, label3, dataInput4, label4):
    birthID = birthIDCheck(dataInput0, label0)
    name = alphabetCheck(dataInput1, label1)
    surname = alphabetCheck(dataInput2, label2)
    email = emailCheck(dataInput3, label3)
    phone = phoneCheck(dataInput4, label4)

    print(birthID)
    print(name)
    print(surname)
    print(email)
    print(phone)

    if name and surname and email and phone and birthID:
        create(dataInput0, dataInput1, dataInput2, dataInput3, dataInput4, window)
        window.destroy()
        mainWindow()
        return True
        # create(dataInput0, dataInput1, dataInput2, dataInput3, dataInput4, window)


def alphabetCheck(dataInput, entryBox):
    dataInput = dataInput.get()

    if any(chr.isdigit() for chr in dataInput) == False and 0 < len(dataInput) < 255:
        entryBox.config(fg="black")
        return True
    else:
        entryBox.config(fg="red")

def emailCheck(dataInput, entryBox):
    dataInput = dataInput.get()

    if re.fullmatch(emailValidator, dataInput):
        entryBox.config(fg="black")
        return True
    else:
        entryBox.config(fg="red")

def phoneCheck(dataInput, entryBox):
    dataInput = dataInput.get()

    if dataInput.isnumeric() and len(dataInput) == 9:
        entryBox.config(fg="black")
        return True
    else:
        entryBox.config(fg="red")

def birthIDCheck(dataInput, entryBox):
    try:
        dataInput = dataInput.get()
    except:
        dataInput = str(dataInput)
        dataInput = str(dataInput[:7] + "/" + str(dataInput[7:]))
        dataInput = dataInput[1:-1]
        print(dataInput)

    if len(dataInput) == 11:
        if dataInput[0:6].isnumeric() and dataInput[6] == "/" and dataInput[7:12].isnumeric():
            d = dataInput
            left = int(d[0]) + int(d[2]) + int(d[4]) + int(d[7]) + int(d[9])
            right = int(d[1]) + int(d[3]) + int(d[5]) + int(d[8]) + + int(d[10])

            valid = [0, 11, -11]
            if left - right in valid and int(d[2:4]) <= 82:
                try:
                    entryBox.config(fg="black")
                    return True
                except:
                    return True
            else:
                print(int(d[2:4]))
                print(left)
                print(right)
                print("Nefunguje 2")
    else:
        print("Nefunguje 1")
        try:
            entryBox.config(fg="red")
        except:
            return False


def create(entry0, entry1, entry2, entry3, entry4, window):

    #checkCascade(window, entry0, entry0, entry1, entry1, entry2, entry2, entry3, entry3, entry4, entry4)

    entry0 = entry0.get()
    entry1 = entry1.get()
    entry2 = entry2.get()
    entry3 = entry3.get()
    entry4 = entry4.get()

    entry0 = str(entry0).replace("/", "")
    cur.execute(
        f"INSERT INTO persons "
        "(RodneCislo, Jmeno, Prijmeni, Email, Telefon) "
        "VALUES (" + str(entry0) + ", '" + str(entry1) + "', '" + str(entry2) + "', "
        "'" + str(entry3) + "', '" + str(
        entry4) + "');""")
    con.commit()

    window.destroy()
    mainWindow()


def delete(data, windowUP, window):
    print("Tried to delete ID" + str(data[0]))
    cur.execute(
        f"DELETE FROM persons "
        "WHERE RodneCislo = " + str(data[0]) + ";"
                                               "")
    con.commit()
    windowUP.destroy()
    window.destroy()
    mainWindow()


def update(entry0, entry1, entry2, entry3, entry4, windowUP, window):

    entry0 = str(entry0)
    birthID = birthIDCheck(entry0, entry0)
    name = alphabetCheck(entry1, entry1)
    surname = alphabetCheck(entry2, entry2)
    email = emailCheck(entry3, entry3)
    phone = phoneCheck(entry4, entry4)

    print(birthID, name, surname, email, phone)

    entry1 = entry1.get()
    entry2 = entry2.get()
    entry3 = entry3.get()
    entry4 = entry4.get()

    if name and surname and email and phone and birthID:
        execString = "UPDATE persons SET Jmeno ='" + str(entry1) + "', Prijmeni = '" + str(entry2) + "', " \
                    "Email = '" + str(entry3) + "', Telefon = '" + str(entry4) + "' " \
                    "WHERE RodneCislo = " + str(entry0[1:-1]) + ";"
        print(execString)
        cur.execute(execString)
        con.commit()

        windowUP.destroy()
        window.destroy()
        mainWindow()


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
