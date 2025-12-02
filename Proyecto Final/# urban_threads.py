# urban_threads.py
import json
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from datetime import datetime

# ---------------------------
# Configuración de archivos
# ---------------------------
INVENTARIO_FILE = "inventario.json"
VENTAS_FILE = "ventas.json"
STOCK_MINIMO = 3

# ---------------------------
# Datos iniciales (por defecto)
# ---------------------------
DEFAULT_INVENTARIO = [
    {"id": "001", "modelo": "sweatpant leg full", "marca": "urban outfitters", "precio": 1090.0, "talla": "XS", "stock": 3, "descripcion": "negros y holgados"},
    {"id": "002", "modelo": "nike air force 1'07LX", "marca": "nike", "precio": 2599.0, "talla": "23", "stock": 2, "descripcion": "negros y detalles plateados"},
    {"id": "003", "modelo": "white lil wayne X NFL X Mitchell & Ness hoodie", "marca": "TRUKFIT", "precio": 2771.0, "talla": "M", "stock": 2, "descripcion": "blanca con detalles azul claro"},
    {"id": "004", "modelo": "sp5der wait web sweatsuit slate gray", "marca": "sp5der", "precio": 6466.0, "talla": "M", "stock": 2, "descripcion": "conjunto de pants y sudadera color gris"},
    {"id": "005", "modelo": "shady records 25th anniversary hoodie", "marca": "shady records", "precio": 1109.0, "talla": "M", "stock": 2, "descripcion": "sudadera azul marino con letras blancas"},
    {"id": "006", "modelo": "T uncutie long ls od", "marca": "diesel", "precio": 3233.0, "talla": "XXS", "stock": 2, "descripcion": "blusa de manga larga negra con el logo de diesel"},
    {"id": "007", "modelo": "baggy jean realtree ap camo", "marca": "supreme", "precio": 3103.0, "talla": "S", "stock": 2, "descripcion": "pantalones baggy camuflajeados"},
    {"id": "008", "modelo": "divine sweats", "marca": "YOUNGLA", "precio": 1015.0, "talla": "S", "stock": 2, "descripcion": "pantalon negro con estampado de calavera"},
    {"id": "009", "modelo": "pants deportivos stadium", "marca": "adiddas", "precio": 1049.0, "talla": "S", "stock": 2, "descripcion": "pants grises con 3 franjas"},
    {"id": "010", "modelo": "katana knit zip-up red", "marca": "nude-project", "precio": 2949.0, "talla": "S", "stock": 2, "descripcion": "sudadera de zipper color rojo cereza"},
]

# ---------------------------
# Funciones de persistencia
# ---------------------------
def cargar_inventario():
    if os.path.exists(INVENTARIO_FILE):
        try:
            with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            messagebox.showwarning("Aviso", "No se pudo leer inventario.json. Se cargará inventario por defecto.")
    # copia profunda simple del default
    return [dict(item) for item in DEFAULT_INVENTARIO]


def guardar_inventario(inventario):
    try:
        with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
            json.dump(inventario, f, ensure_ascii=False, indent=2)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar inventario: {e}")


