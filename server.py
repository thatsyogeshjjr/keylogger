import socket
import threading

SERVER = '192.168.29.131'
PORT = 8865
password = 'bad_password!@#PQWERD'
'''
Problem: we do not know the server ip address.
Though we can consider that we are on the same network of the victim to make it a bit easier
One option can be to scan all open systems on the network for our port. That's what we will do
'''




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER,PORT))
s.listen(5)

client,addr = s.accept()
client.send(b'hello world')

