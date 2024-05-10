# Hacemos override a metodos de la clase base

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

		super().__init__(nombre, edad)

		self.sueldo=sueldo
		self.puesto=puesto

	def mayorEdad(self):
		if(self.edad>=25):
			print('Bienvenido a la empresa')
			return True
		else:
			print('La empresa no contrata a menores de 25')
			return False

	# Hacemos override a muestra Datos
	def muestraDatos(self):
		print('Nombre:',self.nombre)

		if self.mayorEdad()==True:
			print('--- Infomración de empleado ---')

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

print('---------')

# Creamos otra instancia
e2=Empleado('Aldo',23,10000,'DBA')

print(e2.mayorEdad())
e2.muestraDatos()

