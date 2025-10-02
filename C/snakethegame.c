#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define LINHAS 20
#define COLUNAS 40

struct Jogador{
    char nome[5];
    int *pontos;
};

void preencher(struct Jogador *p){
    printf("Jogador: ");
    scanf("%4s", p->nome);

    p->pontos = malloc(sizeof(int));
    if (p->pontos == NULL) {
        printf("Erro de alocação!\n");
        exit(1);
    }

    *(p->pontos) = 0;

}


int random(int min, int max) {
    return min + rand() % (max - min + 1);
}

void cabeca(char matriz[20][40], int linhas, int colunas){
    int linha = random(0, linhas - 1);
    int coluna = random(0, colunas - 1);

    matriz[linha][coluna] = 'O';
}

int main(void){

    char matriz[20][40];

    srand(time(NULL));

    struct Jogador j;

    preencher(&j);

    printf("Pontos: %d\n", *(j.pontos));

    free(j.pontos);

    for (int i = 0; i < LINHAS; i++){
        for (int j = 0; j < COLUNAS; j++){
            matriz[i][j] = ' ';
        }
    }

    cabeca(matriz, LINHAS, COLUNAS);

    for (int i = 0; i < LINHAS; i ++){
        for (int j = 0; j < COLUNAS; j++){
            printf("%c", matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
}