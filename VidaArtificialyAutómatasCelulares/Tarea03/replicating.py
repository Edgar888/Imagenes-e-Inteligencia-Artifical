import os

# Definir la temática de Harry Potter en las funciones
def casa_hogwarts(hechizo):
    """Devuelve la casa según el hechizo utilizado."""
    casas = {
        "Expecto Patronum": "Gryffindor",
        "Avada Kedavra": "Slytherin",
        "Lumos": "Ravenclaw",
        "Wingardium Leviosa": "Hufflepuff"
    }
    return casas.get(hechizo, "Casa desconocida")

def hechizo_favorito(casa):
    """Devuelve el hechizo favorito según la casa de Hogwarts."""
    hechizos = {
        "Gryffindor": "Expecto Patronum",
        "Slytherin": "Avada Kedavra",
        "Ravenclaw": "Lumos",
        "Hufflepuff": "Wingardium Leviosa"
    }
    return hechizos.get(casa, "Hechizo desconocido")

def escribir_codigo():
    """Escribe el código fuente en un archivo .py."""
    codigo = '''import os

# Definir la temática de Harry Potter en las funciones
def casa_hogwarts(hechizo):
    """Devuelve la casa según el hechizo utilizado."""
    casas = {{
        "Expecto Patronum": "Gryffindor",
        "Avada Kedavra": "Slytherin",
        "Lumos": "Ravenclaw",
        "Wingardium Leviosa": "Hufflepuff"
    }}
    return casas.get(hechizo, "Casa desconocida")

def hechizo_favorito(casa):
    """Devuelve el hechizo favorito según la casa de Hogwarts."""
    hechizos = {{
        "Gryffindor": "Expecto Patronum",
        "Slytherin": "Avada Kedavra",
        "Ravenclaw": "Lumos",
        "Hufflepuff": "Wingardium Leviosa"
    }}
    return hechizos.get(casa, "Hechizo desconocido")

def escribir_codigo():
    """Escribe el código fuente en un archivo .py."""
    codigo = {0}{1}{0}
    with open("harry_potter_self_replicating.py", "w") as f:
        f.write(codigo.format(chr(39)*3, codigo))

# Llamar las funciones de Harry Potter como ejemplo
print("El hechizo favorito de Gryffindor es:", hechizo_favorito("Gryffindor"))
print("La casa que usa 'Avada Kedavra' es:", casa_hogwarts("Avada Kedavra"))

# Generar el archivo con el código fuente
escribir_codigo()
'''
    with open("harry_potter_self_replicating.py", "w") as f:
        f.write(codigo.format(chr(39)*3, codigo))

# Llamar las funciones de Harry Potter como ejemplo
print("El hechizo favorito de Gryffindor es:", hechizo_favorito("Gryffindor"))
print("La casa que usa 'Avada Kedavra' es:", casa_hogwarts("Avada Kedavra"))

# Generar el archivo con el código fuente
escribir_codigo()
