import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Lista donde se guardan las tareas
tareas = []

# Función para añadir una nueva tarea
def agregar_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

# Función para marcar una tarea como completada
def completar_tarea():
    seleccionado = lista_tareas.curselection()
    if seleccionado:
        indice = seleccionado[0]
        texto = lista_tareas.get(indice)
        if not texto.startswith("[✓]"):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "[✓] " + texto)
    else:
        messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla.")

# Función para eliminar una tarea
def eliminar_tarea():
    seleccionado = lista_tareas.curselection()
    if seleccionado:
        lista_tareas.delete(seleccionado[0])
    else:
        messagebox.showwarning("Aviso", "Selecciona una tarea para eliminarla.")

# Campo de entrada para escribir tareas
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)
entrada.bind("<Return>", agregar_tarea)  # Permite usar Enter

# Botones
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=40, height=10, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

ventana.mainloop()
