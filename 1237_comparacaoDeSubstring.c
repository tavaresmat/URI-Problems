#include <stdio.h>
#include <string.h>

#define max(x, y) ((x) > (y) ? (x) : (y))

int main()
{
    char stringA[52], stringB[52];
    int tamanhoA, tamanhoB;

    while (fgets(stringA, 52, stdin))
    {
        fgets(stringB, 52, stdin);

        tamanhoA = strlen(stringA) - 1;
        tamanhoB = strlen(stringB) - 1;

        int maior = 0;
        int index;
        int contador;
        
        for (int i = 0; i <= tamanhoA; i++)
        {
          for (int j = 0; j <= tamanhoB; j++)
          {
              contador = 0;
              index = 0;
              while (((i + index) < tamanhoA) && ((j + index) < tamanhoB))
              {
                  if (stringA[i + index] == stringB[j + index])
                  {
                    index += 1;
                    contador += 1;
                  }
                  else
                    break;
              }
            maior = max(maior, contador);
          }
        }
        printf("%d\n", maior);
    }

    return 0;
}
