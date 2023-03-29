import threading
import time
import random

# número máximo de sillas para los clientes
MAX_SILLAS = 5

# semáforos para manejar las secciones críticas
mutex = threading.Semaphore(1)
clientes_esperando = threading.Semaphore(0)
barbero_ocupado = threading.Semaphore(0)

# variables para rastrear el estado del barbero y las sillas de espera
num_sillas_vacias = MAX_SILLAS
barbero_durmiente = True

def cliente(id):
    global num_sillas_vacias, barbero_durmiente
    print(f"Cliente {id} ha llegado a la barbería.")
    
    # intenta obtener un asiento si hay sillas vacías
    mutex.acquire()
    if num_sillas_vacias > 0:
        print(f"Cliente {id} está esperando su turno.")
        num_sillas_vacias -= 1
        clientes_esperando.release()
        mutex.release()
        barbero_ocupado.acquire()
        barbero_durmiente = False
        print(f"Cliente {id} está siendo atendido.")
    else:
        mutex.release()
        print(f"Cliente {id} se ha ido porque no hay sillas disponibles.")

    # el cliente recibe un corte de cabello
    time.sleep(random.randint(1, 3))

    # el cliente sale de la barbería
    print(f"Cliente {id} ha salido de la barbería.")
    mutex.acquire()
    num_sillas_vacias += 1
    if num_sillas_vacias == 1 and not barbero_durmiente:
        barbero_durmiente = True
        barbero_ocupado.release()
    mutex.release()

def barbero():
    global num_sillas_vacias, barbero_durmiente
    while True:
        print("El barbero está durmiendo.")
        clientes_esperando.acquire()
        mutex.acquire()
        num_sillas_vacias += 1
        barbero_durmiente = False
        barbero_ocupado.release()
        mutex.release()

        # el barbero atiende al cliente
        print("El barbero está atendiendo a un cliente.")
        time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    # crear el hilo del barbero
    hilo_barbero = threading.Thread(target=barbero)
    hilo_barbero.start()

    # crear hilos para los clientes
    for i in range(30):
        hilo_cliente = threading.Thread(target=cliente, args=(i,))
        hilo_cliente.start()
        time.sleep(random.randint(1, 3))
