//transformar una Sparce Matrix a una lista doblemente ligada
//mostrar por consola la Sparce Matrix y la lista



#include <stdio.h>
#include <stdlib.h>
#define COL 5
#define REN 4
void showMatrix(int matrix[][REN]);
void addnode(int i, int j, int k);
void traverse();
/* void insertatbegin(int k);
void insertatend(int k);
void insertatpos(int k, int pos);
void delatbegin();
void delatend();
void delatpos(int pos); */

int main(){
	int matrix [COL][REN] = {{6,0,0,0}, {0,2,0,0}, {0,0,10,0}, {0,2,0,0}, {7,0,0,0}};
	int i, j;
	
	
	for(i = 0; i < REN; i++){
		for(j = 0; j < COL; j++){
			if(matrix[i][j] != 0){	
				int val = matrix[i][j];
				addnode(i, j, val);
			}
			
		}
	}
	
	showMatrix(matrix);
	printf("Los elementos de la matriz dispersa con su ubicacion:\n");
	traverse();
	return 0;

}

void showMatrix(int matrix[][REN]){
	printf("La matriz dispersa es:\n");
	for(int i = 0; i < REN; i++){
		printf("[");
		for(int j = 0; j < COL; j++){
			printf(" %d ", matrix[i][j]);
		}
		printf("]");
		printf("\n");
	}
}
