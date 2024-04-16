from tkinter import *
from configparser import ConfigParser

config = ConfigParser()
config.read('config.cfg')

win = Tk()
win.geometry('380x200')

ip_addr = StringVar()
port = IntVar()


# def start_server():
#     import os
#     os.system('python ./server.py')


def save_data():
    config.set("SERVER", "IP", ip_addr.get())
    config.set("SERVER", "PORT", str(port.get()))
    with open('config.cfg', 'w') as configfile:
        config.write(configfile)


ip_addr.set(config['SERVER']['IP'])
port.set(int(config['SERVER']['PORT']))

fonts = {
    'title': 'Consolas 20',
    'para': 'Consolas 12',
    'button': 'Consolas 10'
}

Label(text=">Server Manager", font=fonts["title"]).place(y=12, x=14)
Label(text="IP Address", font=fonts["para"]).place(y=56, x=18)
Entry(textvariable=ip_addr, font=fonts["para"]).place(y=56, x=138)

Label(text="Port", font=fonts["para"]).place(y=86, x=18)
Entry(textvariable=port, font=fonts["para"]).place(y=86, x=138)

Button(text='Save Changes', font=fonts['button'],
       command=save_data).place(y=126, x=20)
# Button(text='Start Server', font=fonts['button'],
#        command=start_server).place(y=126, x=120)


win.mainloop()
