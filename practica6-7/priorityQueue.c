//cola doble de prioridades
//1. Pedir al usuario el nombre de la tarea y su nivel de prioridad 1-10
//2. Insertar en la cola segun sea la prioridad el nombre de la tarea a resolver
//3. Si la prioridad es < 5 se inserta por TAIL, si es > 5 se inserta por HEAD
// 4. Una vez insertadas todas las tareas, mostrar la cola de prioridades
// 5. Elegir un numero aleatorio entre 1-100, si el numero es par se resuelve la primera tarea de baja prioridad
// en caso contrario la primer tarea de alta prioridad

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define MAX_STR 60
#define MAX_LEN 100

void adding_by_head(char arr[][MAX_LEN], char *item, int *, int *);
void adding_by_tail(char arr[][MAX_LEN], char *item, int *, int *);
char* removing_by_head(char arr[][MAX_LEN], int *, int *);
char* removing_by_tail(char arr[][MAX_LEN], int *, int *);
void display(char arr[][MAX_LEN], int );
int count(char arr[][MAX_LEN], int);
int elegirNumero();

int main() {
    char arr[MAX_STR][MAX_LEN];
    int head, tail, i, n, priori, comp, opcion, numero_elegido;
    char tarea[MAX_LEN];
    
    tail= head = -1;

    comp = 0;
    priori = 0;
    printf("Aqui puede ingresar una lista de tareas de baja y alta prioridad segun una escala del 1 al 10");
    printf("\n");
    printf("Cuantas tareas va ingresar a la lista?");
    scanf("%d", &opcion);
    while(comp < opcion){
        printf("Se han agregado %d tareas a la lista\n", comp);
        printf("Que prioridad tiene su tarea en una escala del 1 al 10? ");
        scanf("%d", &priori);
        getchar(); //limpiar el buffer para leer una cadena de texto completa
        printf("Ingrese el nombre de su tarea: ");
        fgets(tarea, MAX_LEN, stdin); //para leer una cadena con espacios
        tarea[strcspn(tarea, "\n")] = '\0';
        comp ++;
        if(priori <= 5){
          adding_by_tail(arr, tarea, &head, &tail);
        }else{
          adding_by_head(arr, tarea, &head, &tail);
        }
    }


    //Mostrar la cola de prioridades
    printf("Aqui esta tu lista de tareas: ");
    display(arr, tail);
    //Elegir un numero entre el 1 y el 100 para resolver las tareas
    numero_elegido = elegirNumero();

    //si es par se resuelve la tarea de baja prioridad
    int tareasTotales = count(arr, tail);
    for(int x = 0; x <= tareasTotales; x ++){
        if(numero_elegido % 2 == 0){
            char *tareaHecha = removing_by_tail(arr, &head, &tail);
            printf("Se realizo la tarea: %s de baja prioridad\n", tareaHecha);
            free(tareaHecha); //se libera la memoria que ocupa la copia de la tarea
        }else {
            char *tareaHecha = removing_by_head(arr, &head, &tail);
            printf("Se realizo la tarea: %s de alta prioridad\n", tareaHecha);
            free(tareaHecha);
        }
    }
    return 0;

}

void adding_by_head(char arr[][MAX_LEN], char *item, int *phead, int *ptail) {
  int i, c;

  if (*phead == 0 && *ptail == MAX_STR - 1) {
    printf("\nDeque is full.\n");
    return;
  }

  if (*phead == -1) {
    *phead = *ptail = 0;
    strcpy(arr[*phead], item);
    return;
  }

  if (*ptail != MAX_STR - 1) {
    c = count(arr, *ptail);
    for (i = *ptail + 1; i > *phead; i--) {
      strcpy(arr[i], arr[i - 1]);
    }
    strcpy(arr[*phead], item);
    (*ptail)++;
  } else {
    (*phead)--;
    strcpy(arr[*phead], item);
  }
}

void adding_by_tail(char arr[][MAX_LEN], char *item, int *phead, int *ptail) {
  int i, c;

  if (*phead == 0 && *ptail == MAX_STR - 1) {
    printf("\nDeque is full.\n");
    return;
  }

  if (*phead == -1) {
    *ptail = *phead = 0;
    strcpy(arr[*ptail], item);
    return;
  }

  if (*ptail == MAX_STR - 1) {
    for (i = *phead + 1; i <= *ptail; i++) {
      strcpy(arr[i - 1], arr[i]);
    }
    (*ptail)--;
    (*phead)--;
  }
  (*ptail)++;
  strcpy(arr[*ptail], item);
}

char* removing_by_head(char arr[][MAX_LEN], int *phead, int *ptail) {
    char* item = NULL;

    if (*phead == -1) {
        printf("\nDeque is empty.\n");
        return item;
    }
    //creamos una copia de la cadena de texto en el apuntador para regresarla
    item = strdup(arr[*phead]);
    if(item == NULL){
      printf("Error al asignar memoria. \n");
      exit(1);
    }
    arr[*phead][0] = '\0';

    if (*phead == *ptail)
        *phead = *ptail = -1;
    else
        (*phead)++;

    return item;
}

char* removing_by_tail(char arr[][MAX_LEN], int *phead, int *ptail) {
    char* item = NULL;

    if (*phead == -1) {
        printf("\nDeque is empty.\n");
        return 0;
    }
    //creamos una copia de la cadena de texto en el apuntador para regresarla
    item = strdup(arr[*ptail]); 
    if(item == NULL){
      printf("Error al asignar memoria. \n");
      exit(1);
    }
    arr[*ptail][0] = '\0';
    (*ptail)--;
    if (*ptail == -1)
        *phead = -1;
    return item;
}

void display(char arr[][MAX_LEN], int tail){
    int i;

    printf("\n head:  ");
    for (i = 0; i <= tail; i++)
        printf("  %s", arr[i]);
    printf("  :tail\n");

}

int count(char arr[][MAX_LEN], int tail) {
  int c = 0, i;

  for (i = 0; i < tail; i++) {
    if (arr[i][0] != '\0')
      c++;
  }
  return c;
}

int elegirNumero(){
    int numero;
    srand(time(NULL));
    numero = (rand() % 100) + 1;
    return numero;
}