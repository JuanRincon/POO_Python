# El otro tipo de herencia que existe es al herencia múltiple

# Inicio de la clase padre Operación
class Operacion:
	# Atributos de la clase
	valor1 = 0
	valor2 = 0

	# Métodos de la clase
	# Constructor de la clase
	def __init__(self, numero1, numero2):
		self.valor1 = numero1
		self.valor2 = numero2

	# Obtener valor1 (getter)
	def obtenerValor1(self):
		return self.valor1

	# Obtener valor2 (getter)
	def obtenerValor2(self):
		return self.valor2

	# Cambiar valor1 (setter)
	def cambiarValor1(self, numeroValor):
		self.valor1 = nuevoValor

	# Cambiar valor2 (setter)
	def cambiarValor2(self, numeroValor):
		self.valor2 = nuevoValor

	# Imprimir número
	def imprimirValor(self, numero):
		print(numero)

# Fin de la clase operación
