#include <stdio.h>

int eqpoint(int arr[], int);

int main(){
  int N, i;
  printf("Ingrese la cantidad de elemenos que tiene su arreglo:");
  scanf("%d", &N);
  int arr[N];

  for(i = 0; i < N; i++){
    printf("Ingrese el %d elemento del arreglo: ", i+1);
    scanf(" %d", &arr[i]);
  }

  int validar = eqpoint(arr, N);
  
  if(validar == -1){
    printf("No se encontro punto de equilibrio en el arreglo");

  }else{
    printf("El punto de equilibrio del arreglo es: %d", validar);
  }

  return 0;
}


int eqpoint(int arr[], int N){
  int i, leftSum, totalSum;
  totalSum = 0;
  leftSum = 0; 
  //sumamos todos los elementos del arreglo
  for(i = 0; i < N; i++){
    totalSum += arr[i];
  }
  //si solamente hay un elemento lo regresamos
  if(totalSum == arr[0]){
    return arr[0];
  }
  
  for(int j = 0; j < N; j++){
    //comprobamos si leftSum es igual a la suma total menos el ultimo elemento
    if(leftSum == totalSum - arr[j]){
      return j + 1; //regresamos el indice del arreglo + 1
    }

    leftSum += arr[j]; //agregamos el elemento para hacer sumas
    totalSum -= arr[j]; //quitamos el elemento que acabamos de sumar
  }
  return -1; 

}

