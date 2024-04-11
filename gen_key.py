import rsa

public,private = rsa.newkeys(1024)

open("public.pem","wb").write(public.save_pkcs1("PEM"))
open("private.pem","wb").write(private.save_pkcs1("PEM"))