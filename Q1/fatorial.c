#include <stdio.h>

int main()
{

    int i, fatorial = 1; 

    printf("Digite N: ");
    scanf('%d', &i);

    while (i > 1) {
            fatorial *= i;
            i--; 
    }
    
    printf("O fatorial de %d é %d", i, fatorial);

	return 0;
}