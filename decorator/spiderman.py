from decorator.hero import Hero

class Spiderman(Hero):
	__amountOfDestruction = None
	def __init__(self):
		self.__amountOfDestruction = 5

	def displayPower(self):
		return "net "

	def attack(self):
		return self.__amountOfDestruction

	def setDamage(self,damage):
		self.__amountOfDestruction = damage
