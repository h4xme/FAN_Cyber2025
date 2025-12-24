from pwn import xor

with open("flag.mp4", "rb") as f:
    secret = f.read()

open("whatisthis.mp4", "wb").write(xor(secret, secret[:16]))