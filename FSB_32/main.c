#include <stdio.h>
#include <stdlib.h>

void shell(){
    system("/bin/sh");
}

//int num = 10;

int main(void){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char buf[200];

    printf("%p\n", buf);
    read(0, buf, 200);
    printf(buf);
    //printf("\n%d", num);
    return 0;
}
//gcc -m32 -mpreferred-stack-boundary=2 -no-pie -fstack-protector -o FSB_32_shell main.c