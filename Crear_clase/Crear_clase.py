""" La herencia es una forma de la POO para llevar a cabo reutilización de código
Con la herencia creamos una relación del tipo 'Es un'
Tenemos una clase base que es extendida por la clase hija
Adquiere todo lo que existe en la clase base y adiciona lo suyo propio

Hay una clase especial construida en el lenguaje llamada object
Provee ciertos metadatos y algunos comportamientos que le peermiten
a python tratar a todos los objetos de formama consistente

Todas las clases en python descienden de object, pero no necesitamos
colocarlo de la forma explicita, el lenguaje lo hace por nosotros"""

import statistics as st

# definimos la clase
# Esta sera la clase base

class Calificaciones:
    
    def __init__(self, lista):
        self.lista=lista
        
    def minimo(self):
        return min(self.lista)
    
    def maximo(self):
        return max(self.lista)
    
# Llevmos a cabo la herencia
# La clas de la cual desciende se coloca entre parentesis

class Estadistica(Calificaciones):
    
    # Adicionamos los metodos propios
    def promedio(self):
        return st.mean(self.lista)
        
    def mediana(self):
        return st.median(self.lista)
    
    def moda(self):
        return st.mode(self.lista)

# creamos la lista
calif=[8,10,9,8,8,7,8,9,10,5,5,6,6,9,9,9,9]

# Creamos la instancia de Calificaciones
MisCalifs=Calificaciones(calif)

# Invocamos sus métodos
print(MisCalifs.minimo())
print(MisCalifs.maximo())

# Creamos la instancia de la clase estadistica

MiEst=Estadistica(calif)

# Comprobamos  que podemos usar metodos de la clase base
print(MiEst.promedio())
print(MiEst.mediana())
print(MiEst.moda())

# La clase base no tiene acceso a ellos
#print(MisCalifs.promedio())

