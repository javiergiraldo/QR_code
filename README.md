# Generador de Códigos QR

Esta es una aplicación de escritorio sencilla desarrollada en Python utilizando la biblioteca `tkinter` para la interfaz gráfica y la biblioteca `qrcode` para la generación de códigos QR. Permite a los usuarios ingresar una URL y generar un código QR correspondiente, el cual pueden visualizar y guardar como un archivo PNG.

![Interfaz del Generador de Códigos QR](ruta_a_la_captura_de_pantalla.png)

## Características Principales

* **Generación de Códigos QR:** Convierte cualquier URL ingresada en un código QR legible.
* **Interfaz Gráfica Intuitiva:** Utiliza `tkinter` para proporcionar una experiencia de usuario amigable.
* **Guardar Códigos QR:** Permite guardar los códigos QR generados como archivos de imagen PNG.
* **Codificación de URL:** Asegura que las URLs complejas se codifiquen correctamente para la generación del QR.
* **Visualización en Tiempo Real:** Muestra el código QR generado directamente en la aplicación.
* **Soporte de Logo (Opcional):** Incluye la funcionalidad para mostrar un logo personalizado en la parte inferior de la ventana (requiere un archivo llamado `logo-kappak.png` en el mismo directorio).

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalado Python en tu sistema. Además, las siguientes bibliotecas deben estar instaladas:

* `tkinter`: Generalmente viene incluido con las instalaciones estándar de Python.
* `qrcode`: Para la generación de códigos QR. Puedes instalarlo con pip:
    ```bash
    pip install qrcode Pillow
    ```
    Nota: `Pillow` es necesario para trabajar con las imágenes generadas por `qrcode`.

## Cómo Utilizar

1.  **Clona el repositorio** (si aún no lo has hecho) a tu máquina local.
2.  **Asegúrate de tener instaladas las dependencias.** Si no las tienes, ejecuta el comando `pip install qrcode Pillow`.
3.  **Ejecuta el script de Python:**
    ```bash
    python tu_script.py
    ```
    (Reemplaza `tu_script.py` con el nombre de tu archivo Python, en este caso, el nombre que le hayas dado al archivo con el código que compartiste).
4.  **Ingresa la URL:** En la ventana de la aplicación, escribe o pega la URL que deseas convertir en un código QR.
5.  **Genera el QR:** Haz clic en el botón "Generar QR". El código QR correspondiente se mostrará en la ventana.
6.  **Guarda el QR:** Si deseas guardar el código QR como un archivo PNG, haz clic en el botón "Guardar QR" y elige la ubicación y el nombre del archivo.

## Personalización (Opcional)

* **Logo:** Para mostrar un logo en la parte inferior de la ventana, coloca un archivo de imagen PNG llamado `logo-kappak.png` en el mismo directorio donde se encuentra el script de Python. Puedes ajustar el tamaño del logo modificando las dimensiones en la línea correspondiente del código.

## Autor

Javier Giraldo

## Licencia

MIT License

Copyright (c) 2025 kappak-dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.