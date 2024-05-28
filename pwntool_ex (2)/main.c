#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <time.h>


void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}


void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(1);
}

int main(int argc, char *argv[]) {
    srand((unsigned)time(NULL));
    int a = rand() % 89999 + 10001;
    int b = rand() % 89999 + 10001;
    unsigned int input = 0;
    unsigned int res = a * b;

    initialize();

    printf("a = %d\n", a);
    printf("b = %d\n", b);
    scanf("%d", &input);

    if(input == res)
        printf("success\n");
    else
        printf("fail\n");

    return 0;
}
