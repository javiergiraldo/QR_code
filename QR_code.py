import tkinter as tk
from tkinter import filedialog
import qrcode
import urllib.parse
from PIL import Image, ImageTk
import os

def generar_qr():
    url = entrada_url.get()
    if not url:
        etiqueta_estado.config(text="Por favor, ingrese una URL")
        return

    url_codificada = urllib.parse.quote(url, safe=':/')
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url_codificada)
    qr.make(fit=True)

    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    
    imagen_qr_tk = ImageTk.PhotoImage(imagen_qr)
    
    etiqueta_qr.config(image=imagen_qr_tk)
    etiqueta_qr.image = imagen_qr_tk
    
    etiqueta_estado.config(text="Código QR generado")

def guardar_qr():
    if hasattr(etiqueta_qr, 'image'):
        archivo = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if archivo:
            imagen = ImageTk.getimage(etiqueta_qr.image)
            imagen.save(archivo)
            etiqueta_estado.config(text=f"Código QR guardado como {archivo}")
    else:
        etiqueta_estado.config(text="Primero genera un código QR")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Código QR")
ventana.geometry("400x500")  # Ajustar el tamaño de la ventana

# Frame principal
frame_principal = tk.Frame(ventana)
frame_principal.pack(expand=True, fill='both', padx=20, pady=20)

# Crear y colocar los widgets
tk.Label(frame_principal, text="Ingrese la URL:").pack(pady=5)
entrada_url = tk.Entry(frame_principal, width=50)
entrada_url.pack(pady=5)

tk.Button(frame_principal, text="Generar QR", command=generar_qr).pack(pady=5)
tk.Button(frame_principal, text="Guardar QR", command=guardar_qr).pack(pady=5)

etiqueta_qr = tk.Label(frame_principal)
etiqueta_qr.pack(pady=10)

etiqueta_estado = tk.Label(frame_principal, text="")
etiqueta_estado.pack(pady=5)

# Agregar logo personalizado
# Reemplazar 'ruta_de_logo.png' con la ruta real de archivo de logo o una ruta relativa
ruta_logo = 'logo-kappak.png'
if os.path.exists(ruta_logo):
    logo_imagen = Image.open(ruta_logo)
    logo_imagen = logo_imagen.resize((300, 300), Image.LANCZOS)  # Ajustar el tamaño según la necesidad
    logo_tk = ImageTk.PhotoImage(logo_imagen)
    etiqueta_logo = tk.Label(frame_principal, image=logo_tk)
    etiqueta_logo.image = logo_tk
    etiqueta_logo.pack(side='bottom', pady=5)
else:
    print(f"No se pudo encontrar el archivo de logo en {ruta_logo}")

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()