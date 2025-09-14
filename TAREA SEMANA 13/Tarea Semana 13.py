import tkinter as tk
from tkinter import messagebox

# Función para agregar datos
def agregar_dato():
    dato = entry.get()
    if dato.strip() != "":
        lista.insert(tk.END, dato)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un dato antes de agregarlo.")

# Función para limpiar datos
def limpiar():
    lista.delete(0, tk.END)  # borra la lista completa
    entry.delete(0, tk.END)  # limpia el campo de entrada

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Lista de Datos")
ventana.geometry("400x300")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

btn_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_dato)
btn_agregar.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar)
btn_limpiar.grid(row=0, column=1, padx=5)

# Lista de datos
label_lista = tk.Label(ventana, text="Lista de datos:")
label_lista.pack(pady=5)

lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=5)

# Iniciar loop de la aplicación
ventana.mainloop()
