#include <stdio.h>
#include <stdlib.h>

void shell(){
    system("/bin/sh");
}

int main(void){
    // setvbuf(stdin, 0, 2, 0);
    // setvbuf(stdout, 0, 2, 0);
    // printf("aa");
    char buf[50];

    read(0, buf, 200);
    printf(buf);
    read(0, buf, 200);

    return 0;
}
//gcc -fstack-protector -z execstack -no-pie -fno-pie -o canary_leak main.c
