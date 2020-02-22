# reserva-salas

***Esta liberia puede considerarse deprecada. A mi y a mis amigos nos banearon del sistema por utilizarlo indiscriminadamente, y cambiaron el funcionamiento. Lo libero por si se puede reutilizar algo***

---
 
***AVISO IMPORTANTE: ACUERDATE DE NO HABER UTILIZADO YA TUS DOS HORAS EN OTRA RESERVA.***
***ADEMAS, SI RESERVAS MAS ALLÁ DE SIETE DIAS, EL PROGRAMA PARECE FUNCIONAR PERO NO HACE RESERVA.***

Se deben introducir los datos de los usuarios en el archivo de configuracion. ¡Ojo, desde el programa no se hace nada con esos datos, pero aun asi ten cuidado al introducirlos!

Comando para el uso del script (en este orden):

    reserva.py <Sala> <Intervalo> <Usuario> <Dias> [-d]

Analizemos el comando:

* `-d`: Activa la opción de debug, que permite visualizar mensajes según funcione la ejecución.

* `Sala`: Estan disponibles las siguentes salas, el programa reserva automáticamente
    - ***Canalobre3***
    - ***Canalobre4***
    - ***Canalobre5***
    - ***Canalobre6***
    - ***Canalobre7***
    - ***Canalobre8***
    - ***Canalobre9***
    - ***1102***
    - ***1103***
    - ***1104***
    - ***1105***
    - ***1107***
    - ***6010***


* `Intervalo`: Seleccionar un intervalo de los siguientes
    - ***Uno:*** 09:00 - 11:00
    - ***Dos:*** 11:00 - 13:00
    - ***Tres:*** 13:00 - 15:00
    - ***Cuatro:*** 15:00 - 17:00
    - ***Cinco:*** 17:00 - 19:00
    - ***Seis:*** 19:00 - 21:00


* `Usuario`: Necesario introducir un usuario de los que estén en el archivo de configuración, para usar su usuario y contraseña.

* `Dias`: Indica el numero de dias a los que reservar. Máximo 7.

***Nota*** : No se puede reservar mas allá de 7 días. La forma ideal de ejecutar este script es reservar como tarde 7 días despues pero una hora y media antes de la actual. Ejemplo:

- ***Mal uso*** : Hoy es 1/3 10:00 e intentamos reservar para el 10/3 10:00
- ***Buen uso***: Hoy es 1/3 10:30 e intentamos reservar para el 10/3 9:00 - 11:00. De esta forma, podemos reservar hasta el límite, pues una vez pasados los minutos 00 y 30 podemos reservar todo ese intervalo.
