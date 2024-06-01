import os

class Producto:
    ProductID=1
    def __init__(self, desc, precio):
        self.id=Producto.ProductID
        self.desc=desc
        self.precio=precio
        Producto.ProductID+=1

    def mostrarProducto(self):
        print("ID: ", self.id, " - Nombre: ",self.desc," - Precio: ",self.precio )

    def getPrecio(self):
        return self.precio
    1
    def getID(self):
        return self.id
    
    def getDesc(self):
        return self.desc
    
class Factura:
    FacturaID=1
    def __init__(self, monto_impuestos, total, productos):
        self.id=Factura.FacturaID
        self.monto_impuestos=monto_impuestos
        self.total=total
        self.productos=productos

    def imprimirProductos():
        for producto in productos:
            producto.mostrarProducto()

    def mostrarFactura(self):
        print("ID: ", self.id, " - Impuestos: ", self.monto_impuestos, " - Total: ", self.total)
        Factura.imprimirProductos()
        print("\n")

productos=[]
productos.append(Producto("Arroz",50))
productos.append(Producto("Habichuelas",80))
productos.append(Producto("Pollo",85))

facturas=[]

def imprimirMenu():
    print("Menú")
    for producto in productos:
        producto.mostrarProducto()

def buscar_producto(id):
    for producto in productos:
        if(producto.id==id):
            return producto
    return None

def calcular_factura(carrito):
    total=0
    for producto in carrito:
        total+=producto.getPrecio()
    impuestos=total*0.18
    return impuestos, total

def facturar():
    seguir_facturando=1
    while seguir_facturando==1:
        carrito=[]
        salir_o_no=1
        while salir_o_no==1:
            os.system("cls")
            imprimirMenu()
            opc=int(input("Ingresa el índice del producto que deseas: "))
            productoTemp=buscar_producto(opc)
            if (productoTemp):
                carrito.append(productoTemp)
            else:
                print("El producto no existe")
            salir_o_no=int(input("Deseas agregar más productos? 1. Sí 2. No: "))
        impuestos, total = calcular_factura(carrito)
        facturas.append(Factura(impuestos, total, carrito))
        seguir_facturando=int(input("Deseas seguir facturando? 1. Sí 2. No: "))

facturar()

for factura in facturas:
    factura.mostrarFactura()
