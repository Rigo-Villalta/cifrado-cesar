####################################################################################
# Como librerias usamos Thinter para entorno gráfico para Python
##
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import hashlib
import os

####################################################################################
# Función que encripta la contraseña que el usuario ingresa a SHA256 como proteccion
#
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

####################################################################################
# Si no existe la clave almacenada, genera un archivo y solicita al usuario la clave
##
#def verify_password_file():
#    password_file = "password.sha256"
#    if not os.path.exists(password_file):
#        password = simpledialog.askstring("Nueva Contraseña", "Ingrese una nueva contraseña de administración:", show='*')
#        if password:
#            hashed_password = hash_password(password)
#            with open(password_file, "w") as file:
#                file.write(hashed_password)
#            messagebox.showinfo("Archivo Creado", "Archivo de contraseña creado.")
#        else:
#            messagebox.showerror("Error", "No se ingresó una contraseña. Se cerrará la aplicación.")
#            exit()

####################################################################################
# Para realizar cambios en el cifrado cesar o cambio de clave solicita la verificacion de la contraseña
##
#def verify_password():
#    with open("password.sha256", "r") as file:
#        stored_password_hash = file.read().strip()
#        entered_password = simpledialog.askstring("Verificación", "Ingrese la contraseña actual:", show='*')
#        if entered_password is None:
#            return False
#        return hash_password(entered_password) == stored_password_hash

####################################################################################
# Esta funcion valida la existencia del script de configuración
##
def open_config_window():
    if os.path.exists("config.py"):
        subprocess.run(["python", "config.py"])
    else:
        messagebox.showerror("Error", "El script de configuración no se encuentra.")

####################################################################################
# Llamada al script de cifrado
##
def open_cifrar_window():
    subprocess.run(["python", "cifrar.py"])

####################################################################################
# Llamada al script de descifrado
##
def open_descifrar_window():
    subprocess.run(["python", "descifrar.py"])

####################################################################################
# Si el archivo con el parametro de cifrado no existe lo crea y establece el valor por defecto a 3
##
def check_or_create_config_file():
    config_file = "config.cfg"
    if not os.path.exists(config_file):
        with open(config_file, "w") as file:
            file.write("cesar = 3\n")
        messagebox.showinfo("Configuración creada", "Archivo de configuración de cifrado creado.")

# Función para abrir el script de créditos
def open_creditos_window():
    subprocess.run(["python", "creditos.py"])



####################################################################################
# Funcion principal y control de aspecto gráfico
##
def main_window():
    # Icono, dimensiones de ventana, Imagen de logo y Labels y titulo de ventana
    root = tk.Tk()
    root.iconbitmap('icon.ico')
    root.geometry("300x400")
    logo_image = tk.PhotoImage(file='logo.png')
    logo_image = logo_image.subsample(2, 2)
    logo_label = tk.Label(root, image=logo_image)
    logo_label.image = logo_image  # Keep a reference
    logo_label.pack(pady=10)
    root.title("Menú Principal - Caesar")

    # Label principal 
    cesar_label = tk.Label(root, text='Cifrado César')
    cesar_label.pack(pady=10)

    # Cifrar
    cifrar_button = tk.Button(root, text="🔒 Cifrar", command=open_cifrar_window)
    cifrar_button.pack(pady=10)

    # Descifrar
    descifrar_button = tk.Button(root, text="🔓 Descifrar", command=open_descifrar_window)
    descifrar_button.pack(pady=10)

    # Botón de créditos
    creditos_button = tk.Button(root, text="👥 Créditos", command=open_creditos_window)
    creditos_button.pack(side='bottom', anchor='sw', pady=10, padx=10)
    
    # Configurar Contraseña/Parámetro César
    conf_button = tk.Button(root, text="Configurar ⚙", command=open_config_window)
    conf_button.pack(side='bottom', anchor='se', pady=10, padx=10)
    root.mainloop()

####################################################################################
# Funciones iniciales
##
if __name__ == "__main__":
    check_or_create_config_file()
    main_window()
