import socket
import sqlite3
import time
import threading


#creating the connection with sqlite3 and creating the table

# with sqlite3.connect('water_station.sqlite3') as conn:
#     cur = conn.cursor()
#     cur.execute('''
#                 CREATE TABLE IF NOT EXISTS station_status (
#                         station_id INT,
#                         last_date TEXT,
#                         alarm1 INT,
#                         alarm2 INT,
#                         PRIMARY KEY(station_id) ); 
#                 ''')


#creating the server connection

SERVER_ADDRESS = '127.0.0.1' , 54321

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(16)

print("server is listening...")

def client_handle(client_conn, client_addr):
    try:
        print("new client connected: {}: {}" .format(*client_adrr))
        
        while True:
            client_data = client_conn.recv(1024) 

            if not client_data:
                break   

            print('received: "{}"'.format(client_data.decode('utf8')))

            response = "message ressived"

            client_conn.send(response.encode('utf8'))
    
    except Exception as e:
        print("error with the client{}" .format(client_addr, e))
    
    finally:
        client_conn.close()



try:
    while True:
        client_conn, client_adrr = server_socket.accept()
        client_threading = threading.Thread(target = client_handle, args = (client_conn, client_adrr))
        client_threading.start()
except KeyboardInterrupt:
    print("\nserver shutting down")
finally:
    server_socket.close()




    

    
