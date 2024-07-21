import socket
import sqlite3
import threading
from datetime import datetime

SERVER_ADDRESS = '127.0.0.1' , 54321


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen(16)
print("server is listening...")



def client_handle(client_conn, client_addr):
    try:
        print("new client connected: {}: {}" .format(*client_adrr))
        
        while True:
            client_data = client_conn.recv(1024)
            if not client_data:
                 break
            
            client_mssg = client_data.decode('utf-8')        
            print('received: "{}"'.format(client_mssg))
            

            response = file_handle(client_mssg)
            client_conn.send(response.encode('utf-8'))
    
    except Exception as e:
        print("error with the client{}" .format(client_addr, e))
    
    finally:
        client_conn.close()


def file_handle(client_mssg):
    try:
        station_id, alarm1, alarm2 = map(int, client_mssg.split())
        
        alarm1_str = ""
        alarm2_str = ""

       
        if alarm1 not in (0, 1):
            alarm1_str = "Wrong value for alarm1"
        if alarm2 not in (0, 1):
            alarm2_str = "Wrong value for alarm2"
        if alarm1_str or alarm2_str:
            return alarm1_str + "\n" + alarm2_str 

        return sqlite3_handle(station_id, alarm1, alarm2)
    except ValueError:
        return "Please enter an integer"


def sqlite3_handle(station_id, alarm1, alarm2):
    try:
        conn = sqlite3.connect('water_station.sqlite3')
        cur = conn.cursor()
        last_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS station_status (
                        station_id INT,
                        last_date TEXT,
                        alarm1 INT,
                        alarm2 INT,
                        PRIMARY KEY(station_id) );
                        ''')
        cur.execute('''INSERT OR REPLACE INTO station_status (station_id, last_date, alarm1, alarm2)
                    VALUES (?, ?, ?, ?);''', (station_id, last_date, alarm1, alarm2))
        conn.commit()

    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        conn.close()
        return "Values inserted to the table"
    
     
try:
    while True:
        client_conn, client_adrr = server.accept()
        client_threading = threading.Thread(target = client_handle, args = (client_conn, client_adrr))
        client_threading.start()
except KeyboardInterrupt:
    print("\nserver shutting down")
finally:
    server.close()