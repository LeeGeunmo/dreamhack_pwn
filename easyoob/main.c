#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//compile option: gcc -m32 -z execstack -fno-stack-protector -o check main_2.c

void title(void){
    printf("1: array randomize\n");
    printf("2: array sort\n");
    printf("3: print array\n");
    printf("4: print a number in array\n");
    printf("5: exit\n");
}

void swap(int *xp, int *yp) {
    int tmp = *xp;
    *xp = *yp;
    *yp = tmp;
}

void bubbleSort(int arr[], int n) {
    int i;
    if (n == 1)
        return;

    for (i = 0; i < n - 1; i++)
        if (arr[i] > arr[i + 1])
            swap(&arr[i], &arr[i + 1]);
 
    bubbleSort(arr, n - 1);
}

int main(void){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    srand(time(NULL));
    char feedback[100];
    int arr[20];
    int input;
    int i;

    while(1){
        title();
        scanf("%d", &input);

        if(input == 1){
            for(i = 0; i < 20; i++){
                arr[i] = rand() % 99 + 1;
            }
        }
        else if(input == 2){
            bubbleSort(arr, 20);
        }
        else if(input == 3){
            for(i = 0; i < 20; i++)
                printf("arr[%d] = %d\n", i, arr[i]);
        }
        else if(input == 4){
            printf("give me a index you want to know\n");
            scanf("%d", &input);
            if(input < 20)
                printf("arr[%d] = %d\n", input, arr[input]);
            else{
                printf("index is under 19\n");
            }
            input = 4;
        }
        else if(input == 5){
            printf("Write some feedback if you have\n");
            read(0, feedback, 200);
            return 0;
        }
        else{
            printf("Worng input!\n");
        }
    }
    return 0;
}