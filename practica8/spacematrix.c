//transformar una Sparce Matrix a una lista doblemente ligada
//mostrar por consola la Sparce Matrix y la lista



#include <stdio.h>
#include <stdlib.h>

int **crearmatriz(int, int);
void mostrarMatriz(int **, int, int);
void llenarlista(int **, int, int);

void addnode(int k);
void traverse();
void insertatbegin(int k);
void insertatend(int k);
void insertatpos(int k, int pos);
void delatbegin();
void delatend();
void delatpos(int pos);

int main(){
	int n, c;
	printf("Ingrese el numero de renglones que tiene su matriz: ");
	scanf("%d", &n);
	printf("Ingrese el numero de columnas que tiene su matriz: ");
	scanf("%d", &c);
	
	int **sparcematrix = crearmatriz(n,c);
	
	//llenar la matriz creada con los elementos del usuario
	printf("Ingrese los elementos de su matriz \n");
	for(int i = 0; i < n; i++){
		for(int j = 0; j < c; j++){
			printf("Ingrese el %d:%d elemento: ", i+1, j+1);
			scanf("%d", &sparcematrix[i][j]);
		}
	}
	
	
	mostrarMatriz(sparcematrix, n, c);
	
	llenarlista(sparcematrix, n, c);
	
	//mostrando la lista
	printf("Asi queda la matriz en la lista:\n");
	traverse();
	return 0;
}

int **crearmatriz(int n, int c){
	int i;
	//crear el espacio de la matriz
	int **sparcematrix = (int **)malloc(n * sizeof(int *));
	for(i = 0; i < n; i++){
		sparcematrix[i] = (int *)malloc(c * sizeof(int));
	}
	return sparcematrix;
}

void mostrarMatriz(int **sparcematrix, int n, int c){

	int i,j;
	printf("Asi esta ordenada la matriz\n");
	for(i = 0; i < n; i++){
		printf("[");
		for(j = 0; j < c; j++){
			printf(" %d ", sparcematrix[i][j]);
		}
		printf("]");
		printf("\n");
	}
}

void llenarlista(int **sparcematrix, int n, int c){
	int i,j;
	for(i = 0; i < n; i ++){
		for(j = 0; j < c; j++){
			addnode(sparcematrix[i][j]);
		}
	}
}

