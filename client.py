import socket
import time

SERVER_ADDRESS = '127.0.0.1' , 54321
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def file_hundle():
    with open('status.txt', 'r') as f:
        try:
            station_number = int(f.readline())
            alarm1 = int(f.readline())
            alarm2 = int(f.readline())

            if alarm1 not in (0, 1):
                print("Wrong value for alarm 1")
                exit()
            if alarm2 not in (0, 1):
                print("Wrong value for alarm 2")
                exit()

            status = (str(station_number), str(alarm1), str(alarm2))

        except ValueError:
            print("Please enter an integer")
            exit()
        return status

try:
    client_socket.connect(SERVER_ADDRESS)
    print("connected to: {}" .format(SERVER_ADDRESS[0]))

    while True:
        status_list = file_hundle()
        status = ' '.join([str(elem) for elem in status_list])
        massege_data = status.encode('utf8') 
        client_socket.send(massege_data)



        response_data = client_socket.recv(1024)
        response_text = response_data.decode('utf-8')
        print("Response", response_text)
        time.sleep(10)


except ConnectionRefusedError:
    print("faild to connect to the server")
except KeyboardInterrupt:
    print("\nclient shutting down")
except Exception as e:
    print("An error occured: {}" .format(e))

finally:
    client_socket.close()
   


    
    
    
    
    