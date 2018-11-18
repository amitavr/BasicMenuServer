"""
@author:
        Amit Avramovich
@Contact:
        amit.avramovich@gmail.com
@date:
        18-Nov-18
@Purpose:
         Client side for server that giving time, rand, name, exit.
         (final ver.)
"""
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address) # CONNECTION OCCOURD
sock.connect(server_address)

try:
    sent_message=''
    while sent_message.upper() != 'EXIT':
        sent_message = input('Input: ')
        if len(sent_message) != 0: # In case input isn't empty
            sock.sendall(sent_message.encode())
            recv_message = sock.recv(1024).decode()
            print(recv_message )
            #print("sent = " + sent_message )
        else:
            print("Invalid input!")
    print("EXIT occourd")

finally:
    print('closing socket')
    sock.close()
