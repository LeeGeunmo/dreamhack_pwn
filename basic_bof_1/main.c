#include <stdio.h>

int main(void){
    char buf[20];
    int i = 10;

    scanf("%s", buf);
    printf(buf);

    if(i == 16706){
        printf("success");
    }

    return 0;
}