import tkinter as tk

# Definimos las direcciones: 0 = arriba, 1 = derecha, 2 = abajo, 3 = izquierda
direcciones = [(0, -1), (1, 0), (0, 1), (-1, 0)]

class HormigaLangton:
    def __init__(self, canvas, grid_size, cell_size):
        self.canvas = canvas
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # Inicializamos la cuadrícula en blanco
        self.x = grid_size // 2  # Posición inicial de la hormiga
        self.y = grid_size // 2
        self.direccion = 0  # Dirección inicial (0 = arriba)
        self.rects = {}  # Guardamos los rectángulos para dibujar

    def mover_hormiga(self):
        # Cambiar el color de la celda actual y la dirección
        if self.grid[self.y][self.x] == 0:
            self.grid[self.y][self.x] = 1  # Voltear de blanco a negro
            self.direccion = (self.direccion + 1) % 4  # Girar 90º a la derecha
        else:
            self.grid[self.y][self.x] = 0  # Voltear de negro a blanco
            self.direccion = (self.direccion - 1) % 4  # Girar 90º a la izquierda

        # Dibujar la nueva celda
        color = "black" if self.grid[self.y][self.x] == 1 else "white"
        rect = self.rects[(self.x, self.y)]
        self.canvas.itemconfig(rect, fill=color)

        # Mover la hormiga en la dirección actual
        dx, dy = direcciones[self.direccion]
        self.x = (self.x + dx) % self.grid_size
        self.y = (self.y + dy) % self.grid_size

    def dibujar_grid(self):
        """Dibuja la cuadrícula inicial."""
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect = self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    (x + 1) * self.cell_size,
                    (y + 1) * self.cell_size,
                    fill="white", outline="gray"
                )
                self.rects[(x, y)] = rect

def actualizar():
    """Función que actualiza la posición de la hormiga y redibuja la cuadrícula."""
    hormiga.mover_hormiga()
    root.after(5, actualizar)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Hormiga de Langton")

# Configuración del canvas para la cuadrícula
grid_size = 101  # Tamaño de la cuadrícula (51x51 celdas)
cell_size = 10  # Tamaño de cada celda
canvas = tk.Canvas(root, width=grid_size * cell_size, height=grid_size * cell_size)
canvas.pack()

# Creamos la hormiga y dibujamos la cuadrícula
hormiga = HormigaLangton(canvas, grid_size, cell_size)
hormiga.dibujar_grid()

# Iniciar la simulación
actualizar()

root.mainloop()
