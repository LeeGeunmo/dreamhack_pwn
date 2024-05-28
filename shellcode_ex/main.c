#include <stdio.h>

int main(void){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    char buf[100];

    printf("%p", buf);
    read(0, buf, 200);

    return 0;
}