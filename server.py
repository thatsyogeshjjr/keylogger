import socket
import rsa
from cryptography.fernet import Fernet
import rsa

SERVER = '192.168.29.131'
PORT = 8865

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))
s.listen(5)

client, addr = s.accept()


def prep_key(enc_key):
    priv_key = rsa.PrivateKey.load_pkcs1(open('private.pem', 'rb').read())
    return Fernet(rsa.decrypt(enc_key, priv_key))


def decrypt_file(f_key, file):
    enc_logs = open(file).read()
    return f_key.decrypt(enc_logs)


file_name = client.recv(1024).decode()
file_size = client.recv(1024).decode()

with open(file_name, 'wb') as file:
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
