import socket
import time

SERVER_ADDRESS = '127.0.0.1' , 54321


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

while True:
    with open("status.txt") as f:
        message = f.read()
        message_data = message.encode('utf8')
        client_socket(message_data)

    time.sleep(60)
