###################################################################################
# Como librerias usamos Thinter para entorno gráfico para Python
##
import tkinter as tk
from tkinter import messagebox, Entry, simpledialog

####################################################################################
# Lectura del parámetro llave para el cifrado
#
def read_cesar_key():
    try:
        with open("config.cfg", "r") as file:
            for line in file:
                if line.startswith("cesar"):
                    _, value = line.split("=")
                    return int(value.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de configuración no encontrado.")
        return 0

####################################################################################
# Proceso de descifrado
#
def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            resultado += chr((ord(caracter) - ascii_offset - desplazamiento) % 26 + ascii_offset)
        else:
            resultado += caracter
    return resultado

####################################################################################
# Si se comprueba al usuario, se procede con el descifrado del mensaje
#
def process_descifrado():
    mensaje_cifrado = message_entry.get()
    if mensaje_cifrado:
        desplazamiento = read_cesar_key()
        mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
        descifrado_text.config(state=tk.NORMAL)
        descifrado_text.delete("1.0", tk.END)
        descifrado_text.insert(tk.END, mensaje_descifrado)
        descifrado_text.config(state=tk.DISABLED)

####################################################################################
# Función principal y control de aspecto gráfico
#
def descifrar_window():
    global message_entry, descifrado_text

    root = tk.Tk()
    root.geometry('450x350')
    root.iconbitmap('icon.ico')
    root.title("Descifrar")

    # Label principal
    label = tk.Label(root, text="Mensaje a descifrar:")
    label.pack(pady=5)

    # Mensaje cifrado
    message_entry = Entry(root, width=50)
    message_entry.pack(pady=10)

    # Descifrar
    descifrar_button = tk.Button(root, text="Descifrar Mensaje", command=process_descifrado)
    descifrar_button.pack(pady=10)

    # Mensaje sin cifrado
    descifrado_label = tk.Label(root, text="Mensaje Descifrado:")
    descifrado_label.pack(pady=5)
    descifrado_text = tk.Text(root, height=4, width=50)
    descifrado_text.pack(pady=5)
    descifrado_text.config(state=tk.DISABLED)

    root.mainloop()

####################################################################################
# Cambio de parámetro de cifrado para la lectura
#
def change_cesar_value():
    new_value_message = f" Ingrese el nuevo valor de desplazamiento para César [0-25], este valor deberá ser conocido para descifrar el mensaje:"
    new_value = simpledialog.askinteger("Valor de César", new_value_message, minvalue=0, maxvalue=25)
    if new_value is not None:
        with open("config.cfg", "w") as file:
            file.write(f"cesar = {new_value}\n")
        descifrar_window()

####################################################################################
# Funciones iniciales
##
if __name__ == "__main__":
    change_cesar_value()
