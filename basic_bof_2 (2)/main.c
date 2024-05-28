#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main(void){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    srand((unsigned)time(NULL));

    int random = rand() % 899999 + 100001;
    char buf[50];
    int i = 10;

    printf("i = %d\n", i);
    printf("change i into %d\n", random);
    read(0, buf, 0x400);
    printf("i = %d\n", i);
    printf("%d\n", random);

    if(i == random){
        printf("success\n");
    }

    return 0;
}

/*gcc -m32 -fno-stack-protector -mpreferred-stack-boundary=2 -z execstack -no-pie -fno-pie -o*/