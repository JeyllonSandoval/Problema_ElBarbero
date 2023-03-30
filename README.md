# Problema_ElBarbero
Explicando y resolviendo el **problema del barbero** usando el **sistema de semáforo** en python

## Barbería con hilos en Python
Este código de Python implementa una solución a un problema clásico conocido como **"El problema del barbero dormilón"** utilizando **hilos** en Python. El problema se refiere a una barbería donde hay una cierta cantidad de sillas para que los clientes esperen y un barbero que atiende a los clientes. El barbero puede estar durmiendo si no hay clientes, pero tan pronto como un cliente llega, se despierta y atiende al cliente. Si no hay sillas disponibles, el cliente se va.

> Este código utiliza la **biblioteca threading** de Python para crear **hilos** para cada cliente y el barbero. También **utiliza semáforos** para manejar las secciones críticas.

# Funcionamiento del código
Al comienzo del código se definen las siguientes **variables** y **semáforos**:

### número máximo de sillas para los clientes
`MAX_SILLAS = 5`  


### semáforos para manejar las secciones críticas
`mutex = threading.Semaphore(1)`  

`clientes_esperando = threading.Semaphore(0)`  

`barbero_ocupado = threading.Semaphore(0)`  


### variables para rastrear el estado del barbero y las sillas de espera
`num_sillas_vacias = MAX_SILLAS`  

`barbero_durmiente = True`  

`MAX_SILLAS`  


representa el número máximo de sillas disponibles para los clientes. mutex es un semáforo para proteger secciones críticas del código. clientes_esperando y barbero_ocupado son semáforos para controlar el flujo de clientes y el estado del barbero. num_sillas_vacias es una variable que rastrea la cantidad de sillas vacías en la barbería, y barbero_durmiente es una variable que indica si el barbero está durmiendo o no.

Luego, se define la función cliente(id) que representa el hilo para cada cliente. Esta función intenta obtener un asiento si hay sillas disponibles y espera si no hay sillas. Si el barbero está dormido, el cliente lo despierta y recibe un corte de pelo. Si el barbero no está durmiendo, el cliente simplemente espera su turno. Después de recibir el corte de pelo, el cliente sale de la barbería.

La función barbero() representa el hilo del barbero. Si no hay clientes, el barbero duerme. Si hay clientes esperando, el barbero atiende al siguiente cliente. Después de atender a un cliente, el barbero espera a que lleguen más clientes.

Finalmente, se crean dos hilos: uno para el barbero y otro para los clientes. Se utilizan semáforos para controlar el flujo de los clientes y el estado del barbero. Cada hilo se ejecuta en paralelo y se duerme al azar entre 1 y 3 segundos para simular el tiempo que toma cada tarea.

## Ejecución del código
Para ejecutar el código, simplemente ejecuta el archivo Python en la terminal:

- python barberia.py

> Esto creará un hilo para el barbero y 30 hilos para los clientes. El número de clientes y la velocidad de ejecución se pueden ajustar en el bucle for en la sección if __name__ == '__main__':.

## Barbería Dormilona
Este es un programa que simula el comportamiento de una barbería con un barbero y varias sillas de espera para los clientes. El barbero atiende a los clientes que están esperando en las sillas, y si no hay sillas disponibles, los clientes se van.

El programa utiliza la biblioteca de hilos **(threading)** para simular varios clientes que llegan a la barbería. Cada cliente es un **hilo** separado, y el barbero también es un **hilo** separado. Los **hilos** comparten recursos críticos, como las sillas de espera, y se utilizan **semáforos** para manejar las secciones críticas.

## En el código, se definen tres semáforos:

- mutex: utilizado para proteger la sección crítica donde se actualiza el número de sillas vacías y se comprueba si hay suficientes sillas para el cliente.
- clientes_esperando: utilizado por los clientes para señalar al barbero que están esperando.
- barbero_ocupado: utilizado por el barbero para señalar que está listo para atender a un cliente.


### Además, hay dos variables globales utilizadas para rastrear el estado del barbero y las sillas de espera:

- num_sillas_vacias: el número actual de sillas de espera vacías.
- barbero_durmiente: una bandera que indica si el barbero está durmiendo o no.  

El programa comienza con el **hilo del barbero**, que está en un bucle infinito. El barbero espera a que los clientes lleguen y se sienten en las sillas de espera. Cuando llega un cliente, el barbero lo atiende y le corta el cabello. Si no hay clientes esperando, el barbero se duerme.

Después de que el **hilo del barbero** se inicia, se inician los **hilos de los clientes**. Cada **hilo de cliente** llega a la barbería y trata de obtener una silla de espera. Si hay una silla disponible, el cliente se sienta y espera a que el barbero lo atienda. Si no hay sillas disponibles, el cliente se va.

Cuando el barbero está disponible, se despierta y atiende a un cliente. Después de que el barbero termina de atender al cliente, el cliente sale de la barbería y libera su silla de espera. Si hay clientes esperando en la fila, el barbero atenderá al siguiente cliente. Si no hay clientes esperando, el barbero se duerme nuevamente.

El código utiliza la función **time.sleep** para simular el tiempo que tarda el barbero en cortar el cabello del cliente y para simular el tiempo que tarda un cliente en llegar a la barbería y sentarse en una silla de espera. La función **random.randint** se utiliza para generar números aleatorios que se utilizan en el tiempo de espera.

Puedes encontrar el código completo en el archivo **Problema_Barberia.py**.
