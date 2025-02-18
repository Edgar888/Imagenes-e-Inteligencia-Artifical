import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

# --- Algoritmo Genético ---
def generar_cadena_aleatoria(longitud):
    """Desde los abismos insondables del caos, se forma una cadena de caracteres."""
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(longitud))

def calcular_aptitud(cadena, objetivo):
    """Evalúa la aptitud, un eco de cuán cerca está la cadena de desentrañar el orden cósmico."""
    return sum(1 for a, b in zip(cadena, objetivo) if a == b)

def mutar(cadena, tasa_mutacion=0.01):
    """En el aliento de Azathoth, las cadenas sufren mutaciones aleatorias."""
    return ''.join(
        c if random.random() > tasa_mutacion else random.choice(string.ascii_uppercase + ' ')
        for c in cadena
    )

def cruzar(cadena1, cadena2):
    """En el umbral entre mundos, dos cadenas se entrelazan."""
    punto_cruce = random.randint(0, len(cadena1) - 1)
    return cadena1[:punto_cruce] + cadena2[punto_cruce:]

def ejecutar_algoritmo_genetico(objetivo, tamano_poblacion, tasa_mutacion, progreso, resultado_label):
    """Ejecuta el algoritmo genético y actualiza la interfaz gráfica con los resultados."""
    longitud_objetivo = len(objetivo)
    poblacion = [generar_cadena_aleatoria(longitud_objetivo) for _ in range(tamano_poblacion)]
    
    generacion = 0
    while True:
        # Evaluar la aptitud de la población
        aptitudes = [(calcular_aptitud(cadena, objetivo), cadena) for cadena in poblacion]
        aptitudes.sort(reverse=True, key=lambda x: x[0])

        # Obtener el mejor resultado de la generación
        mejor_aptitud, mejor_cadena = aptitudes[0]
        progreso["value"] = (mejor_aptitud / len(objetivo)) * 100
        resultado_label.config(text=f"Generación {generacion}: {mejor_cadena} (Aptitud: {mejor_aptitud})")
        root.update()

        if mejor_cadena == objetivo:
            messagebox.showinfo("Éxito", f"¡La cadena objetivo fue encontrada en la generación {generacion}!")
            break

        # Seleccionar las mejores cadenas para la siguiente generación
        padres = [cadena for _, cadena in aptitudes[:tamano_poblacion // 2]]

        # Crear nueva generación mediante cruzamiento y mutación
        nueva_poblacion = []
        while len(nueva_poblacion) < tamano_poblacion:
            padre1, padre2 = random.sample(padres, 2)
            hijo = cruzar(padre1, padre2)
            hijo = mutar(hijo, tasa_mutacion)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion
        generacion += 1

# --- Interfaz Gráfica ---
def iniciar_algoritmo():
    """Inicia el algoritmo genético con los parámetros ingresados por el usuario."""
    try:
        objetivo = objetivo_entry.get().strip().upper()
        tamano_poblacion = int(poblacion_entry.get())
        tasa_mutacion = float(mutacion_entry.get())
        
        if not objetivo:
            raise ValueError("La cadena objetivo no puede estar vacía.")
        if tamano_poblacion <= 0 or not (0 <= tasa_mutacion <= 1):
            raise ValueError("Tamaño de población y tasa de mutación deben ser valores válidos.")

        ejecutar_algoritmo_genetico(objetivo, tamano_poblacion, tasa_mutacion, progreso, resultado_label)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Crear ventana principal
root = tk.Tk()
root.title("Algoritmo Genético - Inspirado en Lovecraft")

# Marco de entrada
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Cadena objetivo:").grid(row=0, column=0, sticky=tk.W)
objetivo_entry = ttk.Entry(frame, width=40)
objetivo_entry.grid(row=0, column=1)

ttk.Label(frame, text="Tamaño de población:").grid(row=1, column=0, sticky=tk.W)
poblacion_entry = ttk.Entry(frame, width=20)
poblacion_entry.grid(row=1, column=1)

ttk.Label(frame, text="Tasa de mutación:").grid(row=2, column=0, sticky=tk.W)
mutacion_entry = ttk.Entry(frame, width=20)
mutacion_entry.grid(row=2, column=1)

# Botón para iniciar
iniciar_button = ttk.Button(frame, text="Iniciar", command=iniciar_algoritmo)
iniciar_button.grid(row=3, column=0, columnspan=2)

# Barra de progreso
progreso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progreso.grid(row=1, column=0, pady=10)

# Resultado
resultado_label = ttk.Label(root, text="Resultado: ", anchor="center")
resultado_label.grid(row=2, column=0, pady=10)

# Iniciar el bucle principal
root.mainloop()
