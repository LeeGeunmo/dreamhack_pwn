#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

void alarm_handler()
{
    puts("TIME OUT");
    exit(-1);
}

void initialize()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(30);
}

void shell(){
    system("/bin/sh");
}

int main(void){
    // setvbuf(stdin, 0, 2, 0);
    // setvbuf(stdout, 0, 2, 0);
    char buf[50];
    char check[3];
    initialize();
    

    read(0, buf, 200);
    printf("my buffer : %s",buf);
    read(0, buf, 200);

    return 0;
}
//gcc -fstack-protector -z execstack -no-pie -fno-pie -o canary_leak main.c
