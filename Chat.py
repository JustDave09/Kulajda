import tkinter as tk
import socket
import threading

message = "Zatím nikdo nic nepíše :/"

def get_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 2205

    s.connect((host, port))
    msg = s.recv(1024)
    message = (msg.decode('ascii'))

    label1.configure(text=message)

    s.close()

def send_message():
    user_input = entry1.get()

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 2205

    serversocket.connect((host, port))

    clientsocket, addr = serversocket.accept()
    clientsocket.sendall(b"Pls")
    clientsocket.close()

#Tady začíná Grafické rozhraní chatu

window = tk.Tk()
window.geometry("750x720")
window.title("Chat")

label1 = tk.Label(
    text=message,
    background="black",
    foreground="white",
    font=("Arial", 20),
)
label1.grid(row=0, column=1, columnspan=4, sticky="W")

entry1 = tk.Entry(
    width=32,
    font=("Arial", 40),
    background="white",
    foreground="black"
)
entry1.grid(row=1, column=1, columnspan=4)

button1 = tk.Button(
    font=("Arial", 40),
    text="Odeslat",
    bg="white",
    fg="black",
    width=33,
    height=1,
    command=send_message,
)
button1.grid(row=2, column=1)

x = threading.Thread(target=get_message)
x.start()

window.mainloop()

