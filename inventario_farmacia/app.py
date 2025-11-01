import json
import customtkinter
from medicamentos import metodos  # Importa tu clase inventario

# --- Crear el inventario y cargar los datos ---
inventario = metodos()
try:
    inventario.cargar_desde_json()
except:
    pass

# --- Funciones para la interfaz ---
def agregar_medicamento_interfaz():
    nombre = entry_nombre.get().strip()
    cantidad = entry_cantidad.get().strip()
    uso = entry_uso.get().strip()
    fecha = entry_fecha.get().strip()

    if not (nombre and cantidad and uso and fecha):
        mostrar_mensaje("Por favor completa todos los campos.")
        return

    if not cantidad.isdigit():
        mostrar_mensaje("Cantidad debe ser numérica.")
        return

    inventario.agregar(nombre, cantidad, uso, fecha)
    inventario.almacen()
    limpiar_campos()
    actualizar_lista()
    mostrar_mensaje(f"Medicamento '{nombre}' agregado correctamente.")

def buscar_medicamento_interfaz():
    nombre = entry_buscar.get().strip()
    if not nombre:
        mostrar_mensaje("Escribe un nombre para buscar.")
        return
    res = inventario.look_for(nombre)
    if res:
        mostrar_mensaje(f"Encontrado: {res['nombre']} (Cantidad: {res['cantidad']})")
    else:
        mostrar_mensaje(f"No se encontró '{nombre}'.")

def eliminar_medicamento_interfaz():
    nombre = entry_buscar.get().strip()
    if not nombre:
        mostrar_mensaje("Escribe un nombre para eliminar.")
        return
    eliminado = inventario.delete(nombre)
    if eliminado:
        inventario.almacen()
        actualizar_lista()
        mostrar_mensaje(f"'{nombre}' eliminado.")
    else:
        mostrar_mensaje(f"'{nombre}' no existe.")

def limpiar_campos():
    entry_nombre.delete(0, customtkinter.END)
    entry_cantidad.delete(0, customtkinter.END)
    entry_uso.delete(0, customtkinter.END)
    entry_fecha.delete(0, customtkinter.END)

def actualizar_lista():
    listbox.delete("1.0", customtkinter.END)
    datos = inventario.mostrar() or []  # Evita error si retorna None
    for med in datos:
        listbox.insert(customtkinter.END, f"{med['nombre']} | {med['cantidad']} | {med['uso']} | {med['fecha']}\n")

def mostrar_mensaje(texto):
    label_mensaje.configure(text=texto)

# --- Crear interfaz ---
app = customtkinter.CTk()
app.geometry("700x450")
app.title("Inventario de Medicamentos")

# --- Panel izquierdo: agregar medicamentos ---
frame_left = customtkinter.CTkFrame(app)
frame_left.pack(side="left", fill="y", padx=20, pady=20)

customtkinter.CTkLabel(frame_left, text="Nombre:").pack(anchor="w")
entry_nombre = customtkinter.CTkEntry(frame_left, width=200)
entry_nombre.pack(pady=(0,8))

customtkinter.CTkLabel(frame_left, text="Cantidad:").pack(anchor="w")
entry_cantidad = customtkinter.CTkEntry(frame_left, width=200)
entry_cantidad.pack(pady=(0,8))

customtkinter.CTkLabel(frame_left, text="Uso:").pack(anchor="w")
entry_uso = customtkinter.CTkEntry(frame_left, width=200)
entry_uso.pack(pady=(0,8))

customtkinter.CTkLabel(frame_left, text="Fecha:").pack(anchor="w")
entry_fecha = customtkinter.CTkEntry(frame_left, width=200)
entry_fecha.pack(pady=(0,8))

boton_agregar = customtkinter.CTkButton(frame_left, text="Agregar", command=agregar_medicamento_interfaz)
boton_agregar.pack(pady=(10,0))

# --- Panel derecho: buscar/eliminar/listar ---
frame_right = customtkinter.CTkFrame(app)
frame_right.pack(side="right", fill="both", expand=True, padx=20, pady=20)

customtkinter.CTkLabel(frame_right, text="Buscar/Eliminar por nombre:").pack(anchor="w")
entry_buscar = customtkinter.CTkEntry(frame_right, width=300)
entry_buscar.pack(pady=(0,8))

boton_buscar = customtkinter.CTkButton(frame_right, text="Buscar", command=buscar_medicamento_interfaz)
boton_buscar.pack(side="left", padx=5)

boton_eliminar = customtkinter.CTkButton(frame_right, text="Eliminar", command=eliminar_medicamento_interfaz)
boton_eliminar.pack(side="left", padx=5)

listbox = customtkinter.CTkTextbox(frame_right, height=200, width=400)
listbox.pack(fill="both", expand=True, pady=(10,10))

label_mensaje = customtkinter.CTkLabel(frame_right, text="")
label_mensaje.pack()

# --- Inicializar lista ---
actualizar_lista()

# --- Ejecutar app ---
app.mainloop()
