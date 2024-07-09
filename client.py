import socket
import time

SERVER_ADDRESS = '127.0.0.1' , 54321
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    client_socket.connect(SERVER_ADDRESS)
    print("connected to: {}" .format(SERVER_ADDRESS[0]))

    while True:
        massage  = input("input message: ")
        massege_data = massage.encode('utf8')
        client_socket.send(massege_data)

        response_data = client_socket.recv(1024)
        response_text = response_data.decode('utf8')
        print("Response", response_text)


except ConnectionRefusedError:
    print("faild to connect to the server")
except KeyboardInterrupt:
    print("\nclient shutting down")
except Exception as e:
    print("An error occured: {}" .format(e))

finally:
    client_socket.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # with open("status.txt") as f:
        # message = f.read()
        # message_data = message.encode('utf8')
        # client_socket(message_data)

    #time.sleep(60)
