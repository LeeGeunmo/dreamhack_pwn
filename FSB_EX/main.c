#include <stdio.h>
#include <stdlib.h>

void shell(){
    system("/bin/sh");
}

int main(void){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    char buf[200];
    printf("%p\n", buf);
    read(0, buf, 200);
    printf(buf);
    return 0;
}
//gcc -no-pie -fstack-protector -o FSB_EX main.c