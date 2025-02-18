## Edgar Montiel Ledesma
## 317317794

import tkinter as tk

def convertir_a_binario(numero, longitud=8):
    """Convierte un número a binario con una longitud específica."""
    return format(numero, f'0{longitud}b')

def generar_reglas(numero_regla):
    """Genera las reglas de producción a partir del número de la regla."""
    binario = convertir_a_binario(numero_regla)
    combinaciones = [
        "111", "110", "101", "100", 
        "011", "010", "001", "000"
    ]
    
    reglas = {}
    for i, combinacion in enumerate(combinaciones):
        reglas[combinacion] = binario[i]
    
    return reglas, combinaciones, binario

def evolucionar(estado_actual, reglas):
    nuevo_estado = ''
    for i in range(len(estado_actual)):
        if i == 0:
            vecindario = estado_actual[-1] + estado_actual[i:i+2]
        elif i == len(estado_actual) - 1:
            vecindario = estado_actual[i-1:] + estado_actual[0]
        else:
            vecindario = estado_actual[i-1:i+2]
        
        nuevo_estado += reglas.get(vecindario, '0')
    return nuevo_estado

def pintar_autómata(canvas, estado, reglas, pasos, tam_celda):
    for paso in range(pasos):
        for i, celda in enumerate(estado):
            color = "black" if celda == '1' else "white"
            canvas.create_rectangle(
                i * tam_celda, paso * tam_celda,
                (i + 1) * tam_celda, (paso + 1) * tam_celda,
                fill=color, outline=color
            )
        estado = evolucionar(estado, reglas)

def mostrar_combinaciones(lateral_frame, combinaciones, binario):
    for widget in lateral_frame.winfo_children():
        widget.destroy()  # Limpiar el frame lateral antes de mostrar nuevas combinaciones

    for i, combinacion in enumerate(combinaciones):
        label = tk.Label(lateral_frame, text=f"{combinacion} -> {binario[i]}", font=("Arial", 12))
        label.pack(anchor="w")

def iniciar_simulacion():
    numero_regla = int(entry_regla.get())
    reglas, combinaciones, binario = generar_reglas(numero_regla)
    n = 101  # longitud de la cadena
    estado_inicial = '0' * (n // 2) + '1' + '0' * (n // 2)
    pasos = 150
    tam_celda = 5

    canvas.delete("all")
    pintar_autómata(canvas, estado_inicial, reglas, pasos, tam_celda)
    mostrar_combinaciones(lateral_frame, combinaciones, binario)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Autómata de Wolfram")

frame = tk.Frame(root)
frame.pack(side=tk.TOP, pady=10)

label = tk.Label(frame, text="Introduce el número de la regla (0-255):")
label.pack(side=tk.LEFT)

entry_regla = tk.Entry(frame)
entry_regla.pack(side=tk.LEFT)

boton_iniciar = tk.Button(frame, text="Iniciar Simulación", command=iniciar_simulacion)
boton_iniciar.pack(side=tk.LEFT)

canvas = tk.Canvas(root, width=505, height=750, bg="white")
canvas.pack(side=tk.LEFT)

lateral_frame = tk.Frame(root)
lateral_frame.pack(side=tk.LEFT, padx=20)

root.mainloop()
