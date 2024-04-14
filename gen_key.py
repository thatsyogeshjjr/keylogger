import rsa
from cryptography.fernet import Fernet

(public, private) = rsa.newkeys(512)

open("public.pem", "wb").write(public.save_pkcs1("PEM"))
open("./server/private.pem", "wb").write(private.save_pkcs1("PEM"))

# fernet keys
fernet_key = Fernet.generate_key()
open("fernet.key", 'wb').write(fernet_key)
