/*
	Задача A-4. Задача о простых сомножителях

	Time limit:	14 s
	Memory limit:	64 M

Составить программу разложения положительного целого числа на простые сомножители и единицу. 

Программа считывает входные данные со стандартного ввода, и печатает результат в стандартный вывод.

Верными входными данными считается только ровно одно положительное число, не превосходящее 2^63 - 1, возможно с предшествующими или последующими пробельными символами. 

Хотя единица не входит в каноническое разложение, но в ответе первым элементом всегда необходимо выводить единицу. 
Считать, что разложение самой единицы состоит только из единицы. 

Процедура разложения числа должна быть оформлена в виде отдельной функции, которой на вход подается целое число. 
Функция должна возвращать указатель на массив целых чисел, содержащий разложение введенного числа на простые сомножители. 
Последний элемент этого массива должен быть нулевым. 

Программа должна уметь обрабатывать ошибки - такие как неверные входные данные(не число, отрицательное число), ошибки выделения памяти и т.п.
В случае возникновения ошибки нужно вывести сообщение "[error]" (без кавычек) и завершать выполнение программы. 

ВАЖНО! Программа в любом случае должна возвращать 0. Не пишите return -1, exit(1) и т.п. Даже если обнаружилась какая-то ошибка, все равно необходимо вернуть 0! (и напечатать [error] в stdout).

	Examples

Input	Output
75
	1 3 5 5
*/

#include <stdio.h>
#include <ctype.h>
#include <errno.h>
#include <stdlib.h>

extern int errno;

void error_exit() {
	printf("[error]");
	exit(0);
}

void increase_size(long long *arr, size_t *size) {
	long long *old_arr = arr;

	int k;
	printf ("%d\n", *size);
        for (k=0; k<*size; k++) printf("%lld ", arr[k]);
        printf("\n");
		
	*size *= 2;
	
	printf ("%d\n", *size);
	long long *new_arr = realloc(old_arr, *size * sizeof(long long));
        for (k=0; k<*size; k++) printf("%lld ", new_arr[k]);
        printf("\n");

	if (new_arr == NULL) {
            printf("Problem with memory reallocating");
            free(arr);
            exit(0);
	}
	arr = new_arr;
        for (k=0; k<*size; k++) printf("%lld ", arr[k]);
        printf("\n");
}

long long* find_divs(long long N) {
    size_t i, size = 2; 
    long long q, *divs = calloc(size, sizeof(long long));

    int k;
    
    divs[0] = 1;
    if (N == 1) return divs;

    increase_size(divs, &size);
    printf("Increased size from 2 to 4\n");
    for (k=0; k<size; k++) printf("%lld ", divs[k]);
    printf("\n");

    i = 1;
    for (q=2; N>1; q++) {
        while ((N % q) == 0) {
            divs[i++] = q;
            N /= q;
            if (i >= size) {
                increase_size(divs, &size);
                for (k=0; k<size; k++) printf("%lld ", divs[k]);
                printf("\n");
            }
        }
    }
    divs[i] = 0;
    return divs;
}

int main () {
    long long num;
    int status, ch;

    status = scanf("%lld", &num);

    if (status < 1 || num <= 0) {error_exit();}
    if (errno) error_exit();
    while ((ch = getchar()) != EOF) { if (!isspace(ch)) error_exit(); }

    long long *divs = find_divs(num);
    //for (i=0; divs[i]>0; i++) {printf("%lld ", divs[i]);}

    return 0;
}
