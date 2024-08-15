from os import system as sy

sy('clear')


class Hola:
    Nombre = ""
    Apellido = ""

    def __init__(self,nombre,apellido):
        print("Constructor de la clase")

        self.Nombre = nombre
        self.Apellido = apellido

    def saludo(self):
        print("Hola" + " " + self.Nombre + " " + self.Apellido)
        
primerObjeto = Hola("Juan","Perez")

primerObjeto.saludo()
