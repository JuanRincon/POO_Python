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

	# Suma de 2 números complejos
	def numeroComplejoSuma(self, numero):
		self.ParteReal = self.ParteReal + numero.ParteReal
		self.ParteImaginaria = self.ParteImaginaria + numero.ParteImaginaria

	# Resta de 2 números complejos
	def numeroComplejoResta(self, numero):
		self.ParteReal = self.ParteReal - numero.ParteReal
		self.ParteImaginaria = self.ParteImaginaria - numero.ParteImaginaria




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


sy("clear")

# Creación de un objeto asociado a la clase
primerNumero = NumeroComplejo(12.0,4.0)
print("Primer número complejo")

# Uso de los métodos asociados al objeto
primerNumero.imprimirNumero()
print("Segundo número complejo")
segundoNumero = NumeroComplejo(8.0,4.5)
segundoNumero.imprimirNumero()
print("Suma de ambos números complejos")
primerNumero.numeroComplejoSuma(segundoNumero)
primerNumero.imprimirNumero()


