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

# Inicio de la clase hijo suma
class Suma(Operacion):

	# Se llama al constructor de la clase padre para iniciar los números
	def __init__(self, numero1, numero2):
		super().__init__(numero1, numero2)

	# Se agrega un método nuevo a la clase suma(que no está en la clase padre)
	def sumar(self):
		self.imprimirValor(self.valor1 + self.valor2)

# Fin de la clase suma

# Crea de objeto de la clase hijo
suma1 = Suma(10, 5)
print("Operando 1 de la suma")
suma1.imprimirValor(suma1.obtenerValor1())
print("Operando 2 de la suma")
suma1.imprimirValor(suma1.obtenerValor2())
print("Resultado de la suma")
suma1.sumar()
