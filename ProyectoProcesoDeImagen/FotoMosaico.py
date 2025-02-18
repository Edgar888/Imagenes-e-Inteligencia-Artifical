import os
import random
from tkinter import Tk, Canvas, Button, filedialog, StringVar, OptionMenu
from PIL import Image, ImageTk

# Tamaño de las piezas del mosaico
TILE_SIZE = (10, 10)

# Ruta del directorio de imágenes
IMAGE_DIR = "photos-800000"

# Cargar una imagen y redimensionarla
def load_image(filepath):
    return Image.open(filepath).convert("RGB").resize(TILE_SIZE)

# Distancia euclidiana entre dos colores
def euclidean_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

# Método Riemersma para seleccionar imágenes
def riemersma_selection(target_color, images):
    selected_image = None
    min_distance = float("inf")
    for img in images:
        avg_color = img[1]
        dist = euclidean_distance(target_color, avg_color)
        if dist < min_distance:
            min_distance = dist
            selected_image = img[0]
    return selected_image

# Método Euclidiano para seleccionar imágenes (similar a Riemersma)
def euclidean_selection(target_color, images):
    return riemersma_selection(target_color, images)

# Generar mosaico
def generate_mosaic(input_image, images, method="Riemersma"):
    input_image = input_image.resize((input_image.width // TILE_SIZE[0] * TILE_SIZE[0], 
                                      input_image.height // TILE_SIZE[1] * TILE_SIZE[1]))
    mosaic = Image.new("RGB", input_image.size)
    tiles_x = input_image.width // TILE_SIZE[0]
    tiles_y = input_image.height // TILE_SIZE[1]
    
    for y in range(tiles_y):
        for x in range(tiles_x):
            box = (x * TILE_SIZE[0], y * TILE_SIZE[1], 
                   (x + 1) * TILE_SIZE[0], (y + 1) * TILE_SIZE[1])
            region = input_image.crop(box)
            avg_color = region.resize((1, 1)).getpixel((0, 0))
            if method == "Riemersma":
                selected_image = riemersma_selection(avg_color, images)
            else:
                selected_image = euclidean_selection(avg_color, images)
            tile = load_image(os.path.join(IMAGE_DIR, selected_image))
            mosaic.paste(tile, box)
    
    return mosaic

# Preprocesar imágenes del directorio
def preprocess_images(directory):
    image_files = [f for f in os.listdir(directory) if f.endswith((".jpg", ".png", ".jpeg"))]
    processed_images = []
    for filename in image_files:
        img = load_image(os.path.join(directory, filename))
        avg_color = img.resize((1, 1)).getpixel((0, 0))
        processed_images.append((filename, avg_color))
    return processed_images

# Interfaz gráfica
def create_gui():
    def load_target_image():
        global target_image, target_image_tk
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            target_image = Image.open(file_path).convert("RGB")
            target_image_tk = ImageTk.PhotoImage(target_image)
            canvas_target.create_image(0, 0, anchor="nw", image=target_image_tk)

    def process_mosaic():
        global mosaic_image, mosaic_image_tk
        if target_image is None:
            print("Cargue una imagen primero.")
            return
        method = selection_method.get()
        mosaic_image = generate_mosaic(target_image, preprocessed_images, method)
        mosaic_image_tk = ImageTk.PhotoImage(mosaic_image)
        canvas_result.create_image(0, 0, anchor="nw", image=mosaic_image_tk)

    def save_mosaic():
        if mosaic_image is None:
            print("No hay mosaico para guardar.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG files", "*.jpg"),
                                                            ("PNG files", "*.png"),
                                                            ("All files", "*.*")])
        if file_path:
            mosaic_image.save(file_path)
            print(f"Mosaico guardado en {file_path}.")

    # Ventana principal
    root = Tk()
    root.title("Foto Mosaico")

    # Canvas para la imagen original
    canvas_target = Canvas(root, width=500, height=500, bg="white")
    canvas_target.grid(row=0, column=0)

    # Canvas para la imagen de mosaico
    canvas_result = Canvas(root, width=500, height=500, bg="white")
    canvas_result.grid(row=0, column=1)

    # Selección de método
    selection_method = StringVar(value="Riemersma")
    OptionMenu(root, selection_method, "Riemersma", "Euclidiana").grid(row=1, column=0, columnspan=2)

    # Botones
    Button(root, text="Cargar Imagen", command=load_target_image).grid(row=2, column=0, pady=10)
    Button(root, text="Procesar Mosaico", command=process_mosaic).grid(row=2, column=1, pady=10)
    Button(root, text="Guardar Mosaico", command=save_mosaic).grid(row=3, column=0, columnspan=2, pady=10)

    return root, canvas_target, canvas_result, selection_method

# Variables globales
target_image = None
target_image_tk = None
mosaic_image = None
mosaic_image_tk = None

# Preprocesar imágenes y ejecutar la GUI
if __name__ == "__main__":
    if not os.path.exists(IMAGE_DIR):
        print(f"El directorio '{IMAGE_DIR}' no existe.")
    else:
        print("Preprocesando imágenes, esto puede tardar un poco...")
        preprocessed_images = preprocess_images(IMAGE_DIR)
        print(f"Procesadas {len(preprocessed_images)} imágenes.")
        app, canvas_target, canvas_result, selection_method = create_gui()
        app.mainloop()
