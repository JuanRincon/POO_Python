""" En otros lenguajes tenemos diferentes tipos de acceso a los datos
publico, privado, protegido
Esto nos permite tener encapsulación

Python ve todos los métodos y datos como si fueran públicos
y deja a la buena voluntad del programador respetar el acceso al dato

Para indicar que un dato es privado se recomienda colocar la información
en la documentación/doctring

Por convención si deseamos que un atributo sea tratado como privado
colocamos _ antes del nombre _costo"""

# Creamos una clase
class Producto:

    def __init__(self):
        self.cantidad = 10

        # Indicamos que costo es privado
        self._costo=5

# Creamos una intancia
manzana=Producto()

# Hacemos uso de cantidad
print(manzana.cantidad)

# Ahora hacemos uso de costo
# aunque no deberiamos por estar indicado como privado
# pero nada en el lenguaje nos impide usarlo

print(manzana._costo)
manzana._costo=56
print(manzana._costo)

print("-------------------------------------")
print("######################################")
####################################################

""" El usar _ es por convención
El usar __ no es una convención, tiene un significado especial para el
interprete. Se usa para evitar colisiones de nombres cuando se definen subclases
Esto se llama name mangling, el interprete cambia el nombre para que sea
menos posible tener coliciones si la clase se extiende"""

class Producto2:

    def __init__(self):
        self.cantidad=10

        # Indicamos que costo es privado
        self._costo=5

        # Creamos el atributo
        self.__impuesto=0.16

# Al usar __ podemos pensar que tenemos un acceso privado, pero no es así

pera=Producto2()

print(pera.cantidad, pera._costo)
#print(pera.__impuesto)

# veamos que sucede
# Al nombre del atributo se le ha adiciconado _Producto2
a = dir(pera)   # Para ver los atributos de pera le asignamos el resultado del método dir a la variable a e imprimimos
print(a)

# Si ponemos el nombre completo podemos hacer uso directo, lo que
# comprueba que no es un aaceso privado
print(pera._Producto2__impuesto)  # El nombre que se le asignó con __impuesto, por el name mangling fue _Producto2__impuesto

print("-------------------------------------")
print("######################################")
####################################################

# El usar - al final del nombre es usado para evitar conflicto con
# palabras reservadas de python

"""def funcion1(class, nombre):      Si se hace de esta manera sacara error por usar la palabra reservada class
    pass"""

# Ahora podemos usar un parametro con nombre class
def funcion2(class_, nombre):
    pass