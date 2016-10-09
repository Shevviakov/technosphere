
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

    //increase_size(divs, &size);
    divs = realloc(divs, (size *= 2)*sizeof(long long));
    printf("Increased size from 2 to 4\n");
    for (k=0; k<size; k++) printf("%lld ", divs[k]);
    printf("\n");

    i = 1;
    
    for (q=2; N>1; q++) {
        while ((N % q) == 0) {
            divs[i++] = q;
            N /= q;
            if (i >= size) {
                long long *new_divs;
                new_divs = realloc(divs, (size *= 2) * sizeof(long long));
                if (new_divs == NULL) {
                    printf
                }
                printf("Increased size from to %d\n", size);
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

    scanf("%lld", &num);


    long long *divs = find_divs(num);

    return 0;
}
