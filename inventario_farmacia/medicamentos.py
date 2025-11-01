# --- TODO el código de clases y métodos queda igual ---
import json

class Nodo:
    def __init__(self, nombre, cantidad, uso, fecha):
        self.nombre = nombre
        self.cantidad = cantidad
        self.uso = uso
        self.fecha = fecha
        self.next = None

class metodos:
    def __init__(self):
        self.head = None

    def agregar(self, nombre, cantidad, uso,  fecha):
        nuevo = Nodo(nombre, cantidad, uso, fecha)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo        

    def mostrar(self):
        actual = self.head
        if not actual:
            print("No hay medicamentos por mostrar")
            return []
        lista = []
        while actual:
            lista.append({
                "nombre": actual.nombre,
                "cantidad": actual.cantidad,
                "uso": actual.uso,
                "fecha": actual.fecha
            })
            actual = actual.next
        return lista

    def delete(self,  dato):
        actual = self.head
        anterior = None
        if not self.head:
            print("No hay medicamentos registrados")
            return False
        while actual:
            if actual.nombre.lower() == dato.lower():
                if anterior is None:
                    self.head = actual.next
                else:
                    anterior.next = actual.next
                return True
            else:
                anterior = actual
                actual = actual.next
        return False

    def look_for(self, word):
        actual = self.head
        if not actual:
            return None
        while actual:
            if actual.nombre.lower() == word.lower():
                return {
                    "nombre": actual.nombre,
                    "cantidad": actual.cantidad,
                    "uso": actual.uso,
                    "fecha": actual.fecha
                }
            actual = actual.next
        return None

    def almacen(self):
        datos = []
        actual = self.head
        while actual:
            datos.append({
                "nombre": actual.nombre,
                "cantidad": actual.cantidad,
                "uso": actual.uso,
                "fecha": actual.fecha
            })
            actual = actual.next
        with open("inventario.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print("Inventario guardado correctamente.")

    def cargar_desde_json(self): 
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                for med in datos:
                    self.agregar(med["nombre"],  med["cantidad"], med["uso"], med["fecha"])
            print("Inventario cargado correctamente")
        except FileNotFoundError:
            print("No se encontró un archivo de inventario previo. Se creará uno nuevo")                        

# --- Solo ejecuta el menú de consola si corremos este archivo directamente ---
if __name__ == "__main__":
    inventario = metodos()
    inventario.cargar_desde_json()

    while True:
        print("\nWELCOME TO THE APP MEDICINE INVENTORY")
        print("===============================")
        print("1. Agregar medicamento")
        print("2. Buscar medicamento")
        print("3. Mostrar todos los medicamentos")
        print("4. Eliminar medicamento")
        print("5. Salir")
        try:
            option = int(input("SELECCIONA UNA OPCION: "))
        except ValueError:
            print("Error: Debe ingresar un número válido (1-5).")
            continue

        match option:
            case 1:
                nombre = input("INGRESE NOMBRE DEL MEDICAMENTO: ")
                cantidad = input("INGRESE CANTIDAD: ")
                uso = input("USO: ")
                fecha = input("FECHA DE VENCIMIENTO: ")
                inventario.agregar(nombre, cantidad, uso, fecha)
                inventario.almacen()
                print("DATOS CORRECTAMENTE INGRESADOS ")

            case 2:
                medicamento = input("INGRESE NOMBRE DEL MEDICAMENTO: ")
                inventario.look_for(medicamento)

            case 3:
                print("MOSTRANDO LOS MEDICAMENTOS")
                print("==========================")
                inventario.mostrar()

            case 4:
                MEDI = input("INGRESE NOMBRE DEL MEDICAMENTO A ELIMINAR: ")
                inventario.delete(MEDI)
                inventario.almacen()
                print("Medicamento eliminado")

            case 5:
                print("Salió del programa")
                break

            case _:
                print("Escriba un número dentro de las opciones válidas (1–5).")
