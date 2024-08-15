from os import system as sy

sy('clear')

class NumeroComplejo:
    ParteReal = 0
    ParteImaginaria = 0

    def __init__(self, real, imaginaria):
        self.ParteReal = real
        self.ParteImaginaria = imaginaria

    def imprimirNumero(self):
        print(str(self.ParteReal) + " + i * " + str(self.ParteImaginaria))

    def CambiarParteReal(self, real):
        self.ParteReal = real

    def obtenerParteReal(self):
        return self.ParteReal

    def cambiarParteImaginaria(self, imaginaria):
        self.ParteImaginaria = imaginaria

    def obtenerParteImaginaria(self):
        return self.ParteImaginaria



nuevoNumero = NumeroComplejo(12.0,3.0)

#NumeroComplejo.imprimirNumero()
nuevoNumero.imprimirNumero()
 
primerNumero = NumeroComplejo(12.0, 4.0)
print("número complejo versión inicial")
primerNumero.imprimirNumero()
print("número complejo modificado (cambiar valor de la parteReal)")
primerNumero.CambiarParteReal(24.0)
primerNumero.imprimirNumero()
print("Parte imaginaria en otro cálculo (parteImaginaria + 5.0)")
print( (primerNumero.obtenerParteImaginaria() ) + 5.0)
