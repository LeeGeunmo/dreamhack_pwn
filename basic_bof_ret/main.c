#include <stdio.h>
#include <stdlib.h>

void shell(void){
    system("/bin/sh");
}

int main(void){
    char buf[20];

    scanf("%s", buf);
    printf(buf);

    return 0;
}