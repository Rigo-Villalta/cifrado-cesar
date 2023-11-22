import tkinter as tk

def creditos_window():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Créditos")

    # Ajustar el tamaño y el ícono de la ventana (ajusta la ruta del ícono si es necesario)
    root.geometry("400x200")
    root.iconbitmap('icon.ico')

    # Label principal
    main_label = tk.Label(root, text="ACO941 | G01T", font=("Arial", 20))
    main_label.pack(anchor='w', padx=10, pady=(10, 0))

    # Label de descripción
    description_label = tk.Label(root, text="Python | Cifrado César", font=("Arial", 10))
    description_label.pack(anchor='w', padx=10)

    # Label de integrantes
    members_label = tk.Label(root, text="Integrantes:", font=("Arial", 12))
    members_label.pack(anchor='w', padx=10, pady=(10, 0))

    # Labels para cada integrante
    members_info = [
        "[CP121738] David Cardona",
        "[MM200462] Alberto Mendoza",
        "[VV000329] Rigoberto Villalta"
    ]
    for member in members_info:
        member_label = tk.Label(root, text=member, anchor='w', font=("Arial", 12))
        member_label.pack(anchor='w', padx=20)

    # Iniciar el loop principal de la ventana
    root.mainloop()

if __name__ == "__main__":
    creditos_window()
