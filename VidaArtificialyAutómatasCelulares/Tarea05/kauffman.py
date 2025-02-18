import random
from tkinter import Tk, Label, Entry, Button, IntVar, Canvas, Frame, messagebox


# Clase de Red Booleana de Kauffman
class RedBooleanaKauffman:
    def __init__(self, num_nodos, k):
        self.num_nodos = num_nodos
        self.k = k
        self.estados = [random.choice([0, 1]) for _ in range(num_nodos)]
        self.conexiones = self._generar_conexiones()
        self.funciones_booleanas = self._generar_funciones_booleanas()

    def _generar_conexiones(self):
        conexiones = []
        for _ in range(self.num_nodos):
            conexiones.append(random.sample(range(self.num_nodos), self.k))
        return conexiones

    def _generar_funciones_booleanas(self):
        funciones = []
        for _ in range(self.num_nodos):
            num_combinaciones = 2 ** self.k
            funciones.append([random.choice([0, 1]) for _ in range(num_combinaciones)])
        return funciones

    def _evaluar_funcion_booleana(self, nodo):
        entradas = self.conexiones[nodo]
        combinacion = ''.join(str(self.estados[i]) for i in entradas)
        indice = int(combinacion, 2)
        return self.funciones_booleanas[nodo][indice]

    def actualizar(self):
        nuevos_estados = [self._evaluar_funcion_booleana(nodo) for nodo in range(self.num_nodos)]
        self.estados = nuevos_estados

    def simular(self, pasos):
        historial = []
        for _ in range(pasos):
            historial.append(self.estados[:])
            self.actualizar()
        return historial


# Ventana principal
ventana = Tk()
ventana.title("Red Booleana de Kauffman")
ventana.geometry("800x600")

# Variables
num_nodos_var = IntVar(value=10)
k_var = IntVar(value=3)
pasos_var = IntVar(value=20)
red = None

# Configuración visual
grid_size = 400  # Tamaño del canvas
node_size = 20   # Tamaño de cada nodo


def inicializar_red():
    global red
    num_nodos = num_nodos_var.get()
    k = k_var.get()
    if k > num_nodos:
        messagebox.showerror("Error", "K no puede ser mayor que el número de nodos.")
        return
    red = RedBooleanaKauffman(num_nodos, k)
    dibujar_red()
    messagebox.showinfo("Info", "Red inicializada correctamente.")


def simular_red():
    pasos = pasos_var.get()
    if not red:
        messagebox.showerror("Error", "Primero inicialice la red.")
        return
    for _ in range(pasos):
        red.actualizar()
        dibujar_red()


def dibujar_red():
    canvas.delete("all")
    nodos_por_fila = int(grid_size // node_size)
    for i, estado in enumerate(red.estados):
        fila = i // nodos_por_fila
        columna = i % nodos_por_fila
        color = "red" if estado == 1 else "white"
        x0 = columna * node_size
        y0 = fila * node_size
        x1 = x0 + node_size
        y1 = y0 + node_size
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")


# Widgets
frame_opciones = Frame(ventana, padx=10, pady=10)
frame_opciones.pack(side="left", fill="y")

Label(frame_opciones, text="Número de nodos:").pack(pady=5)
Entry(frame_opciones, textvariable=num_nodos_var).pack(pady=5)

Label(frame_opciones, text="Conexiones por nodo (K):").pack(pady=5)
Entry(frame_opciones, textvariable=k_var).pack(pady=5)

Label(frame_opciones, text="Pasos de simulación:").pack(pady=5)
Entry(frame_opciones, textvariable=pasos_var).pack(pady=5)

Button(frame_opciones, text="Inicializar Red", command=inicializar_red).pack(pady=20)
Button(frame_opciones, text="Simular", command=simular_red).pack(pady=10)

# Canvas para la red
canvas = Canvas(ventana, width=grid_size, height=grid_size, bg="gray")
canvas.pack(side="right", padx=10, pady=10)

ventana.mainloop()
