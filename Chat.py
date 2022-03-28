import tkinter as tk
import socket
import threading
import errno

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

#nastavit jméno => Grafické rozhrani pozdeji
my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#???????????? no.1

client_socket.connect((IP, PORT))
# Připojit na daný soket

client_socket.setblocking(False)
#???????????? no.1.5

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)
# Získej a odešli data na server

while True:
    #--------------------------------------------- Message input
    message = input(f'{my_username} > ')

    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        #--------------------------------------------- Vypiš zprávy
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print('Connection closed by the server')
                # --------------------------------------------- Předělat na logging
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            #--------------------------------------------- Vypiš zprávy
            print(f'{username} > {message}')

    except IOError as e:
        # --------------------------------------------- Předělat na logging -------------------------------------------
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()
        continue

    except Exception as e:
        print('Reading error: '.format(str(e)))
        sys.exit()


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

