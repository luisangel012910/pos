import os
from datetime import datetime
from tabulate import tabulate

class Producto:
    ProductID = 1
    def __init__(self, desc, precio):
        self.id = Producto.ProductID
        self.desc = desc
        self.precio = precio
        Producto.ProductID += 1

    def mostrarProducto(self):
        return [self.id, self.desc, self.precio]

    def getPrecio(self):
        return self.precio

class Factura:
    FacturaID = 1
    def __init__(self, cliente, fecha_emision):
        self.id = Factura.FacturaID
        self.cliente = cliente
        self.fecha_emision = fecha_emision
        self.monto_impuestos = 0
        self.total = 0
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def calcular_factura(self):
        self.total = sum(producto.getPrecio() * cantidad for producto, cantidad in self.productos.items())
        self.monto_impuestos = self.total * 0.18

    def generar_tabla_productos(self):
        table = []
        for producto, cantidad in self.productos.items():
            table.append([producto.id, producto.desc, producto.precio, cantidad, producto.precio * cantidad])
        return table

    def mostrarFactura(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n========================= FACTURA =========================")
        print("ID de Factura:", self.id)
        print("Cliente:", self.cliente)
        print("Fecha de emisión:", self.fecha_emision.strftime("%Y-%m-%d %H:%M:%S"))
        print("------------------------------------------------------------")
        print(tabulate(self.generar_tabla_productos(), headers=["ID", "Descripción", "Precio Unitario", "Cantidad", "Precio Total"], tablefmt="pretty"))
        print("------------------------------------------------------------")
        print("Subtotal:", sum(producto.getPrecio() * cantidad for producto, cantidad in self.productos.items()))
        print("Itebis:", self.total * 0.18)
        print("Total:", self.total)
        print("============================================================")

productos = []
productos.append(Producto("Arroz", 50))
productos.append(Producto("Habichuelas", 80))
productos.append(Producto("Pollo", 85))

facturas = []

def imprimirMenu():
    print("Menú")
    for producto in productos:
        print(producto.mostrarProducto())

def buscar_producto(id):
    for producto in productos:
        if producto.id == id:
            return producto
    return None

def facturar():
    nombre_cliente = input("Ingrese su Nombre: ")
    fecha_emision = datetime.now()
    factura_actual = Factura(nombre_cliente, fecha_emision)
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        imprimirMenu()
        opc = int(input("Ingrese el ID del producto que desea (0 para finalizar): "))
        if opc == 0:
            facturas.append(factura_actual)
            break
        producto = buscar_producto(opc)
        if producto:
            cantidad = int(input(f"Ingrese la cantidad de '{producto.desc}' que desea: "))
            if cantidad > 0:
                factura_actual.agregar_producto(producto, cantidad)
            else:
                print("La cantidad debe ser mayor que cero.")
        else:
            print("El producto no existe")

facturar()

for factura in facturas:
    factura.calcular_factura()
    factura.mostrarFactura()
