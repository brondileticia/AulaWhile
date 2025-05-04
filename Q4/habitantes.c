#include <stdio.h>

int main() {
    int idade, sexo;
    float salario;
    int contador = 0, mulheres_baixa_renda = 0;
    int maior_idade = -1, menor_idade = 200;
    float soma_salarial = 0.0;

    while (1) {
        printf("Idade: ");
        scanf("%d", &idade);

        if (idade < 0) {
            break;
        }

        printf("Sexo 1=F 2=M: ");
        scanf("%d", &sexo);

        printf("Salario:\n");
        scanf("%f", &salario);

        soma_salarial += salario;
        contador++;

        if (idade > maior_idade) {
            maior_idade = idade;
        }
        if (idade < menor_idade) {
            menor_idade = idade;
        }

        if (sexo == 1 && salario <= 1000.00) {
            mulheres_baixa_renda++;
        }
    }

    if (contador > 0) {
        printf("Idade: Media salarial = %.0f\n", soma_salarial / contador);
        printf("Maior idade = %d Menor idade = %d\n", maior_idade, menor_idade);
        printf("Mulheres baixa renda = %d\n", mulheres_baixa_renda);
    } else {
        printf("Nenhum dado foi inserido.\n");
    }

    return 0;
}
