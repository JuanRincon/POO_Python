
import math

# Creamos una clase
class Vector:
    """
    Un cosntructor es un método que se invoca automaticamente cuando
    el objeto es creado/intanciado
    El constructor en python es el metodo __new__, pero se usa solamente
    en casos avanzados
    El método __init__ tambien se invoco automaticamente en el proceso
    de intanciación y es la opción preferida para llevar a cabo
    las instancias del objeto en python
    """
    def __init__(self, x, y):
        # Colocamos los atributos
        self.x=x
        self.y=y

    # Creamos otro método
    def Muestra(self):
        print(self.x,self.y)

# Y un método que regrese un valor
    def magnitud(self):
        return math.sqrt(self.x**2+self.y**2)

# Creamos el objeto
""" Ya no necesitamos invocar a inicializa manualmente
simplemente pasamos los parametros al instanciar el objeto"""

v1 = Vector(4,5)

# Invocamos el metodo
v1.Muestra()

# Obtener la magnitud
m=v1.magnitud()
print("La magnitud es", m)
