#include <stdio.h>

char binsh[] = "/bin/sh";

int main(void){
    char buf[50];

    printf("BOF1\n");
    read(0, buf, 200);
    printf("%s\n", buf);
    printf("BOF2\n");
    read(0, buf, 200);

    return 0;
}
//gcc -fno-stack-protector -mpreferred-stack-boundary=4 -no-pie -fno-pie -o rtl_64 main_64.c