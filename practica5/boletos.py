"""
El programa atiende a las personas uno a uno conforme van llegando
Cada cliente tiene un tiempo t en ser atendido
Se van a atender 20 clientes en total
Usar las funciones peek, dequeue, enqueue

"""
import time
import queue

TAM_COLA = 5

cola_boletos = queue.Queue(TAM_COLA)

clientes = 0
tiempo = 2
print("Bienvenido al sistema, se va a atender a los clientes conforme van llegando al sistema y tendran un tiempo de espera")
while True: 
    if cola_boletos.full():
        print("La cola esta llena! No se pueden aceptar mas clientes.")
        break

    clientes += 1
    if(clientes+1 > TAM_COLA):
        print("Cliente %d entra para ser atendido." % clientes)

        print("Cliente %d sera atendido en %d segundos.\n" %(clientes,tiempo))
        time.sleep(tiempo)
        cola_boletos.put("Cliente %d" % clientes)
        break

    print("Cliente %d entra para ser atendido." % clientes)
    cola_boletos.put(f"Cliente {clientes}")
    print("Cliente %d pasa a la sala de espera..." % (clientes + 1))
    print("Cliente %d sera atendido en %d segundos.\n" % (clientes, tiempo))
    time.sleep(tiempo)



print("\nClientes atendidos:")
while not cola_boletos.empty():
    print(cola_boletos.get())


