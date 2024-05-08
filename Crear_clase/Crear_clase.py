# Adicionamos métodos

import math

# Creamos una clase
class Vector:
    # Creamos un metodo que recibe parametros
    # esto facilita la inicializacion
    def inicializa(self, x, y):
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
v1 = Vector()

# Invocamos el metodo
v1.inicializa(4,5)


# Obtener la magnitud
m=v1.magnitud()
print("La magnitud es", m)
