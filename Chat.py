import tkinter as tk
import sys
import socket
import threading

def send_message(event=None):
    message = your_chat_message.get()
    entry1.delete(0, tk.END)
    label1.see(tk.END)

    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{1024}}".encode('utf-8')
        client_socket.send(message_header + message)

def get_message():
    while True:
        try:
            #--------------------------------------------- Vypiš zprávy
            while True:
                username_header = client_socket.recv(1024)
                if not len(username_header):
                    print('Připojení ukončeno')
                    sys.exit()

                username_length = int(username_header.decode('utf-8').strip())
                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(1024)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')

                #--------------------------------------------- Vypiš zprávy
                label1.insert(0, str(username) + ">" + str(message))

        except Exception as e:
            print('ERROR: '.format(str(e)))
            sys.exit()

def destroy():
    global name

    testname = str(name.get())

    if testname.isalpha():
        window.destroy()


IP = "127.0.0.1"
PORT = 1234

window = tk.Tk()
window.geometry("580x220")
window.title("Name")
window.configure(bg="black")


label1 = tk.Label(
    text="Zadejte jméno pouze z písmen (žádné znaky ani čísla)",
    background="black",
    foreground="#7bff00",
    width=63,
    font=(20),
)
label1.grid(row=0, column=1, columnspan=4, sticky="W")

name = tk.StringVar()
entry1 = tk.Entry(
    textvariable=name,
    width=23,
    font=("Arial", 34),
    background="black",
    foreground="white",
    highlightbackground="black",
)
entry1.grid(row=1, column=0, columnspan=4)


button1 = tk.Button(
    window,
    font=("Arial", 20),
    text="Odeslat",
    bg="white",
    highlightbackground="white",
    foreground="black",
    width=10,
    height=2,
    command=destroy,
)
button1.grid(row=1, column=4)


window.mainloop()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP, PORT))
# Připojit na daný soket

username = name.get()
username = str(username).encode('utf-8')
username_header = f"{len(username):<{1024}}".encode('utf-8')

client_socket.send(username_header + username)
# Získej a odešli data na server


#Tady začíná Grafické rozhraní chatu

window = tk.Tk()
window.geometry("580x220")
window.title("Chat")
window.configure(bg="black")

label1 = tk.Listbox(
    background="black",
    foreground="#7bff00",
    width=63,
    font=(20),
)
label1.grid(row=0, column=1, columnspan=4, sticky="W")

your_chat_message = tk.StringVar()
entry1 = tk.Entry(
    textvariable=your_chat_message,
    width=23,
    font=("Arial", 34),
    background="black",
    foreground="white",
    highlightbackground="black",
)
entry1.grid(row=1, column=0, columnspan=4)

button1 = tk.Button(
    window,
    font=("Arial", 20),
    text="Odeslat",
    bg="white",
    highlightbackground="white",
    foreground="black",
    width=10,
    height=2,
    command=send_message,
)
button1.grid(row=1, column=4)

window.bind('<Return>', send_message)

x = threading.Thread(target=get_message)
x.start()

window.mainloop()

