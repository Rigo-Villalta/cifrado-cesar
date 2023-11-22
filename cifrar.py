###################################################################################
# Como librerias usamos Thinter para entorno gráfico para Python
##
import tkinter as tk
from tkinter import Entry, filedialog, messagebox
import os

####################################################################################
# Lectura del parámetro de cifrado
##
def read_cesar_key():
    try:
        with open("config.cfg", "r") as file:
            for line in file:
                if line.startswith("cesar"):
                    _, value = line.split("=")
                    return int(value.strip())
    except FileNotFoundError:
        return 0

####################################################################################
# Funcion principal y control de aspecto gráfico
##
def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            resultado += chr((ord(caracter) - ascii_offset + desplazamiento) % 26 + ascii_offset)
        else:
            resultado += caracter
    return resultado

####################################################################################
# Conversión a binario
##
def to_binary_string(text):
    return ' '.join(format(ord(char), '08b') for char in text)

####################################################################################
# Conversión a hexadecimal
##
def to_hex_string(text):
    return ' '.join(format(ord(char), '02x') for char in text)

####################################################################################
# Almacenamiento de conversion en archivo (ascii, bin, hex)
##
def save_message(ascii_variant, binary_variant, hex_variant):
    with open("mensaje.db", "w") as file:
        file.write(f"cesar-ascii:\"{ascii_variant}\";\n")
        file.write(f"cesar-bin:\"{binary_variant}\";\n")
        file.write(f"cesar-hex:\"{hex_variant}\";\n")

####################################################################################
# Mostrar las conversiones y cifrado en pantalla
##
def process_message():
    desplazamiento = read_cesar_key()
    mensaje = message_entry.get()
    if mensaje:
        mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
        mensaje_binario = to_binary_string(mensaje_cifrado)
        mensaje_hexadecimal = to_hex_string(mensaje_cifrado)

        save_message(mensaje_cifrado, mensaje_binario, mensaje_hexadecimal)

        ascii_text.config(state=tk.NORMAL)
        ascii_text.delete("1.0", tk.END)
        ascii_text.insert(tk.END, mensaje_cifrado)
        ascii_text.config(state=tk.DISABLED)
        binary_label.config(text=f"Binario: {mensaje_binario}")
        hex_label.config(text=f"Hexadecimal: {mensaje_hexadecimal}")

# Función para verificar si mensaje.db existe
def check_mensaje_db_exists():
    return os.path.exists("mensaje.db")

# Función para guardar el mensaje cifrado
def save_encrypted_message():
    # Ruta del archivo original (mensaje.db)
    source_file = "mensaje.db"

    # Pedir al usuario que elija la ubicación y el nombre del archivo de destino
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            # Leer el contenido de mensaje.db
            with open(source_file, "rb") as file:
                content = file.read()

            # Guardar el contenido en el nuevo archivo (mensajecifrado.txt)
            with open(file_path, "w") as file:
                file.write(content.decode("utf-8"))

            messagebox.showinfo("Guardado", "La copia del mensaje cifrado ha sido guardada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al guardar el archivo: {e}")


####################################################################################
# Proceso principal de cifrado
##
def cifrar_window():
    global message_entry, ascii_text, binary_label, hex_label

    # Icono, dimensiones de ventana, Imagen de logo y Labels y titulo de ventana
    root = tk.Tk()
    root.geometry('450x350')  # Set window size
    root.iconbitmap('icon.ico')  # Set window icon
    root.title("Cifrar")

    # Label principal 
    label = tk.Label(root, text="Ingrese el mensaje a cifrar:")
    label.pack(pady=5)

    # Entrada de mensaje a cifrar
    message_entry = Entry(root, width=50)
    message_entry.pack(pady=10)

    # Cifrar
    cifrar_button = tk.Button(root, text="Cifrar mensaje", command=process_message)
    cifrar_button.pack(pady=10)

    # ascii
    ascii_label = tk.Label(root, text="ASCII: ")
    ascii_label.pack(pady=5)

    # Mensaje en ascii
    ascii_text = tk.Text(root, height=4, width=50)
    ascii_text.pack(pady=5)
    ascii_text.config(state=tk.DISABLED)

    # Mensaje en bin
    binary_label = tk.Label(root, text="Binario: ", wraplength=500)
    binary_label.pack(pady=5)

    # Mensaje en hex
    hex_label = tk.Label(root, text="Hexadecimal: ", wraplength=500)
    hex_label.pack(pady=5)

    # Botón de guardar con ícono de disquete
    save_button = tk.Button(root, text="💾", command=save_encrypted_message)
    save_button.pack(pady=10)

    # Habilitar el botón solo si mensaje.db existe
    save_button['state'] = 'normal' if check_mensaje_db_exists() else 'disabled'

    root.mainloop()

####################################################################################
# Funciones iniciales
##
if __name__ == "__main__":
    cifrar_window()
