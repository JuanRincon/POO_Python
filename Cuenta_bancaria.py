# Inicio de clase

class CuentaBancaria:
	# Variables de la clase
	saldo = None
	nombre = None

	# Constructor de la clase
	def __init__(self, saldo, nombre):
		# Revisar si las variables de entrada son del tipo específico
		if ((type(saldo) == int or type(salso) == float) and isinstance(nombre, str)):
			self.saldo = saldo
			self.nombre = nombre
			self.mostrarInformacion()
		else:
			self.saldo = 0
			self.nombre = "Desconocido"
			self.mostrarInformacion()

	'''Despliego la representación de la cuenta bancaria como una cadena'''
	def mostrarInformacion(self):
		print(self.nombre + " cuenta con: " + str(self.saldo) + " de saldo")
	
	def deposito(self, cantidad):
		if type(cantidad) == int or type(cantidad) == float:
			print("Depósito de " + self.nombre + " por: " + str(cantidad))
			# Incrementar la cantidad de saldo
			self._calcularSaldo(self.saldo + cantidad)
			self.mostrarInformacion()
		else:
			print("Deposito de " + self.nombre + " por: " + str(cantidad))
			print("las cantidades deben ser números")

	def retiro(self, cantidad):
		if type(cantidad) == int or type(cantidad) == float:
			print("Retiro de " + self.nombre + " por: " + str(cantidad))
			cantidadRetirar = cantidad
			if cantidadRetirar > self.saldo:
				print(self.nombre + " No hay saldo suficiente.")
			else:
				# Reducir la cantidad del saldo de la cuenta
				self._calcularSaldo(self.saldo - cantidadRetirar)
				self.mostrarInformacion()
		else:
			print("Retiro de " + self.nombre + " por: " + str(cantidad))
			print("Las cantidades deben ser números.")

	def _calcularSaldo(self, cantidad):
		# Obtener el saldo asociado a la cuenta
		self.saldo = cantidad
	# Fin de clase

objeto1 = CuentaBancaria(12, "Pedro")
objeto2 = CuentaBancaria(125, "Juan")

# Manipulación de las funciones de los objetos
objeto2.retiro(89)
objeto1.retiro(12000)
objeto1.deposito("mil doscientos")
objeto2.deposito(1200)

