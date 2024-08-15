# Herencia multiple (NO SE RECOMIENDA POR LOS CONFLICTOS QUE PUEDE PRESNTAR ENTRE CLASES ESPECIALMENTE EN PROYECTOS GRANDES)
# Aunque es permitida por Python uno de los problemas es uno conocido como el problema del diamante


# Creamos una primera clase
class Producto():

    def __init__ (self, cantidad, costo):
        self.cantidad=cantidad
        self.costo=costo

    def calculaTotales(self):
        self.total=self.cantidad*self.costo
        print('Se tiene el total $', self.total)

    def muestraProducto(self):
        print('Se tienen ',self.cantidad, ' productos')
        print('El costo del producto es $', self.costo)
        self.calculaTotales()

# Creamos otra clase
class Fruta():

        def __init__(self, nombre, origen):
                self.nombre=nombre
                self.origen=origen

        def muestraFruta(self):
                print('La fruta es ', self.nombre)
                print('Con origenn en ', self.origen)

# Creamos una clase con herencia multiple
class Articulo(Producto, Fruta):

        def __init__(self, nombre, origen, cantidad, costo):
                Fruta.__init__(self, nombre, origen)
                Producto.__init__(self, cantidad, costo)

        def muestraArticulo(self):
                Fruta.muestraFruta(self)
                Producto.muestraProducto(self)

manzana=Articulo('Manzana', 'Mexico', 500, 10.56)

manzana.muestraArticulo()
