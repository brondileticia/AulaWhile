#include <stdio.h>

int main() {
    double N;
    int divisao = 0;

    printf("Digite N: ");
    scanf("%lf", &N);

    while (N >= 1) {
        N /= 2;
        divisao++;
    }

    printf("Ultimo resultado = %g\n", N);
    printf("Foram feitas %d divisoes", divisao);

    return 0;
}
