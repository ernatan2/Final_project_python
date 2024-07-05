import socket
import sqlite3
import time


#creating the connection with sqlite3 and creating the table

with sqlite3.connect('water_station.sqlite3') as conn:
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS station_status (
                        station_id INT,
                        last_date TEXT,
                        alarm1 INT,
                        alarm2 INT,
                        PRIMARY KEY(station_id) ); 
                ''')


#creating the server connection

SERVER_ADDRESS = '127.0.0.1' , 54321

accept_socket = socket.socket()
accept_socket.bind(SERVER_ADDRESS)
accept_socket.listen(20)

print("server is listening...")

while True:


    