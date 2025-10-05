import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - UEA")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Lista donde se guardarán las tareas (texto y estado)
        self.tareas = []

        # ----- INTERFAZ GRÁFICA -----
        self.lbl_titulo = tk.Label(root, text="Gestor de Tareas", font=("Arial", 14, "bold"))
        self.lbl_titulo.pack(pady=10)

        # Campo de entrada
        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=5)
        self.entrada.focus()

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)

        self.btn_agregar = tk.Button(frame_botones, text="Agregar", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(frame_botones, text="Completar", command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.lista = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.lista.pack(pady=10)

        # ----- ATAJOS DE TECLADO -----
        self.root.bind("<Return>", lambda event: self.agregar_tarea())       # Enter → agregar tarea
        self.root.bind("<c>", lambda event: self.marcar_completada())        # C → marcar completada
        self.root.bind("<d>", lambda event: self.eliminar_tarea())           # D → eliminar
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())      # Supr → eliminar
        self.root.bind("<Escape>", lambda event: self.cerrar_aplicacion())   # Esc → salir

    # ----- FUNCIONES -----
    def agregar_tarea(self):
        tarea = self.entrada.get().strip()
        if tarea:
            self.lista.insert(tk.END, tarea)
            self.tareas.append({"texto": tarea, "completada": False})
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Debe escribir una tarea antes de agregarla.")

    def marcar_completada(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showinfo("Información", "Seleccione una tarea para marcar como completada.")
            return

        indice = seleccion[0]
        tarea_info = self.tareas[indice]

        if not tarea_info["completada"]:
            tarea_info["completada"] = True
            texto = f"✔ {tarea_info['texto']}"
            self.lista.delete(indice)
            self.lista.insert(indice, texto)
            self.lista.itemconfig(indice, fg="green")
        else:
            tarea_info["completada"] = False
            self.lista.delete(indice)
            self.lista.insert(indice, tarea_info["texto"])
            self.lista.itemconfig(indice, fg="black")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showinfo("Información", "Seleccione una tarea para eliminar.")
            return

        indice = seleccion[0]
        self.lista.delete(indice)
        del self.tareas[indice]

    def cerrar_aplicacion(self):
        if messagebox.askyesno("Salir", "¿Desea cerrar la aplicación?"):
            self.root.destroy()

# ----- EJECUCIÓN PRINCIPAL -----
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()
