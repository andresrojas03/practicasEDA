/*"pasillos" de la tienda: salud, bebidas y alimentos, electrodomesticos, limpieza, ropa, panaderia, papeleria 
    usar las funciones

    1. Llenar carrito 
    2. Devolver producto
    3. Pagar carrito
    4. Listar productos (imprimir arreglo)

*/
#include <stdio.h>
#include <string.h>
#define TAM 5

struct carrito {
    int precio;
    char nombre[200];
    char pasillo[200];
};


void llenarCarrito(struct carrito *);
void listarProductos(struct carrito *);
void devolverProducto(struct carrito *);
void pagarCarrito(struct carrito *);

int main(){
    int menu=0;
    struct carrito arreglo[TAM]={}; //iniciamos el struct en 0
    printf("Hola, bienvenido a la tienda.");
    llenarCarrito(arreglo);
    while(1){
        printf("\nIngrese una opcion para continuar.");
        printf("\n1.Llenar carrito\n2.Listar Productos\n3.Devolver Producto\n4.Pagar carrito\n");
        scanf("%d",&menu);
        switch(menu){
            case 1:
                llenarCarrito(arreglo);
                break;
            case 2:
                listarProductos(arreglo);
                break;
            case 3:
                devolverProducto(arreglo);
                break;
            case 4:
                pagarCarrito(arreglo);
                return 0;
        }
    }
    return 0;
}

void llenarCarrito(struct carrito arreglo[TAM]){
    int i,opcion;
    printf("\nLa tienda tiene los siguientes articulos (indice/precio/nombre/pasillo): ");
    printf("\n1. 15 pesos, Gansito en Comida");
    printf("\n2. 20 pesos, Cepillo dental en Salud");
    printf("\n3. 5,000 pesos, Lavadora en Electrodomesticos");
    printf("\n4. 40 pesos, Detergente en Limpieza");
    for(i=0; i<TAM; i++) {
        opcion = 0;
        struct carrito carrito1;
        /*
        printf("\nIngrese el precio de su articulo: ");
        setbuf(stdin, NULL);
        scanf("%d", &carrito1.precio);
        getchar();
        printf("\nIngrese el nombre de su articulo: ");
        setbuf(stdin, NULL);
        scanf("%s", carrito1.nombre);
        getchar();
        printf("Ingrese el pasillo de su articulo: ");
        setbuf(stdin, NULL);
        scanf("%s", carrito1.pasillo);
        getchar();
        arreglo[i] = carrito1;
        */
       printf("\n Por favor ingrese el indice de su articulo, si no desea agregar nada mas pulse 5: ");
       setbuf(stdin, NULL);
       scanf("%d",&opcion);
       getchar();
       switch(opcion){
        case 1:
            printf("Agregando Gansito al carrito...");
            carrito1.precio = 15;
            strcpy(carrito1.nombre,"Gansito");
            strcpy(carrito1.pasillo, "Comida");
            printf("Producto agregado!");
            break;
        case 2:
            printf("Agregando Cepillo Dental al carrito...");
            carrito1.precio = 20;
            strcpy(carrito1.nombre, "Cepillo");
            strcpy(carrito1.pasillo, "Salud");
            printf("Producto agregado!");
            break;
        case 3:
            printf("Agregando Lavadora al carrito...");
            carrito1.precio=5000;
            strcpy(carrito1.nombre, "Lavadora");
            strcpy(carrito1.pasillo,"Electrodomesticos");
            printf("Producto agregado!");
            break;
        case 4:
            printf("Agregando Detergente al carrito...");
            carrito1.precio = 40;
            strcpy(carrito1.nombre, "Detergente");
            strcpy(carrito1.pasillo, "Limpieza");
            printf("Producto agregado!");
            break;
        case 5: 
            i = TAM;
       }
       

       arreglo[i] = carrito1;


    }
}

void listarProductos(struct carrito arreglo[TAM]){
    int i;
    printf("Sus productos son los siguientes: ");
    for(i=TAM-1;i>=0; i--){
        printf("\n");
        printf("Precio: %d\n", arreglo[i].precio);
        printf("Nombre: %s\n", arreglo[i].nombre);
        printf("Pasillo: %s\n", arreglo[i].pasillo);
    }
}

void devolverProducto(struct carrito arreglo[TAM]){
    int i;
    
    for(i=TAM-1; i>=1 ; i--){
        printf("Eliminando el ultimo articulo agregado al carrito...");
        arreglo[i-1].precio = arreglo[i].precio;
        strcpy(arreglo[i-1].nombre,arreglo[i].nombre);
        strcpy(arreglo[i-1].pasillo,arreglo[i].pasillo);
    }
    printf("\nProducto eliminado!");
}


void pagarCarrito(struct carrito arreglo[TAM]){
    int i,total=0;
    for(i=TAM-1;i>=0;i--){
        total += arreglo[i].precio;
    }
    printf("El total de tu compra fue de: %d", total);
}