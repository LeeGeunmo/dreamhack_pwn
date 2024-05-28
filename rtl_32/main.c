#include <stdio.h>
#include <stdlib.h>

char binsh[] = "/bin/sh";

int main(void){
    char buf[50];
    printf("system addr: %p\n", &system);

    printf("BOF\n");
    read(0, buf, 200);

    return 0;
}