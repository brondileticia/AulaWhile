#include <stdio.h>

int main() {
    int n, c, a = 0, b = 1, i = 3;

    printf("Digite N: ");
    scanf("%d", &n);

    printf("Digite N: %d %d ", a, b);

    while (i <= n) {
        c = a + b;
        printf("%d ", c);
        a = b;
        b = c;
        i++;
    }

    return 0;
}
