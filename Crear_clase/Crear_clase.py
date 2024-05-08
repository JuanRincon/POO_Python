
import math

""" Python no permite la sobrecarga de los constructores
cosa que si permiten otros lenguajes

Si intentamos hacerla, obtenemos un warning y un error al
ejecutar pues unicamente la última definición es la que se toma
en cuenta"""
class Alumno():

    # Este es el primer init
    def __init__(self):
        self.nombre="Por asignar"
        self.edad=0
        self.calificacion=0

    # Esta es la sobrecarga dle init
    def __init__(self,nombre,edad,calificacion):
        self.nombre=nombre

        if(edad>=18):
            self.edad=edad
        else:
            print("Edad invalida")

        if(calificacion>=0):
            self.calificacion=calificacion
        else:
            print("Calificación invalida")
            self.calificacion=0

    def muestraDatos(self):
        print(self.nombre, self.edad, self.calificacion)

# Creamos un objeto

    #a1=Alumno()
    #a1.muestraDatos()

# Creamos un segundo objeto
a2=Alumno('Ana',20,10)
a2.muestraDatos()
