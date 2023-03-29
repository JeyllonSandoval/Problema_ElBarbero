# Problema_ElBarbero
Explicando y resolviendo el problema del barbero usando el sistema de semáforo en python

#Explicación del código
El código comienza importando los módulos necesarios threading, time y random.

Luego, se define la constante MAX_SILLAS que representa el número máximo de sillas que hay en la barbería. También se inicializan tres semáforos: mutex, clientes_esperando y barbero_ocupado. mutex se utiliza para proteger secciones críticas del código de hilos concurrentes, clientes_esperando se utiliza para que los clientes esperen si no hay sillas disponibles y barbero_ocupado se utiliza para que el barbero espere si no hay clientes en espera.

Se define la variable num_sillas_vacias para rastrear el número de sillas vacías en la barbería y barbero_durmiente para rastrear si el barbero está durmiendo o no.

Luego, se define la función cliente(id) que representa a un cliente que llega a la barbería. La función toma un argumento id que es un número entero que representa el ID del cliente.

Dentro de la función cliente(id), se intenta obtener un asiento en la barbería usando el semáforo mutex. Si hay sillas vacías, el cliente reduce el número de sillas vacías, indica que está esperando usando clientes_esperando y libera el semáforo mutex. Si no hay sillas vacías, el cliente libera el semáforo mutex y sale de la barbería. Si el cliente logra obtener un asiento, espera a que el barbero lo atienda usando el semáforo barbero_ocupado, indica que el barbero no está durmiendo y luego recibe un corte de cabello. Después de recibir un corte de cabello, el cliente libera el semáforo mutex, sale de la barbería y libera una silla. Si hay clientes esperando y el barbero está durmiendo, el barbero despierta, toma a un cliente y lo atiende.

La función barbero() representa al barbero. Dentro de la función, el barbero espera a que haya clientes esperando usando el semáforo clientes_esperando. Cuando hay clientes esperando, el barbero reduce el número de sillas vacías, indica que no está durmiendo y libera el semáforo barbero_ocupado. El barbero atiende al cliente, espera un tiempo aleatorio y luego vuelve a esperar a que haya clientes esperando.

Finalmente, se crea el hilo del barbero y se inician hilos para los clientes. Los hilos de los clientes se crean en un bucle for y se espera un tiempo aleatorio antes de crear cada hilo.
