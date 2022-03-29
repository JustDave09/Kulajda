import socket
import select
import threading
import logging

logging.basicConfig(filename='server.log', level=logging.DEBUG, filemode='a+', format='[%(asctime)s] %(levelname)s %(threadName)s %(name)s: %(message)s')
logging.info('-----------------------------------------------------------------')
logging.info('Starting server "The_Best_chatting_service_2022.jar"')
logging.info('-----------------------------------------------------------------')


HEADER_LENGTH = 1024

IP = "127.0.0.1"
PORT = 1234

logging.info('Creating server at ' + str(IP) + " on port" + str(PORT))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET - rodina sítě
# socket.SOCK_STREAM - TCP

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#???????????? no.1

server_socket.bind((IP, PORT))
# nabindovat server na socket který bude používat
# 0.0.0.0 oddposlouchává veškeré použitelné síte! :o
logging.info('Succesfully bound to socket')

server_socket.listen()
# server čeké na nové připojení

sockets_list = [server_socket]
#???????????? no.2

clients = {}

logging.info('Listening for connections on ' + str(IP) + ":" + str(PORT))
#-----------------------------------------------------------Předělat na logging

# Následující funkce spravuje příchozí zprávy
def receive_message(client_socket):
    while True:
        try:
            message_header = client_socket.recv(HEADER_LENGTH)
            # ???????????? no.3

            # Pokud nepřišla zpráva:
            if not len(message_header):
                return False

            message_length = int(message_header.decode('utf-8').strip())
            # ???????????? no.4

            return {'header': message_header, 'data': client_socket.recv(message_length)}
            # ???????????? Vrátí zprávu? no.4.5
        except:
            # Pokud skončilo připojení. . . Logging?
            return False

def server():
    while True:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
        # ???????????? no.5

        # Prohlíží příchozí připojení
        for notified_socket in read_sockets:

            # Pokud se jedná o nové připojení => Přijmi
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                # ???????????? no.6

                user = receive_message(client_socket)
                #Získej jméno uživatele (první zpráva)

                # Pokud se odpojí před odesláním jména:
                if user is False:
                    continue

                sockets_list.append(client_socket)
                # ???????????? no.7
                clients[client_socket] = user

                logging.info('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
                # -----------------------------------------------------------Předělat na logging
            # Pokud posílá zprávu:
            else:
                # Zpráva
                message = receive_message(notified_socket)

                # Pokud se odpojí:
                if message is False:
                    logging.info('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                    # -----------------------------------------------------------Předělat na logging
                    # Vymaž z listu připojených uživatelů
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue

                # Zjisti kdo píše zprávu:
                user = clients[notified_socket]

                logging.info(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
                # -----------------------------------------------------------Předělat na logging
                # Odešli zprávu všem připojeným:
                for client_socket in clients:
                    # Pokud se nejedná o odesílatele
                    #if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

x2 = threading.Thread(target=server)
x2.start()
"""
    #Příprava na pokročilejí logging
    for notified_socket in exception_sockets:

        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)

        # Remove from our list of users
        del clients[notified_socket]
"""