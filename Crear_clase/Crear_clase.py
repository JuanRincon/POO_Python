
import math

""" Python no permite la sobrecarga de los constructores
cosa que si permiten otros lenguajes

Si intentamos hacerla, obtenemos un warning y un error al
ejecutar pues unicamente la última definición es la que se toma
en cuenta"""
class Alumno():

    # Este es el primer init
    def __init__(self, *args):

        # Verificamos cuando no nos pasan parametros
        if len(args)==0:
            self.nombre="Por asignar"
            self.edad=0
            self.calificacion=0

        if len(args)==3:
            self.nombre=args[0]

            if(args[1]>=18):
                self.edad=args[1]
            else:
                print("Edad invalida")
                self.edad=0

            if(args[2]>=0):
                self.calificacion=args[2]
            else:
                print("Calificación invalida")
                self.calificacion=0

    def muestraDatos(self):
        print(self.nombre, self.edad, self.calificacion)

# Creamos un objeto

a1=Alumno()
a1.muestraDatos()

# Creamos un segundo objeto
a2=Alumno('Ana',20,10)
a2.muestraDatos()
