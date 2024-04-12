import rsa
from cryptography.fernet import Fernet

public,private = rsa.newkeys(1024)

open("public.pem","wb").write(public.save_pkcs1("PEM"))
open("private.pem","wb").write(private.save_pkcs1("PEM"))

# fernet keys
fernet_key = Fernet.generate_key()
open("ferney.key", 'wb').write(fernet_key)