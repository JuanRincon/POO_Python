# Acá se usará la herencia simple con la reescritura de métodos
from herencia_simple import Operacion
from os import system as sy

sy('clear')

# Inicio de la clase hijo Multiplicación
class multiplicacion(Operacion):
	# Se llama al contructor de la clase padre para inicializar los números.
	def __init__(self, numero1, numero2):
		super().__init__(numero1, numero2)

	def multiplicar(self):
		self.imprimirValor(self.valor1*self.valor2)

	# Se sobreescribe un método de la clase padre
	def imprimirValor(self, numero):
		print("El número es: " + str(numero))

# Fin de la clase hijo Multiplicación

multiplicacion1 = multiplicacion(10, 5)
multiplicacion1.imprimirValor(multiplicacion1.obtenerValor1())
multiplicacion1.imprimirValor(multiplicacion1.obtenerValor2())
print("Resultado de la multiplicación")
multiplicacion1.multiplicar()
