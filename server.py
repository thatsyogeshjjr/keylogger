import socket
import threading

SERVER = '192.168.29.131'
PORT = 8865
password = 'bad_password!@#PQWERD'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER,PORT))
s.listen(5)

client,addr = s.accept()

file_name = client.recv(1024).decode()
file_size = client.recv(1024).decode()

print(f'((({file_name}))) created.')

open(file_name,'w').close()
file = open(file_name, 'wb')
file_bytes = b''
done = False

while not done:
    data = client.recv(1024)
    if file_bytes[-13:] == b'<END OF FILE>':
        done = True
    else:
        file_bytes += data
        print('wait...')

file.write(file_bytes)
s.close()
client.close()
    

