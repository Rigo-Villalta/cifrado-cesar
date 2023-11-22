###################################################################################
# Como librerias usamos Thinter para entorno gráfico para Python
##
import tkinter as tk
from tkinter import simpledialog, messagebox
import hashlib

####################################################################################
# Función que encripta la contraseña que el usuario ingresa a SHA256 como proteccion
#
#def hash_password(password):
#   return hashlib.sha256(password.encode()).hexdigest()

####################################################################################
# Funcion que solicita la contraseña para usar el modulo de configuración
#
#def verify_password():
#    with open("password.sha256", "r") as file:
#        stored_password_hash = file.read().strip()
#        entered_password = simpledialog.askstring("Verificación", "Ingrese la contraseña actual:", show='*')
#        return hash_password(entered_password) == stored_password_hash

####################################################################################
# Cambio de contraseña
#
# def change_password():
#    if verify_password():
#        new_password = simpledialog.askstring("Nueva Contraseña", "Ingrese una nueva contraseña:", show='*')
#        confirm_password = simpledialog.askstring("Confirmar Contraseña", "Confirme la nueva contraseña:", show='*')
        
#        if new_password and new_password == confirm_password:
#            with open("password.sha256", "w") as file:
#                file.write(hash_password(new_password))
#            messagebox.showinfo("Éxito", "Contraseña cambiada correctamente.")
#        else:
#            messagebox.showerror("Error", "Las contraseñas no coinciden.")
#    else:
#        messagebox.showerror("Error", "Contraseña incorrecta.")

####################################################################################
# Lectura del parámetro de cifrado actual
#
def read_current_cesar_value():
    try:
        with open("config.cfg", "r") as file:
            for line in file:
                if line.startswith("cesar"):
                    _, value = line.split("=")
                    return value.strip()
    except FileNotFoundError:
        return "No definido"

####################################################################################
# Cambio de parámetro de cifrado
#
def change_cesar_value():
    current_value = read_current_cesar_value()
    new_value_message = f"Valor actual de César: {current_value}. Ingrese el nuevo valor de desplazamiento para César [0-25]:"
    new_value = simpledialog.askinteger("Valor de César", new_value_message, minvalue=0, maxvalue=25)
    if new_value is not None:
        with open("config.cfg", "w") as file:
            file.write(f"cesar = {new_value}\n")
        messagebox.showinfo("Éxito", "Valor de César actualizado correctamente.")

####################################################################################
# Funcion principal y control de aspecto gráfico
##
def config_window():
    root = tk.Tk()
    root.iconbitmap('icon.ico')
    root.title("Configuración")

    #change_password_button = tk.Button(root, text="Cambiar contraseña", command=change_password)
    #change_password_button.pack(pady=10)

    cesar_message_label = tk.Label(root, text='El cifrado César necesita un valor numérico entre 0 y 25 que sirve de llave de desplazamiento alfabético para cifrar el mensaje.')
    cesar_message_label.pack(pady=10)
    change_cesar_button = tk.Button(root, text="Cambiar valor de llave César 🗝️", command=change_cesar_value)
    change_cesar_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    config_window()
