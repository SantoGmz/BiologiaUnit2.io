import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import subprocess
import platform
import threading
import time




print("Inicio del script")

def hacer_ping(direccion_ip):
    print("Función hacer_ping definida")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', param, '1', direccion_ip]
    try:
        print(f"Intentando ping a: {direccion_ip}")
        proceso = subprocess.run(comando, capture_output=True, text=True, check=True, timeout=5)
        print(f"Ping exitoso a: {direccion_ip}")
        return True, proceso.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error de ping a {direccion_ip}: {e}")
        return False, e.stderr.strip()
    except subprocess.TimeoutExpired:
        print(f"Timeout de ping a: {direccion_ip}")
        return False, "Tiempo de espera agotado"

class PingApp:
    def __init__(self, root):
        print("Inicializando PingApp")
        self.root = root
        self.root.title("Monitor de Conexión")

        self.clientes = []  # Lista para almacenar los clientes (diccionarios con 'nombre', 'ip', 'estado')
        self.tree = None   # Widget Treeview para mostrar los clientes

        self.crear_interfaz()
        print("Interfaz creada")
        self.cargar_clientes() # Opcional

        self.ejecutar_monitoreo_periodico()
        print("Monitoreo periódico iniciado")

    def crear_interfaz(self):
        print("Creando interfaz")
        # Botones de acción
        ttk.Button(self.root, text="Agregar Cliente", command=self.agregar_cliente).pack(pady=5)
        ttk.Button(self.root, text="Editar Cliente", command=self.editar_cliente).pack(pady=5)
        ttk.Button(self.root, text="Eliminar Cliente", command=self.eliminar_cliente).pack(pady=5)

        # Treeview
        self.tree = ttk.Treeview(self.root, columns=('Nombre', 'IP', 'Estado', 'Detalles'), show='headings')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('IP', text='Dirección IP')
        self.tree.heading('Estado', text='Estado')
        self.tree.heading('Detalles', text='Detalles')
        self.tree.pack(expand=True, fill='both', padx=10, pady=10)

    def agregar_cliente(self):
        print("Función agregar_cliente llamada")
        dialog = AgregarEditarClienteDialog(self.root, "Agregar Cliente")
        if dialog.result:
            nombre, ip = dialog.result
            self.clientes.append({'nombre': nombre, 'ip': ip, 'estado': 'Desconocido', 'detalles': ''})
            self.actualizar_tabla()

    def editar_cliente(self):
        print("Función editar_cliente llamada")
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Editar", "Selecciona un cliente para editar.")
            return
        # ... (resto de la función editar_cliente) ...

    def eliminar_cliente(self):
        print("Función eliminar_cliente llamada")
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Eliminar", "Selecciona un cliente para eliminar.")
            return
        # ... (resto de la función eliminar_cliente) ...

    def actualizar_tabla(self):
        print("Función actualizar_tabla llamada")
        for item in self.tree.get_children():
            self.tree.delete(item)
        for cliente in self.clientes:
            self.tree.insert('', tk.END, values=(cliente['nombre'], cliente['ip'], cliente['estado'], cliente['detalles']))

    def monitorear_cliente(self, cliente):
        print(f"Monitoreando cliente: {cliente['nombre']} ({cliente['ip']})")
        conectado, detalles = hacer_ping(cliente['ip'])
        nuevo_estado = "En Línea" if conectado else "Fuera de Línea"
        if nuevo_estado != cliente['estado']:
            print(f"Cambio de estado para {cliente['nombre']}: {cliente['estado']} -> {nuevo_estado}")
            cliente['estado'] = nuevo_estado
            cliente['detalles'] = detalles
            self.actualizar_tabla_hilo()

    def ejecutar_monitoreo_periodico(self):
        print("Ejecutando monitoreo periódico en hilo separado")
        threading.Thread(target=self._monitoreo_periodico, daemon=True).start()

    def _monitoreo_periodico(self):
        print("Hilo de monitoreo periódico iniciado")
        while True:
            for cliente in self.clientes:
                self.monitorear_cliente(cliente)
            time.sleep(5)

    def actualizar_tabla_hilo(self):
        self.root.after(0, self.actualizar_tabla)

    def cargar_clientes(self):
        print("Función cargar_clientes llamada (si está implementada)")
        pass

class AgregarEditarClienteDialog(simpledialog.Dialog):
    def __init__(self, parent, title, nombre_inicial="", ip_inicial=""):
        print(f"Inicializando diálogo: {title}")
        self.nombre = nombre_inicial
        self.ip = ip_inicial
        super().__init__(parent, title=title)

    def body(self, master):
        print("Creando cuerpo del diálogo")
        tk.Label(master, text="Nombre:").grid(row=0, sticky=tk.W)
        self.nombre_entry = tk.Entry(master)
        self.nombre_entry.insert(0, self.nombre)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(master, text="Dirección IP:").grid(row=1, sticky=tk.W)
        self.ip_entry = tk.Entry(master)
        self.ip_entry.insert(0, self.ip)
        self.ip_entry.grid(row=1, column=1)
        return self.nombre_entry # initial focus

    def apply(self):
        print("Función apply del diálogo llamada")
        nombre = self.nombre_entry.get()
        ip = self.ip_entry.get()
        self.result = (nombre, ip)

if __name__ == "__main__":
    print("Bloque principal __name__ == '__main__'")
    root = tk.Tk()
    print("Instancia de tk.Tk() creada")
    app = PingApp(root)
    print("Instancia de PingApp creada")
    root.mainloop()
    print("mainloop() finalizado")