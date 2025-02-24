import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from PIL import Image
import pytesseract

# Configurar ruta de Tesseract (ajusta según tu instalación)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def adjuntar_imagen():
    global ruta_imagen
    ruta_imagen = filedialog.askopenfilename(
        filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )
    if ruta_imagen:
        label_info.config(text=f"Imagen seleccionada:\n{os.path.basename(ruta_imagen)}")
    else:
        label_info.config(text="No se seleccionó ninguna imagen.")

def procesar_imagen():
    if not ruta_imagen:
        messagebox.showerror("Error", "Por favor, adjunta una imagen primero.")
        return

    try:
        imagen = Image.open(ruta_imagen)
        texto = pytesseract.image_to_string(imagen, lang="spa")
        guardar_texto(texto)
        messagebox.showinfo("Éxito", "Texto extraído y guardado en un archivo .txt")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al procesar la imagen: {e}")

def guardar_texto(texto):
    ruta_guardado = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")]
    )
    if ruta_guardado:
        with open(ruta_guardado, "w", encoding="utf-8") as archivo:
            archivo.write(texto)

# Crear la ventana principal
ventana = Tk()
ventana.title("OCR con Tesseract")
ventana.geometry("400x300")

# Variables
ruta_imagen = ""

# Widgets
label_titulo = Label(ventana, text="OCR con Tesseract", font=("Arial", 16))
label_titulo.pack(pady=10)

btn_adjuntar = Button(ventana, text="Adjuntar Imagen", command=adjuntar_imagen)
btn_adjuntar.pack(pady=5)

label_info = Label(ventana, text="No se ha seleccionado ninguna imagen", wraplength=350, fg="gray")
label_info.pack(pady=5)

btn_procesar = Button(ventana, text="Procesar Imagen", command=procesar_imagen)
btn_procesar.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
