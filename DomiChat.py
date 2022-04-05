import tkinter as tk
import socket
import threading


def get_message():
    while True:
        try:
            msg = clientsocket.recv(1024).decode("utf8")
            zpravy.insert(tk.END, msg)
        except:
            break


def send_message(event=None):
    msg = my_msg.get()
    my_msg.set("")
    clientsocket.send(bytes(msg, "utf8"))
    if msg == "quit!":
        clientsocket.close()
        window.quit()


def on_closing(event=None):
    my_msg.set("quit!")
    send_message()


window = tk.Tk()
window.title("chat")
messages_frame = tk.Frame(window)
my_msg = tk.StringVar()

zpravy = tk.Listbox(
    height=15, width=50
)
zpravy.pack()

vstup = tk.Entry(
    window,
    textvariable=my_msg
)
vstup.bind("<Return>", send_message)
vstup.pack()

odeslat = tk.Button(
    window,
    text="Send",
    command=send_message
)
odeslat.pack()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "DST22802"
port = 30004
clientsocket.connect((host, port))

x = threading.Thread(target=get_message)
x.start()
tk.mainloop()