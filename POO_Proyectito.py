import os
from datetime import datetime

class Producto:
    ProductID = 1
    def __init__(self, desc, precio, stock):
        self.id = Producto.ProductID
        self.desc = desc
        self.precio = precio
        self.stock = stock
        Producto.ProductID += 1

    def mostrarProducto(self):
        return [self.id, self.desc, self.precio, self.stock]

    def getPrecio(self):
        return self.precio

class Factura:
    FacturaID = 1
    def __init__(self, cliente, fecha_emision):
        self.id = Factura.FacturaID
        self.cliente = cliente
        self.fecha_emision = fecha_emision
        self.productos = {}
        self.monto_impuestos = 0
        self.total = 0
        Factura.FacturaID += 1

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def calcular_factura(self):
        subtotal = sum(producto.precio * cantidad for producto, cantidad in self.productos.items())
        self.monto_impuestos = subtotal * 0.18
        self.total = subtotal + self.monto_impuestos

def imprimirMenu(productos):
    print("Menú")
    print("ID   | Descripción       | Precio Unitario | Stock")
    print("--------------------------------------------------")
    for producto in productos.values():
        print(f"{producto.id:<5}| {producto.desc:<17}| {producto.precio:^16}| {producto.stock:^5}")
    print("--------------------------------------------------")
    print("0. Finalizar compra")
    print("99. Ver todas las facturas")
    print("--------------------------------------------------")

def buscar_producto(productos, id):
    return productos.get(id, None)

def facturar(facturas):
    nombre_cliente = input("Ingrese su Nombre: ")
    fecha_emision = datetime.now()
    productos_disponibles = {
        1: Producto("Arroz", 50, 100),
        2: Producto("Habichuelas", 80, 80),
        3: Producto("Pollo", 85, 50),
        4: Producto("Leche", 30, 70),
        5: Producto("Huevos", 25, 60),
        6: Producto("Pan", 20, 120),
        7: Producto("Azúcar", 40, 90),
        8: Producto("Aceite", 60, 40),
        9: Producto("Café", 70, 55),
        10: Producto("Harina", 45, 85),
        11: Producto("Manzanas", 35, 65),
        12: Producto("Plátanos", 15, 100),
    }
    factura = Factura(nombre_cliente, fecha_emision)
    while True:
        carrito = {}
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            imprimirMenu(productos_disponibles)
            opc = input("Ingrese el ID del producto que desea o seleccione una opción: ")
            if opc == "0":
                break
            elif opc == "99":
                ver_facturas(facturas)
            else:
                opc = int(opc)
                producto = buscar_producto(productos_disponibles, opc)
                if producto:
                    cantidad = int(input(f"Ingrese la cantidad de '{producto.desc}' que desea: "))
                    if cantidad > 0:
                        if cantidad <= producto.stock:
                            factura.agregar_producto(producto, cantidad)
                            producto.stock -= cantidad
                        else:
                            print(f"No hay suficiente stock de '{producto.desc}'. Stock disponible: {producto.stock}.")
                    else:
                        print("La cantidad ingresada debe ser mayor que cero.")
                else:
                    print("El producto no existe")
        
        factura.calcular_factura()
        facturas.append(factura)
        
        os.system("cls" if os.name == "nt" else "clear")
        print("\n========================= FACTURA =========================")
        print("ID de Factura:", factura.id)
        print("Cliente:", factura.cliente)
        print("Fecha de emisión:", factura.fecha_emision.strftime("%Y-%m-%d %H:%M:%S"))
        print("------------------------------------------------------------")
        print("ID   | Descripción       | Precio Unitario | Cantidad | Precio Total")
        print("------------------------------------------------------------")
        for producto, cantidad in factura.productos.items():
            print(f"{producto.id:<5}| {producto.desc:<17}| {producto.precio:^16}| {cantidad:^9}| {producto.precio * cantidad:^13}")
        print("------------------------------------------------------------")
        subtotal = sum(producto.precio * cantidad for producto, cantidad in factura.productos.items())
        impuestos = subtotal * 0.18
        print("Subtotal:", subtotal)
        print("Impuestos (18%):", impuestos)
        print("Total:", subtotal + impuestos)
        print("============================================================")
        input("Presione Enter para continuar...")

def ver_facturas(facturas):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n===================== LISTA DE FACTURAS ====================")
    for factura in facturas:
        print("------------------------------------------------------------")
        print("ID de Factura:", factura.id)
        print("Cliente:", factura.cliente)
        print("Fecha de emisión:", factura.fecha_emision.strftime("%Y-%m-%d %H:%M:%S"))
        print("------------------------------------------------------------")
        print("ID   | Descripción       | Precio Unitario | Cantidad | Precio Total")
        print("------------------------------------------------------------")
        for producto, cantidad in factura.productos.items():
            print(f"{producto.id:<5}| {producto.desc:<17}| {producto.precio:^16}| {cantidad:^9}| {producto.precio * cantidad:^13}")
        print("------------------------------------------------------------")
        subtotal = sum(producto.precio * cantidad for producto, cantidad in factura.productos.items())
        impuestos = subtotal * 0.18
        print("Subtotal:", subtotal)
        print("Impuestos (18%):", impuestos)
        print("Total:", subtotal + impuestos)
        print("============================================================")
    input("Presione Enter para continuar...")

facturas = []
while True:
    facturar(facturas)
    opc = input("¿Desea crear otra factura? (s/n): ").lower()
    if opc != 's':
        break
