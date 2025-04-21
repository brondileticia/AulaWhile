#include <stdio.h>

int main() {
    double fahrenheit, celsius;

    while (1) {
        printf("Graus F: ");
        scanf("%lf", &fahrenheit);

        if (fahrenheit <= -459.67) {
            break; 
        }

        celsius = (fahrenheit - 32) * 5 / 9.0;
        
        printf("%.0f\n", celsius);
    }

    return 0;
}
