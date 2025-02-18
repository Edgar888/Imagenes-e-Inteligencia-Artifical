## Edgar Montiel Ledesma
## 317317794

Descripción del Programa
Este programa simula un autómata celular de Wolfram utilizando reglas de producción especificadas por un número entre 0 y 255. La simulación se presenta en una interfaz gráfica que muestra la evolución del autómata en una cuadrícula de celdas blancas y negras.

Además, el programa muestra en un panel lateral la combinación binaria que corresponde a la regla seleccionada, permitiendo una fácil visualización de cómo cada combinación de celdas en el vecindario afecta la evolución del autómata.

Requisitos
Python 3.x
Biblioteca estándar tkinter (incluida en la instalación estándar de Python)
Instrucciones de Ejecución

Abre una terminal o línea de comandos.
Navega al directorio donde se encuentra el archivo automata_wolfram_.py
Ejecuta el siguiente comando:
$ python automata_wolfram_gui.py

Interfaz de usuario:
Aparecerá una ventana gráfica donde podrás interactuar con el programa.
Introduce un número entre 0 y 255 en la caja de texto que representa la regla de producción del autómata de Wolfram.
Haz clic en el botón "Iniciar Simulación" para ver la evolución del autómata en la cuadrícula.
A la derecha, verás la representación binaria de la regla seleccionada junto con las combinaciones de vecindario que determinan el próximo estado de las celdas.