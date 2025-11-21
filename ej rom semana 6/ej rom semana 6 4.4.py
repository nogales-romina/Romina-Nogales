import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Prueba de Tkinter")
ventana.geometry("300x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="✔ Tkinter funciona correctamente", font=("Arial", 12))
etiqueta.pack(pady=20)

# Botón
def mostrar_mensaje():
    messagebox.showinfo("Éxito", "¡La librería tkinter está funcionando!")

boton = tk.Button(ventana, text="Hacer clic aquí", command=mostrar_mensaje)
boton.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()