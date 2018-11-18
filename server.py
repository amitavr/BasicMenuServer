"""
@author:
        Amit Avramovich
@Contact:
        amit.avramovich@gmail.com
@date:
        18-Nov-18
@Purpose:
         Server side for server that giving time, rand, name, exit.
         (final ver.)
@TODO:

"""
import socket
import datetime
import time
from random import randint

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 10000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        print('Check Log: ')
        data = ""
        while True:
            print("data = "+data)
            data = conn.recv(1024).decode()
            print("-> "+data)
            if(data.upper() == 'RAND'):
                random = str(randint(0, 9))
                conn.sendall(random.encode())
            elif(data.upper() == 'NAME'):
                conn.sendall(b"Server Name - Amit's server")
            elif(data.upper() == 'TIME'):
                localtime = time.localtime(time.time())
                time=str(datetime.datetime.now())
                conn.sendall(time.encode())
            elif (data.upper() == 'EXIT'):
                conn.close()
                s.close()
                break
            else:
                conn.sendall(b"Invalid command")
        print("session")

