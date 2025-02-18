Edgar Montiel Ledesma
317317794

Descripción del Programa
Este programa implementa el algoritmo de la hormiga de Langton utilizando la biblioteca tkinter para la visualización en una interfaz gráfica. La hormiga de Langton es un autómata celular en el que una "hormiga" se mueve sobre una cuadrícula siguiendo reglas simples:

Si la hormiga está en una celda blanca, gira 90 grados a la derecha y cambia la celda a negra.
Si la hormiga está en una celda negra, gira 90 grados a la izquierda y cambia la celda a blanca.
El programa visualiza estos movimientos y permite observar cómo evoluciona la cuadrícula con el tiempo.

Requisitos
Python 3.x
La biblioteca estándar tkinter (incluida con la mayoría de las instalaciones de Python)
Instrucciones de Ejecución
Clonar o descargar el archivo: Asegúrate de tener el archivo hormiga_langton.py en tu máquina local.

Ejecutar el programa:

Abre una terminal o línea de comandos.
Navega al directorio donde está guardado el archivo hormiga_langton.py.
Ejecuta el siguiente comando:
bash
Copiar código
python hormiga_langton.py
Interacción con la interfaz:

Aparecerá una ventana con una cuadrícula.
La hormiga comenzará en el centro de la cuadrícula y seguirá las reglas de Langton.
La cuadrícula cambiará dinámicamente conforme la hormiga se mueve, mostrando las celdas negras y blancas.
Funcionamiento del Programa
Hormiga: La hormiga empieza en el centro de una cuadrícula de 51x51 celdas.
Celdas: Cada celda es inicialmente blanca. La hormiga se mueve en función del color de la celda en la que se encuentra, siguiendo las reglas mencionadas anteriormente.
Actualización: La posición de la hormiga se actualiza cada 100 ms, y la cuadrícula se redibuja con los cambios.
Personalización
Tamaño de la cuadrícula: Puedes cambiar el tamaño de la cuadrícula modificando la variable grid_size en el código. Actualmente está configurada en 51x51 celdas.
Velocidad de actualización: La velocidad de movimiento de la hormiga se controla con el valor pasado a la función root.after(100, actualizar), donde 100 es el tiempo en milisegundos entre cada actualización.
Compilación
Este programa no requiere ser compilado. Simplemente necesita ser ejecutado en un entorno donde Python 3.x esté instalado.

Notas adicionales
El programa utiliza un enfoque modular que permite fácil expansión si se desea agregar características adicionales, como la modificación del tamaño de la cuadrícula o diferentes reglas de comportamiento.
Si deseas pausar o detener la simulación, puedes cerrar la ventana gráfica en cualquier momento.