from decorator.hero import Hero

class Superman(Hero):
	__amountOfDestruction = None
	def __init__(self):
		self.__amountOfDestruction = 6

	def displayPower(self):
		return "fly "

	def attack(self):
		return self.__amountOfDestruction

	def setDamage(self,damage):
		self.__amountOfDestruction = damage
