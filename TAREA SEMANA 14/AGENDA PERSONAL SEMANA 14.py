import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, showerror, askyesno
import calendar
from datetime import datetime

class SimpleDatePicker(tk.Toplevel):
    def __init__(self, parent, initial_date=None):
        super().__init__(parent)
        self.title("Seleccionar fecha")
        self.resizable(False, False)
        self.transient(parent)
        self.selected_date = None

        if initial_date:
            try:
                dt = datetime.strptime(initial_date, "%Y-%m-%d")
                self.year, self.month = dt.year, dt.month
            except:
                now = datetime.now()
                self.year, self.month = now.year, now.month
        else:
            now = datetime.now()
            self.year, self.month = now.year, now.month

        self._build_ui()
        self.grab_set()
        self.wait_window()

    def _build_ui(self):
        header = ttk.Frame(self)
        header.pack(padx=8, pady=6)
        ttk.Button(header, text="<", width=3, command=self._prev_month).grid(row=0, column=0)
        self.month_label = ttk.Label(header, text="", width=18, anchor="center")
        self.month_label.grid(row=0, column=1, padx=6)
        ttk.Button(header, text=">", width=3, command=self._next_month).grid(row=0, column=2)
        self.cal_frame = ttk.Frame(self)
        self.cal_frame.pack(padx=8, pady=8)
        self._draw_calendar()

    def _draw_calendar(self):
        for w in self.cal_frame.winfo_children(): w.destroy()
        self.month_label.config(text=f"{calendar.month_name[self.month]} {self.year}")
        for i, d in enumerate(["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"]):
            ttk.Label(self.cal_frame, text=d, width=4, anchor="center").grid(row=0, column=i)
        for r, week in enumerate(calendar.monthcalendar(self.year, self.month), start=1):
            for c, day in enumerate(week):
                if day:
                    ttk.Button(self.cal_frame, text=str(day), width=4,
                               command=lambda d=day: self._select_day(d)).grid(row=r, column=c)

    def _select_day(self, day):
        self.selected_date = f"{self.year:04d}-{self.month:02d}-{day:02d}"
        self.destroy()

    def _prev_month(self):
        self.month -= 1
        if self.month < 1:
            self.month, self.year = 12, self.year - 1
        self._draw_calendar()

    def _next_month(self):
        self.month += 1
        if self.month > 12:
            self.month, self.year = 1, self.year + 1
        self._draw_calendar()

class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Personal")
        self.geometry("700x420")
        self.resizable(False, False)
        self.events = []
        self._create_widgets()

    def _create_widgets(self):
        frame_list = ttk.Frame(self, padding=10)
        frame_list.pack(fill=tk.BOTH, expand=True)
        ttk.Label(frame_list, text="Eventos Programados", font=(None, 12, 'bold')).pack(anchor='w')
        self.tree = ttk.Treeview(frame_list, columns=("date", "time", "desc"), show='headings', height=10)
        self.tree.heading("date", text="Fecha")
        self.tree.heading("time", text="Hora")
        self.tree.heading("desc", text="Descripción")
        self.tree.column("date", width=120, anchor='center')
        self.tree.column("time", width=80, anchor='center')
        self.tree.column("desc", width=460, anchor='w')
        self.tree.pack(fill=tk.BOTH, expand=True, pady=6)

        frame_inputs = ttk.Frame(self, padding=10)
        frame_inputs.pack(fill=tk.X)
        left = ttk.Frame(frame_inputs)
        left.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(left, text="Fecha:").grid(row=0, column=0, padx=6, pady=4)
        self.entry_date = ttk.Entry(left, width=14)
        self.entry_date.grid(row=0, column=1)
        self.entry_date.bind('<1>', self._open_datepicker)
        ttk.Label(left, text="Hora:").grid(row=0, column=2, padx=6)
        self.entry_time = ttk.Entry(left, width=10)
        self.entry_time.grid(row=0, column=3)
        ttk.Label(left, text="Descripción:").grid(row=1, column=0, pady=6)
        self.entry_desc = ttk.Entry(left, width=60)
        self.entry_desc.grid(row=1, column=1, columnspan=3, sticky='w')

        frame_actions = ttk.Frame(frame_inputs, padding=8)
        frame_actions.pack(side=tk.RIGHT)
        ttk.Button(frame_actions, text="Agregar", command=self._add_event).pack(fill=tk.X, pady=4)
        ttk.Button(frame_actions, text="Eliminar", command=self._delete_selected).pack(fill=tk.X, pady=4)
        ttk.Button(frame_actions, text="Salir", command=self.quit).pack(fill=tk.X)

    def _open_datepicker(self, event=None):
        dp = SimpleDatePicker(self, self.entry_date.get().strip() or None)
        if dp.selected_date:
            self.entry_date.delete(0, tk.END)
            self.entry_date.insert(0, dp.selected_date)

    def _add_event(self):
        date_text, time_text, desc_text = self.entry_date.get().strip(), self.entry_time.get().strip(), self.entry_desc.get().strip()
        if not date_text or not desc_text:
            showwarning("Campos requeridos", "Debe ingresar al menos fecha y descripción.")
            return
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
        except:
            showerror("Error", "Formato de fecha inválido (YYYY-MM-DD).")
            return
        if time_text:
            try: datetime.strptime(time_text, "%H:%M")
            except: pass
        self.events.append({"date": date_text, "time": time_text, "desc": desc_text})
        self._refresh_treeview()
        self.entry_date.delete(0, tk.END)
        self.entry_time.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def _delete_selected(self):
        sel = self.tree.selection()
        if not sel: return
        if not askyesno("Confirmar", "¿Eliminar evento(s) seleccionado(s)?"): return
        indices = [int(self.tree.item(iid, 'text')) for iid in sel]
        for idx in sorted(indices, reverse=True):
            if 0 <= idx < len(self.events): del self.events[idx]
        self._refresh_treeview()

    def _refresh_treeview(self):
        for iid in self.tree.get_children(): self.tree.delete(iid)
        self.events.sort(key=lambda ev: (ev['date'], ev['time']))
        for idx, ev in enumerate(self.events):
            self.tree.insert('', 'end', text=str(idx), values=(ev['date'], ev['time'], ev['desc']))

if __name__ == '__main__':
    AgendaApp().mainloop()
