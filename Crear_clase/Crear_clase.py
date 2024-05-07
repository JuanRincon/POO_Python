# Creamos una clase
class Vector:
    # Creamos un metodo
    # self es una referencia al objeto que invoca el metodo
    # tambien se le conoce como variable de instancia
    def inicializa(self):
        # Colocamos los atributos
        self.x=0
        self.y=0

# Creamos la instancia
v1=Vector()

# Invocamos el metodo
v1.inicializa()

# Accedemos a los atributos para imprimir sus contenidos
print(v1.x,v1.y)

# Coloca un valor en el atributo
v1.x=5

print(v1.x,v1.y)

###

# Creamos un segundo objeto
v2=Vector()

v2.inicializa()
print(v2.x,v2.y)

v2.x=3
v2.y=7

# Cada objeto tiene una vida por separado y guarda valores en sus
# propios atributos
print(v1.x,v1.y)
print(v2.x,v2.y)

# Una forma no recomendable de adicionar atributos
v1.z=6

print(v1.x, v1.y, v1.z)

# El atributo no se comparte co la otra instancia, pues no esta
# declrado en la clase
# print(v2.x, v2.y, v2.z) /Por lo tanto esto último así como está nos saca un error