
import math

""" Para este caso se le da al constructor unos valores por default 
que pueden servirnos por seguridad o para cuando en alguna aplicación
hay unos valores que son los normalmente usados y pocas veces hay que
cambiarlos"""

# Creamos una clase
class Vector:

    def __init__(self, x=5, y=5):
        # Colocamos los atributos
        self.x=x
        self.y=y

    # Creamos otro método
    def Muestra(self):
        print(self.x,self.y)

# Y un método que regrese un valor
    def magnitud(self):
        return math.sqrt(self.x**2+self.y**2)

v1 = Vector(4,5)

# Invocamos el metodo
v1.Muestra()

# Obtener la magnitud
m=v1.magnitud()
print("La magnitud es", m)

print("-------------")
# Aquí no pasamos parametros y usa el valor de default
v2=Vector()
v2.Muestra()
m2=v2.magnitud()
print(m2)