def cargar_ventas():
    if os.path.exists(VENTAS_FILE):
        try:
            with open(VENTAS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            messagebox.showwarning("Aviso", "No se pudo leer ventas.json. Se iniciará historial vacío.")
    return []


def guardar_ventas(historial):
    try:
        with open(VENTAS_FILE, "w", encoding="utf-8") as f:
            json.dump(historial, f, ensure_ascii=False, indent=2)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar ventas: {e}")


# ---------------------------
# Validaciones y utilidades
# ---------------------------
def validar_numero_positivo(valor, nombre_campo, entero=False):
    """Valida que el valor sea un número positivo. Retorna float o int según entero."""
    try:
        if entero:
            num = int(float(valor))  # acepta '2.0' pero lo convierte a int
        else:
            num = float(valor)
        if num < 0:
            messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' no puede ser negativo.")
            return None
        return int(num) if entero else float(num)
    except Exception:
        messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' debe ser un número válido.")
        return None


def generar_nuevo_id(inventario):
    """Genera un nuevo ID consecutivo basado en el ID numérico más alto actual (rellena con ceros)."""
    max_id = 0
    for p in inventario:
        try:
            n = int(p.get("id", "0"))
            if n > max_id:
                max_id = n
        except Exception:
            continue
    return str(max_id + 1).zfill(3)


# ---------------------------
# Interfaz principal
# ---------------------------
class UrbanThreadsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Urban Threads - Sistema de Inventario")
        self.root.geometry("1100x700")
        self.root.configure(bg="#f5f5f5")

        # Cargar datos
        self.inventario = cargar_inventario()
        self.historial_ventas = cargar_ventas()

        # Botón activo (referencia)
        self.boton_activo = None

        # Estilos y frames
        self.crear_widgets()
        self.mostrar_bienvenida()

    def crear_widgets(self):
        # Título
        titulo = tk.Label(self.root, text="Urban Threads", font=("Helvetica", 28, "bold"), bg="#f5f5f5", fg="#111111")
        titulo.pack(pady=(12, 0))

        subtitulo = tk.Label(self.root, text="Sistema de Gestión de Inventario (datos guardados automáticamente)",
                             font=("Helvetica", 10), bg="#f5f5f5", fg="#666666")
        subtitulo.pack(pady=(0, 8))

        # Frame para botones
        self.frame_botones = tk.Frame(self.root, bg="#f5f5f5")
        self.frame_botones.pack(pady=8)

        btn_style = {"font": ("Helvetica", 10, "bold"), "bg": "#000000", "fg": "white",
                     "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

        # Crear botones (definidos antes de bind)
        self.btn_home = tk.Button(self.frame_botones, text="HOME", command=self.mostrar_bienvenida, **btn_style)
        self.btn_inventario = tk.Button(self.frame_botones, text="INVENTARIO", command=self.mostrar_inventario, **btn_style)
        self.btn_agregar = tk.Button(self.frame_botones, text="AGREGAR", command=self.agregar_tenis, **btn_style)
        self.btn_vender = tk.Button(self.frame_botones, text="VENDER", command=self.vender_tenis, **btn_style)
        self.btn_buscar = tk.Button(self.frame_botones, text="BUSCAR", command=self.buscar_tenis, **btn_style)
        self.btn_historial = tk.Button(self.frame_botones, text="HISTORIAL", command=self.mostrar_historial, **btn_style)
        self.btn_guardar = tk.Button(self.frame_botones, text="GUARDAR", command=self.guardar_datos, **btn_style)

        # Grid botones
        self.btn_home.grid(row=0, column=0, padx=6)
        self.btn_inventario.grid(row=0, column=1, padx=6)
        self.btn_agregar.grid(row=0, column=2, padx=6)
        self.btn_vender.grid(row=0, column=3, padx=6)
        self.btn_buscar.grid(row=0, column=4, padx=6)
        self.btn_historial.grid(row=0, column=5, padx=6)
        self.btn_guardar.grid(row=0, column=6, padx=6)

        # Binds para hover
        for widget in [self.btn_home, self.btn_inventario, self.btn_agregar, self.btn_vender, self.btn_buscar, self.btn_historial, self.btn_guardar]:
            widget.bind("<Enter>", lambda e, w=widget: self.on_enter(w))
            widget.bind("<Leave>", lambda e, w=widget: self.on_leave(w))

        # Area de texto principal (scrollable)
        self.texto = scrolledtext.ScrolledText(self.root,
                                               font=("Open Sans", 11),
                                               bg="#ffffff", fg="#000000",
                                               height=24, padx=16, pady=12,
                                               relief=tk.SOLID, bd=1)
        self.texto.pack(padx=20, pady=(10, 6), fill=tk.BOTH, expand=True)

        # Tags para formato
        self.texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground="#000000")
        self.texto.tag_config("alerta", background="#fff3f0", foreground="#ff4500", font=("Open Sans", 11, "bold"))
        self.texto.tag_config("agotado", background="#fdf2f2", foreground="#cc0000", font=("Open Sans", 11, "bold"))
        self.texto.tag_config("total", font=("Open Sans", 12, "bold"), foreground="#008000")

        # Footer
        footer = tk.Label(self.root, text="2025 Urban Threads 👻", font=("Helvetica", 9), bg="#f5f5f5", fg="#999999")
        footer.pack(pady=(4, 10))

    # ---------------------------
    # UI helpers
    # ---------------------------
    def activar_boton(self, boton):
        # Poner todos negros y el activo naranja
        for w in [self.btn_home, self.btn_inventario, self.btn_agregar, self.btn_vender, self.btn_buscar, self.btn_historial, self.btn_guardar]:
            w.config(bg="#000000")
        if boton:
            boton.config(bg="#ff4500")
            self.boton_activo = boton

    def on_enter(self, widget):
        if widget != self.boton_activo:
            widget.config(bg="#222222")

    def on_leave(self, widget):
        if widget != self.boton_activo:
            widget.config(bg="#000000")

    # ---------------------------
    # Funcionalidades principales
    # ---------------------------
    def mostrar_bienvenida(self):
        self.texto.delete(1.0, tk.END)
        self.activar_boton(self.btn_home)

        total_modelos = len(self.inventario)
        total_pares = sum(int(p.get("stock", 0)) for p in self.inventario)
        ventas_hoy = sum(1 for v in self.historial_ventas if self._fecha_es_hoy(v.get("fecha", "")))
        productos_stock_bajo = sum(1 for t in self.inventario if 0 < int(t.get("stock", 0)) <= STOCK_MINIMO)

        self.texto.insert(tk.END, "      /\\___/\\  \n     (  o . o ) \n      >   ^  <  \n\n")
        self.texto.insert(tk.END, "-" * 60 + "\n\n")
        self.texto.insert(tk.END, "  👻 Bienvenido a Urban Threads 👻\n\n")
        self.texto.insert(tk.END, "-" * 60 + "\n\n")

        self.texto.insert(tk.END, "RESUMEN RÁPIDO:\n", "titulo")
        self.texto.insert(tk.END, f"Modelos Únicos: {total_modelos}\n")
        self.texto.insert(tk.END, f"Total de Pares en Stock: {total_pares}\n")
        self.texto.insert(tk.END, f"Ventas Registradas (Hoy): {ventas_hoy}\n\n")

        if productos_stock_bajo > 0:
            self.texto.insert(tk.END, f"¡ALERTA DE STOCK BAJO!: {productos_stock_bajo} productos necesitan reabastecimiento.\n", "alerta")
        else:
            self.texto.insert(tk.END, "¡Inventario en buen estado!\n")

        self.texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")

    def _fecha_es_hoy(self, fecha_str):
        try:
            dt = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            return dt.date() == datetime.now().date()
        except Exception:
            return False

    def mostrar_inventario(self):
        self.texto.delete(1.0, tk.END)
        self.activar_boton(self.btn_inventario)

        if not self.inventario:
            self.texto.insert(tk.END, "X No hay productos en el inventario\n")
            return

        header = f"{'ID':<5} | {'MODELO':<36} | {'PRECIO':<12} | {'TALLA':<6} | {'MARCA':<12} | {'STOCK':<6}\n"
        self.texto.insert(tk.END, "=== 👟 INVENTARIO COMPLETO ===\n\n")
        self.texto.insert(tk.END, header)
        self.texto.insert(tk.END, "-" * 100 + "\n")

        for p in self.inventario:
            linea = f"{p['id']:<5} | {p['modelo'][:36]:<36} | ${float(p['precio']):<10.2f} | {p['talla']:<6} | {p['marca'][:12]:<12} | {int(p['stock']):<6}"
            self.texto.insert(tk.END, linea)
            # indicadores por producto
            if 0 < int(p.get("stock", 0)) <= STOCK_MINIMO:
                self.texto.insert(tk.END, "  , STOCK BAJO", "alerta")
            elif int(p.get("stock", 0)) == 0:
                self.texto.insert(tk.END, "  , AGOTADO", "agotado")
            self.texto.insert(tk.END, "\n")

    def agregar_tenis(self):
        self.activar_boton(self.btn_agregar)
        new_id = generar_nuevo_id(self.inventario)

        modelo = simpledialog.askstring("Agregar Producto", "1. Nombre del modelo (Obligatorio):", parent=self.root)
        if not modelo:
            return

        marca = simpledialog.askstring("Agregar Producto", "2. Marca/Categoría (Obligatorio):", parent=self.root)
        if not marca:
            return

        precio_str = simpledialog.askstring("Agregar Producto", "3. Precio unitario (Obligatorio):", parent=self.root)
        if precio_str is None:
            return
        precio_validado = validar_numero_positivo(precio_str, "Precio", entero=False)
        if precio_validado is None:
            return

        talla = simpledialog.askstring("Agregar Producto", "4. Talla (Obligatorio):", parent=self.root)
        if not talla:
            return

        stock_str = simpledialog.askstring("Agregar Producto", "5. Cantidad inicial (Stock) (Obligatorio):", parent=self.root)
        if stock_str is None:
            return
        stock_validado = validar_numero_positivo(stock_str, "Cantidad inicial", entero=True)
        if stock_validado is None:
            return

        descripcion = simpledialog.askstring("Agregar Producto", "6. Descripción adicional (Opcional):", parent=self.root)

        nuevo = {
            "id": new_id,
            "modelo": modelo.strip(),
            "marca": marca.strip(),
            "precio": float(precio_validado),
            "talla": talla.strip().upper(),
            "stock": int(stock_validado),
            "descripcion": descripcion.strip() if descripcion else "Sin descripción"
        }

        self.inventario.append(nuevo)
        guardar_inventario(self.inventario)
        messagebox.showinfo("Éxito", f"'{modelo}' agregado con ID {new_id} al inventario.")
        self.mostrar_inventario()

    def buscar_tenis(self):
        self.activar_boton(self.btn_buscar)

        if not self.inventario:
            messagebox.showwarning("Sin inventario", "No hay productos disponibles para buscar", parent=self.root)
            return

        criterio_busqueda = simpledialog.askstring("Buscar Producto", "Busca por: ID, Modelo, Marca o Talla:", parent=self.root)
        if not criterio_busqueda:
            return

        criterio = criterio_busqueda.lower().strip()
        resultados = []
        for p in self.inventario:
            if (criterio in str(p.get("id", "")).lower() or
                criterio in p.get("modelo", "").lower() or
                criterio in p.get("marca", "").lower() or
                criterio in str(p.get("talla", "")).lower()):
                resultados.append(p)

        self.texto.delete(1.0, tk.END)
        self.texto.insert(tk.END, f"RESULTADOS DE BÚSQUEDA: '{criterio_busqueda}' ===\n\n")
        if not resultados:
            self.texto.insert(tk.END, "X No se encontraron resultados\n")
            return

        self.texto.insert(tk.END, f"Se encontraron {len(resultados)} producto(s):\n\n")
        header = f"{'ID':<5} | {'MODELO':<36} | {'PRECIO':<12} | {'TALLA':<6} | {'MARCA':<12} | {'STOCK':<6}\n"
        self.texto.insert(tk.END, header)
        self.texto.insert(tk.END, "-" * 100 + "\n")

        for p in resultados:
            linea = f"{p['id']:<5} | {p['modelo'][:36]:<36} | ${float(p['precio']):<10.2f} | {p['talla']:<6} | {p['marca'][:12]:<12} | {int(p['stock']):<6}"
            self.texto.insert(tk.END, linea)
            if 0 < int(p.get("stock", 0)) <= STOCK_MINIMO:
                self.texto.insert(tk.END, "  , STOCK BAJO", "alerta")
            elif int(p.get("stock", 0)) == 0:
                self.texto.insert(tk.END, "  , AGOTADO", "agotado")
            self.texto.insert(tk.END, "\n")

    def vender_tenis(self):
        self.activar_boton(self.btn_vender)

        if not self.inventario:
            messagebox.showwarning("Sin Inventario", "No hay productos disponibles para vender", parent=self.root)
            return

        # Mostrar opciones numeradas
        opciones = "\n".join([f"{i+1}. ID: {p['id']} - {p['modelo']} ({p['marca']}) - Stock: {p['stock']}"
                              for i, p in enumerate(self.inventario)])
        seleccion = simpledialog.askinteger("Vender Producto", f"Selecciona el NÚMERO del producto a vender:\n\n{opciones}", parent=self.root)

        if seleccion is None:
            return
        if seleccion < 1 or seleccion > len(self.inventario):
            messagebox.showerror("Error", "Selección inválida.")
            return

        producto = self.inventario[seleccion - 1]
        if int(producto.get("stock", 0)) <= 0:
            messagebox.showwarning("Sin stock", "Este modelo está agotado.", parent=self.root)
            return

        cantidad_str = simpledialog.askstring("Vender Producto", f"¿Cuántas unidades de {producto['modelo']} quieres vender?", parent=self.root)
        if cantidad_str is None:
            return
        cantidad_validada = validar_numero_positivo(cantidad_str, "Cantidad a vender", entero=True)
        if cantidad_validada is None:
            return
        cantidad = int(cantidad_validada)

        if cantidad > int(producto.get("stock", 0)):
            messagebox.showerror("Error de Venta", f"Solo hay {producto.get('stock', 0)} unidades disponibles. No se puede vender {cantidad}.")
            return

        monto_total = cantidad * float(producto["precio"])
        producto["stock"] = int(producto.get("stock", 0)) - cantidad

        registro = {
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "id_producto": producto["id"],
            "modelo": producto["modelo"],
            "cantidad": cantidad,
            "precio_unitario": float(producto["precio"]),
            "total": float(monto_total)
        }
        self.historial_ventas.append(registro)
        guardar_ventas(self.historial_ventas)
        guardar_inventario(self.inventario)

        messagebox.showinfo("Venta Registrada",
                            f"Se vendieron {cantidad} unidades de '{producto['modelo']}'\nMonto Total: ${monto_total:.2f}")

        self.mostrar_resumen_venta(registro)

    def mostrar_resumen_venta(self, venta):
        self.texto.delete(1.0, tk.END)
        self.texto.insert(tk.END, "= VENTA REGISTRADA =\n\n")
        self.texto.insert(tk.END, "DETALLES DE LA VENTA:\n", "titulo")
        self.texto.insert(tk.END, f"Fecha y Hora: {venta['fecha']}\n")
        self.texto.insert(tk.END, f"Producto ID: {venta['id_producto']}\n")
        self.texto.insert(tk.END, f"Nombre: {venta['modelo']}\n")
        self.texto.insert(tk.END, f"Cantidad: {venta['cantidad']} unidades\n")
        self.texto.insert(tk.END, f"Precio Unitario: ${venta['precio_unitario']:.2f}\n")
        self.texto.insert(tk.END, f"TOTAL: ${venta['total']:.2f}\n", "total")
        self.texto.insert(tk.END, "\n¡La venta ha sido registrada exitosamente!\n")

    def mostrar_historial(self):
        self.activar_boton(self.btn_historial)
        self.texto.delete(1.0, tk.END)
        self.texto.insert(tk.END, "=== HISTORIAL DE VENTAS ===\n\n")
        if not self.historial_ventas:
            self.texto.insert(tk.END, "No hay ventas registradas.\n")
            return

        # Mostrar de forma tabular
        cab = f"{'FECHA':<18} | {'ID':<5} | {'MODELO':<36} | {'CANT':<4} | {'TOTAL':<10}\n"
        self.texto.insert(tk.END, cab)
        self.texto.insert(tk.END, "-" * 90 + "\n")
        for v in self.historial_ventas:
            linea = f"{v.get('fecha',''):<18} | {v.get('id_producto',''):<5} | {v.get('modelo','')[:36]:<36} | {v.get('cantidad',0):<4} | ${v.get('total',0):<10.2f}\n"
            self.texto.insert(tk.END, linea)

    def guardar_datos(self):
        guardar_inventario(self.inventario)
        guardar_ventas(self.historial_ventas)
        messagebox.showinfo("Guardado", "Inventario y ventas guardados correctamente.")

# ---------------------------
# Main
# ---------------------------
def main():
    root = tk.Tk()
    app = UrbanThreadsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
