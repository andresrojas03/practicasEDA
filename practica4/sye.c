//crear el tablero (arreglo de 10x10)
//casillas con estrella (18,36,40,65)
//casillas con escalera (19->66, 32->53, 67->100, 73->91)
//casillas con serpiente (25->6, 46->12, 74->52, 88->76)
//crear una funcion tirardado() que elija un numero entre el 1 y el 6

/*
imprimir el tablero
    for(x=0;x<10;x++){
        printf("\n[");
        for(y=0;y<10;y++){
            printf("|%d|",tablero[x][y]);
        }
        printf("]");
    }
    printf("\n");
variables de control juego
dado = tirardado();
            printf("---->Tu tirada fue: %d<----", dado);
            player(q,dado, &posicionJugador);
            escalera(q,&posicionJugador);
            serpiente(q,&posicionJugador);
            estrella(q,&posicionJugador);

*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define COL 10
#define FIL 10


int tirardado();

int genTablero(int **tablero);

void mostrarTablero(int **tablero, int posicionJugador, int posicionComputadora);

void player(int **tablero, int dado, int *posicionJugador);
void COM(int **tablero, int dado, int *posicionComputadora);

void escalera(int **tablero, int *posicionJugador);
void serpiente(int **tablero, int *posicionJugador);
void estrella(int **tablero, int *posicionJugador);

int main(){
    srand(time(NULL));
    int **tablero;

    tablero = (int **)malloc(FIL*sizeof(int *));
    for(int x = 0; x<FIL; x++){
        tablero[x]=(int *) malloc(COL*sizeof(int));
    }


    int dado,opcion,inicio; 
    int posicionComputadora= 1;
    int posicionJugador=1;
    opcion = 0;
    inicio = 0; 
    dado = 0;
    
    int *p[10];
    for(int i=0;i<10;i++){
        p[i]= tablero[i];
    }
    int **q;
    q = p;
    
    genTablero(q);
    printf("Se va a tirar una moneda al azar y se decidira quien empieza");
    printf("\nEl resultado es...");
    inicio = rand() % 2 + 1;
    if(inicio==1){
        printf("Comienzas tu");
    }
    if(inicio==2){
        printf("Comienza la computadora");
    }
    while (1) {
    mostrarTablero(q, posicionJugador, posicionComputadora);

    //control por si termino el juego
    if(posicionJugador >=100){
        printf("El jugador ha ganado!!");
        printf("La computadora se quedo en la casilla: %d", posicionComputadora);
        free(tablero);
        break;
    }
    if(posicionComputadora >=100){
        printf("La computadora ha ganado!!");
        printf("El jugador se quedo en la casilla: %d", posicionJugador);
        free(tablero);
        break;
    }
    // Acciones del jugador activo
    if (inicio == 1) {
        printf("\nTe toca. 1. Lanzar dado, 2. Salir: ");
        scanf("%d", &opcion);
        if (opcion == 1) {
            dado = tirardado();
            printf("\n----> Tu tirada fue: %d <----", dado);
            player(q, dado, &posicionJugador);
            escalera(q, &posicionJugador);
            serpiente(q, &posicionJugador);
            estrella(q, &posicionJugador);
        } else if (opcion == 2) {
            break;
        }
    } else if (inicio == 2) {
        // Acciones del otro jugador
        printf("\nLe toca a la computadora");
        dado = tirardado();
        printf("\n----> La tirada de la computadora fue: %d <----", dado);
        player(q, dado, &posicionComputadora);
        escalera(q, &posicionComputadora);
        serpiente(q, &posicionComputadora);
        estrella(q, &posicionComputadora);
    }

    // Cambiar al siguiente jugador
    inicio = (inicio == 1) ? 2 : 1;
}   
    return 0;

}

int genTablero(int **tablero){
    int i,j,n,col;
    col = 91;
    n=92;
    for(i=0;i<10;i++){
        tablero[i][0]=col;
        col-=10;
        for(j=1;j<10;j++){
            tablero[i][j] = n;
            n++;
        }
        n-=19;
          
    }
}

void mostrarTablero(int **tablero, int posicionJugador, int posicionComputadora) {
    printf("\n#### Jugador:X ####\n####Computadora:C####");
    for(int x=0;x<10;x++){
        printf("\n[");
        for(int y=0;y<10;y++){
            if(tablero[x][y] == posicionJugador){ //compara la posicion del jugador con la casilla para mostrarlo
                printf("|**X**|");
            } 
            if(tablero[x][y] == posicionComputadora){
                printf("|**C**|");
            }
            else{
                printf("|%d|",tablero[x][y]); //muestra el numero de la casilla en el tablero
            }
        }
        printf("]");
    }
    printf("\n");
}

int tirardado(){
    int dado;
    dado = rand() % 6 + 1;
    return dado;
}

void player(int **tablero, int dado, int *posicionJugador) {
    // Calcular la nueva posición del jugador
    *posicionJugador += dado;

    // Obtener la fila y la columna donde se encuentra el jugador
    int fila = *posicionJugador / 10; 
    int columna;
    if (fila % 2 == 0) {
        columna = 9 - (*posicionJugador % 10); 
    } else {
        columna = *posicionJugador % 10; 
    }
}

void COM(int **tablero, int dado, int *posicionComputadora){
     // Calcular la nueva posición del jugador
    *posicionComputadora += dado;

    // Obtener la fila y la columna donde se encuentra el jugador
    int fila = *posicionComputadora / 10; 
    int columna;
    if (fila % 2 == 0) {
        columna = 9 - (*posicionComputadora % 10); 
    } else {
        columna = *posicionComputadora % 10; 
    }
}


void escalera(int **tablero, int *posicionJugador){
    switch(*posicionJugador){
        case 19:
            printf("\n----->Caiste en una escalera, pasas a la casilla 66!!<-----");
            *posicionJugador = 66;
            break;
        case 32:
            printf("\n----->Caiste en una escalera, pasas a la casilla 53!!<-----");
            *posicionJugador =53;
            break; 
        case 67:
            printf("\n----->Caiste en una escalera, pasas a la casilla 100!!<-----");
            *posicionJugador = 100;
            printf("\n######Termino el juego######");
            break;
        case 73:
            printf("\n----->Caiste en una escalera, pasas a la casilla 91!!<-----");
            *posicionJugador = 91;
            break;
            
    }
}


void serpiente(int **tablero, int *posicionJugador){
    switch(*posicionJugador){
        case 25:
            printf("\n----->Caiste en una escalera, pasas a la casilla 6!!<-----");
            *posicionJugador = 6;
            break;
        case 46:
            printf("\n----->Caiste en una escalera, pasas a la casilla 12!!<-----");
            *posicionJugador = 12;
            break; 
        case 74:
            printf("\n----->Caiste en una escalera, pasas a la casilla 52!!<-----");
            *posicionJugador = 52;
            printf("\n######Termino el juego######");
            break;
        case 88:
            printf("\n----->Caiste en una escalera, pasas a la casilla 76!!<-----");
            *posicionJugador = 76;
            break;
            
    }
}


void estrella(int **tablero, int *posicionJugador){
    switch(*posicionJugador){
        case 18:
            printf("\nCaiste en una casilla estrella!! Avanzas 5 casillas adicionales.");
            *posicionJugador = 23;
            break;
        case 40:   
            printf("\nCaiste en una casilla estrella!! Avanzas 5 casillas adicionales.");
            *posicionJugador = 45;
            break;
        case 65:
            printf("\nCaiste en una casilla estrella!! Avanzas 5 casillas adicionales.");
            *posicionJugador = 70;
            break;


            
    }
}


