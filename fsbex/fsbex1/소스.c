#include <stdio.h>

void shell(void) {
	system("/bin/sh");
}

int main(void) {
	char buf[0x100];
	read(0, buf, 0x100);
	printf(buf);
	exit(0);
}