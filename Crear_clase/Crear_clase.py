# Aprendemos con reutilizar el código de la clase base

# Esta es la clase base
class Persona:
	def __init__(self, nombre, edad):
		self.nombre=nombre
		self.edad=edad

	def mayorEdad(self):
		if(self.edad>=18):
			return True
		else:
			return False

	def muestraDatos(self):

		print('El nombre es ', self.nombre)
		print('La edad es ', self.edad)

# Hacemos una herencia
class Empleado(Persona):
	def __init__(self, nombre, edad, sueldo, puesto):

		# Por medio de super() invocamos métodos que existan en la clase base
		# y podemos hacer reutilización de código

		# Aprovechamos que init de Persona ya inicializa algunos atrubutos
		super().__init__(nombre, edad)

		# Ahora inicalizamos los propios
		self.sueldo=sueldo
		self.puesto=puesto

	def muestraDatos(self):

		# Aprovechamos el muestraDatos de Persona
		super().muestraDatos()

		# Adicionamos lo propio
		print('Sueldo: $',self.sueldo)
		print('Puesto:',self.puesto)

# Creamos una intancia
p1=Persona('Ana',25)

print(p1.mayorEdad())
p1.muestraDatos()

print('---------')

# Creamos otra instancia
e1=Empleado('Juan',30,15000,'Analista')

print(e1.mayorEdad())
e1.muestraDatos()
