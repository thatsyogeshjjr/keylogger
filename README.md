# Keylogger

##### _An application to understand standard keyloggers and their functions_

![Python | Powered](https://www.python.org/static/community_logos/python-powered-w-100x40.png)

This tries to understand advanced set of keyloggers. By re-creating its functionality in parts.

## Features

- Note keystroke logs down into a key.log file
- Send those files to a local server (from server folder)
- encrypt the sent logs with a fernet key
- Encrypt the fernet keys with asymmetric encryption allowing only attacker to get access to logs
- A seperate file to generate public.pem, private.pem, and fernet.key for rsa and fernet encryption.

## Tech / Libraries

- [Sockets](https://pypi.org/project/sockets/) - Conversing between attacker and victim
- [Cryptography.fernet](https://cryptography.io/en/latest/fernet/) - Encryption of logs for transfer
- [Rsa](https://pypi.org/project/rsa/) - Asymmetrical encryption of fernet keys for secure exchange
- [os](https://docs.python.org/3/library/os.html) - Handle files e.g. delete old data
- [apscheduler.schedulers.blocking](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/blocking.html) - Schedule time tags on logs
- [keyboard](https://pypi.org/project/keyboard/) - Get keystroke data for logging
- [time](https://docs.python.org/3/library/time.html) - Get time tags for logging
- [threading](https://docs.python.org/3/library/threading.html#module-threading) - handle client and logging events in threads

## Installation

This requires [Python](python.org) to run.

1. Install the the required libraries.

```
pip install -r requirements.txt
```

2. Generate keys for data exfiltration.

```
python gen_key.py
```

3. Start the keylogger.

```
python app.py
```

4. Stop the keylogger and start the server for exfiltration.

```sh
cd server
python server.py
```

4. In a seperate terminal start the exfiltration socket.

```sh
python exfil_revconn.py
```
