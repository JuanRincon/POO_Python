class Casa:

	def __init__(self, color='rojo'):
		self.color = color
		self.consumo_de_luz = 0
		self.consumo_de_agua = 19
	

	def pintar(self, color):
		self.color = color

	def prender_luz(self):
		self.consumo_de_luz += 10

	def abrir_ducha(self):
		self.consumo_de_agua += 10

	def tocar_timbre(self):
		print("RRRIIIIIIIING")
		self.consumo_de_luz += 2

mi_casa = Casa("verde")
print(mi_casa.color)
mi_casa.tocar_timbre()
print(mi_casa.consumo_de_luz)

class Mansion(Casa):
	def prender_luz(self):
		self.consumo_de_luz += 50

	def abrir_ducha(self):
		self.consumo_de_agua += 50

	def tocar_timbre(self):
		print("DING DONG")
		self.consumo_de_luz += 3

mi_mansion = Mansion('azul')
print("El color de mi mansión es : ", mi_mansion.color)
