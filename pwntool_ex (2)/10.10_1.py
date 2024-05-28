from pwn import *

p = process('./pwntool_ex')

p.recvuntil("=")
rawa = p.recvuntil("\n")
a = int(rawa)
p.recvuntil("=")
rawb = p.recvuntil("\n")
b = int(rawb)
input = a*b
print(a)
print(b)
print(input)

p.sendline(str(input))

p.interactive()
