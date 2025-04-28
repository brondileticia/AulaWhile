#include <stdio.h>

int main() {
    double altura, peso, altura_mais_pesada;
    int pessoa_mais_pesada = 0;
    double maior_peso = 0;
    int i = 1;

    while (i <= 5) {
        printf("Altura da pessoa %d: ", i);
        scanf("%lf", &altura);

        printf("Peso da pessoa %d:\n", i);
        scanf("%lf", &peso);

        if (peso > maior_peso) {
            maior_peso = peso;
            pessoa_mais_pesada = i;
            altura_mais_pesada = altura;
        }
        
        i++;
    }

    printf("A pessoa mais pesada e' a de numero %d, com altura %.1f\n", pessoa_mais_pesada, altura_mais_pesada);

    return 0;
}
